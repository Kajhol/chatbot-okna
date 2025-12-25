from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
import os

# Wczytaj klucz API
env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(env_path)

# Klient OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Wczytaj bazę wektorową
script_dir = os.path.dirname(os.path.abspath(__file__))
chroma_dir = os.path.join(script_dir, '..', 'knowledge_base')

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small",
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

vectorstore = Chroma(
    persist_directory=chroma_dir,
    embedding_function=embeddings,
    collection_name="wafam_knowledge"
)

print("Baza wektorowa załadowana!")

# FastAPI
app = FastAPI(
    title="WAFAM Chatbot API",
    description="AI Chatbot with Advanced RAG",
    version="2.4"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# System prompt (ZOPTYMALIZOWANY - krótszy)
# System prompt (ZOPTYMALIZOWANY + WERYFIKACJA)
SYSTEM_PROMPT = """Asystent WAFAM (okna, drzwi, rolety).

ZASADY:
- Odpowiadaj tylko z kontekstu, krótko (2-3 zdania)
- Brak cen. Zbieraj dane do wyceny: produkt, ilość, wymiary, miejscowość, montaż tak/nie, kontakt
- Max 1/2 pytanie na odpowiedź
- Linki: [tekst](url) - tylko gdy klient pyta gdzie czytać więcej
- Pamiętaj kontekst rozmowy
- NIE WYMYŚLAJ informacji których klient nie podał. Jeśli klient nie podał danych (telefon, email, adres) - zapytaj o nie zamiast udawać że je masz.
- Jeśli klient chce przekazać dane - najpierw zapytaj jakie dane chce zostawić (telefon lub email).

LINKI: okna-standardowe, okna-premium, systemy-przesuwne, system-tarasowy, drzwi-pelne, drzwi-przeszklone, rolety, zaluzje-fasadowe, bramy-garazowe (dodaj https://wafam.pl/ przed)"""
# Pamięć rozmów
conversations = {}

# Pamięć tematów rozmów
conversation_topics = {}

# Modele danych
class Message(BaseModel):
    text: str
    session_id: str = "default"

class Answer(BaseModel):
    bot: str
    sources: list[str] = []

# Funkcja wyszukiwania w bazie (2 fragmenty zamiast 3)
def search_knowledge(query: str, k: int = 2):
    results = vectorstore.similarity_search_with_score(query, k=k)
    
    contexts = []
    sources = []
    
    for doc, score in results:
        # Ogranicz długość fragmentu do 300 znaków
        content = doc.page_content[:300]
        contexts.append(content)
        title = doc.metadata.get('title', 'Nieznane')
        sources.append(title)
    
    return contexts, sources

# Funkcja rozszerzająca krótkie pytania o kontekst
def expand_query_with_context(user_message: str, session_id: str) -> str:
    short_responses = ["tak", "nie", "podaj", "link", "chcę", "poproszę", "dawaj", "ok", "okej", "dobrze"]
    message_lower = user_message.lower().strip()
    is_short = len(message_lower.split()) <= 4 and any(word in message_lower for word in short_responses)
    
    if is_short and session_id in conversation_topics:
        topic = conversation_topics[session_id]
        return f"{user_message} (kontekst: {topic})"
    
    product_keywords = ["okna", "okno", "drzwi", "rolety", "roleta", "bramy", "brama", "żaluzje", "taras", "przesuwne"]
    for keyword in product_keywords:
        if keyword in message_lower:
            conversation_topics[session_id] = user_message
            break
    
    return user_message

# Funkcja kompresji historii
def compress_history(history: list) -> list:
    """Zachowuje tylko ostatnie 4 wiadomości i skraca je"""
    if len(history) <= 4:
        return history
    
    compressed = []
    for msg in history[-4:]:
        content = msg["content"]
        # Skróć długie wiadomości do 200 znaków
        if len(content) > 200:
            content = content[:200] + "..."
        compressed.append({"role": msg["role"], "content": content})
    
    return compressed

# Funkcja czatu
def ask_wafam_bot(user_message: str, session_id: str) -> dict:
    if session_id not in conversations:
        conversations[session_id] = []
    
    history = conversations[session_id]
    
    # Rozszerz pytanie o kontekst jeśli jest krótkie
    expanded_query = expand_query_with_context(user_message, session_id)
    
    # Wyszukaj w bazie wiedzy (2 fragmenty, max 300 znaków każdy)
    contexts, sources = search_knowledge(expanded_query)
    context_text = "\n---\n".join(contexts)
    
    # Krótki prompt
    user_prompt = f"""KONTEKST:
{context_text}

PYTANIE: {user_message}"""

    history.append({"role": "user", "content": user_prompt})
    
    # Kompresuj historię
    compressed_history = compress_history(history)
    
    # Zbuduj wiadomości dla API
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    messages.extend(compressed_history)
    
    # Wyślij do OpenAI (max 200 tokenów odpowiedzi)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        max_tokens=200,
        temperature=0.3
    )
    
    bot_response = response.choices[0].message.content
    
    history.append({"role": "assistant", "content": bot_response})
    
    # Ogranicz historię do 6 wiadomości
    if len(history) > 6:
        conversations[session_id] = history[-6:]
    else:
        conversations[session_id] = history
    
    unique_sources = list(dict.fromkeys(sources))
    
    return {
        "bot": bot_response,
        "sources": unique_sources[:2]
    }

# ENDPOINT: Strona główna
@app.get("/")
def home():
    return {
        "status": "online",
        "message": "WAFAM Chatbot API with Advanced RAG",
        "version": "2.4"
    }

# ENDPOINT: Czat
@app.post("/chat", response_model=Answer)
def chat(message: Message):
    response = ask_wafam_bot(message.text, message.session_id)
    return response

# ENDPOINT: Wyczyść rozmowę
@app.post("/clear")
def clear_conversation(session_id: str = "default"):
    if session_id in conversations:
        del conversations[session_id]
    if session_id in conversation_topics:
        del conversation_topics[session_id]
    return {"status": "Rozmowa wyczyszczona", "session_id": session_id}

# ENDPOINT: Szukaj w bazie
@app.get("/search")
def search(query: str, limit: int = 2):
    contexts, sources = search_knowledge(query, k=limit)
    return {
        "query": query,
        "results": [
            {"content": ctx, "source": src}
            for ctx, src in zip(contexts, sources)
        ]
    }

# ENDPOINT: Info
@app.get("/info")
def info():
    return {
        "project": "WAFAM Sales Chatbot",
        "author": "Kajetan Holdan",
        "university": "Silesian University of Technology",
        "ai_model": "GPT-4o-mini",
        "embeddings": "text-embedding-3-small",
        "vector_db": "ChromaDB",
        "optimization": "Token-optimized v2.4"
    }