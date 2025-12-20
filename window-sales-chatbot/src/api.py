from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load API key from .env file
env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(env_path)

# Create OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Create FastAPI application
app = FastAPI(
    title="WAFAM Chatbot API",
    description="AI Chatbot for WAFAM - window and door manufacturer",
    version="0.6"
)

# Add CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load WAFAM knowledge base
script_directory = os.path.dirname(os.path.abspath(__file__))
knowledge_path = os.path.join(script_directory, '..', 'data', 'wafam_oferta.txt')

with open(knowledge_path, "r", encoding="utf-8") as file:
    WAFAM_KNOWLEDGE = file.read()

# System prompt with knowledge base
SYSTEM_PROMPT = f"""Jesteś asystentem firmy WAFAM - producenta okien, drzwi i rolet zewnętrznych.

BAZA WIEDZY WAFAM:
{WAFAM_KNOWLEDGE}

ZASADY ODPOWIEDZI:
1. Odpowiadaj TYLKO na podstawie powyższej bazy wiedzy.
2. Jeśli czegoś nie ma w bazie, powiedz: "To świetne pytanie! Nasi handlowcy chętnie Ci to wyjaśnią."
3. Odpowiadaj po polsku, krótko i konkretnie.
4. Nie wymyślaj cen. Przy wycenie zbierz dane i zaproponuj kontakt.
5. Zadawaj max 3 pytania naraz.
6. Kończ odpowiedź kolejnym krokiem.
7. WAŻNE: Pamiętaj o całej rozmowie. Nie pytaj ponownie o rzeczy, które klient już podał.
8. Jeśli klient podał już produkt, miejscowość lub kontakt - wykorzystaj te informacje.
"""

# Store conversation history (simple in-memory storage)
conversations = {}

# Data models
class Message(BaseModel):
    text: str
    session_id: str = "default"

class Answer(BaseModel):
    bot: str

# Chat with OpenAI using conversation history
def ask_wafam_bot(user_message: str, session_id: str) -> str:
    # Get or create conversation history
    if session_id not in conversations:
        conversations[session_id] = []
    
    history = conversations[session_id]
    
    # Add user message to history
    history.append({"role": "user", "content": user_message})
    
    # Keep only last 10 messages to avoid token limit
    if len(history) > 10:
        history = history[-10:]
        conversations[session_id] = history
    
    # Build messages for API
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    messages.extend(history)
    
    # Get response from OpenAI
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        max_tokens=500,
        temperature=0.3
    )
    
    bot_response = response.choices[0].message.content
    
    # Add bot response to history
    history.append({"role": "assistant", "content": bot_response})
    conversations[session_id] = history
    
    return bot_response

# ENDPOINT 1: Home page
@app.get("/")
def home():
    return {
        "status": "online",
        "message": "WAFAM Chatbot API with Memory",
        "version": "0.6",
        "company": "WAFAM - producent okien i rolet"
    }

# ENDPOINT 2: Chat with bot
@app.post("/chat", response_model=Answer)
def chat(message: Message):
    response = ask_wafam_bot(message.text, message.session_id)
    return {"bot": response}

# ENDPOINT 3: Clear conversation
@app.post("/clear")
def clear_conversation(session_id: str = "default"):
    if session_id in conversations:
        del conversations[session_id]
    return {"status": "Conversation cleared", "session_id": session_id}

# ENDPOINT 4: Information
@app.get("/info")
def info():
    return {
        "project": "WAFAM Sales Chatbot",
        "author": "Kajetan Holdan",
        "university": "Silesian University of Technology",
        "ai_model": "GPT-4o-mini",
        "features": ["RAG", "Conversation Memory"]
    }
    