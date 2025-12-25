import json
import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

# Wczytaj klucz API
env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(env_path)

# Ścieżki
script_dir = os.path.dirname(os.path.abspath(__file__))
chunks_file = os.path.join(script_dir, '..', 'data', 'wafam_chunks.json')
chroma_dir = os.path.join(script_dir, '..', 'knowledge_base')

print("=" * 50)
print("WAFAM Vector Database Builder")
print("=" * 50)

# Krok 1: Wczytaj chunki
print("\n[1/4] Wczytywanie fragmentów...")
with open(chunks_file, 'r', encoding='utf-8') as f:
    chunks = json.load(f)
print(f"Wczytano {len(chunks)} fragmentów")

# Krok 2: Przygotuj teksty i metadane
print("\n[2/4] Przygotowywanie danych...")
texts = []
metadatas = []

for chunk in chunks:
    texts.append(chunk['content'])
    metadatas.append({
        'id': chunk['id'],
        'title': chunk['title'],
        'char_count': chunk['char_count']
    })

print(f"Przygotowano {len(texts)} tekstów z metadanymi")

# Krok 3: Utwórz embeddingi
print("\n[3/4] Tworzenie embeddingów (to może chwilę potrwać)...")
embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small",
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

# Krok 4: Zapisz do ChromaDB
print("\n[4/4] Zapisywanie do bazy wektorowej...")

# Usuń starą bazę jeśli istnieje
if os.path.exists(chroma_dir):
    import shutil
    shutil.rmtree(chroma_dir)

vectorstore = Chroma.from_texts(
    texts=texts,
    embedding=embeddings,
    metadatas=metadatas,
    persist_directory=chroma_dir,
    collection_name="wafam_knowledge"
)

print("\n" + "=" * 50)
print("SUKCES!")
print("=" * 50)
print(f"Baza wektorowa zapisana w: {chroma_dir}")
print(f"Liczba fragmentów: {len(texts)}")
print("\nGotowe! Możesz teraz używać zaawansowanego RAG.")