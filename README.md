<<<<<<< HEAD
# 🏠 Chatbot do obsługi klienta (Window Sales Bot)
![Status](https://img.shields.io/badge/Status-Tworzę-red)
![Wersja](https://img.shields.io/badge/Version-0.2-blue)

👋 Tutaj wrzucam projekt, nad którym ostatnio pracuję. Jest to chatbot dla branży okiennej, który ma za zadanie wstępnie obsłużyć klienta, zanim ten trafi do handlowca.

### 💡 Skąd ten pomysł?
Chciałbym ułatwić pracę wszystkim handlowcom w branży okienniczej

Napisałem tego bota, żeby:
1.  Klient mógł korzystać z usług **24/7**
2.  Odciążyć pracownika rozmawiającego z klientem
3.  Zautomatyzować umawianie pomiarów

---

### ⚙️ Jak to jest zrobione (Tech Stack)
- **Python 3.12.9**
- **NLTK** - przetwarzanie języka naturalnego
- **scikit-learn** - uczenie maszynowe
- **NumPy** - obliczenia

### 🛠️ Co już działa?
- Konfiguracja środowiska Python 3.12.9
- Struktura projektu (foldery, venv)
- Instalacja bibliotek (NLTK, scikit-learn, NumPy)
- Plik intents.json z 6 kategoriami (powitanie, pożegnanie, ceny okien, ceny drzwi, pomiar, kontakt)
- Wczytywanie danych JSON
- Pętla rozmowy (ciągła konwersacja)
- Obsługa nieznanych pytań
- Ignorowanie wielkości liter
- Losowe odpowiedzi z puli
- Dopasowanie częściowe (rozumie dłuższe zdania)

### 🚧 Co jeszcze chcę dodać? (To-Do)
- **Etap 1** - ~~Podstawy chatbota~~ ✅ UKOŃCZONE
- **Etap 2** - Rozbudowa bazy wiedzy (więcej intencji)
- **Etap 3** - Uczenie maszynowe (klasyfikacja tekstu)
- **Etap 4** - Interfejs webowy
- **Etap 5** - Rozszerzenia

### 🚀 Jak uruchomić?
1. Sklonuj repozytorium
2. Utwórz środowisko wirtualne:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   pip install nltk scikit-learn numpy
   ```
3. Uruchom
   ```bash
   python chatbot.py
   ```

### 📫 Kontakt
Jeśli masz pytania do kodu albo uwagi (każde Code Review mile widziane!), znaleźć mnie można tutaj:

- **LinkedIn**:
- **Autor**: Kajhol (Student Informatyki, Politechnika Śląska, 3 rok)  
*Śledź to repozytorium, żeby zobaczyć postępy!*
=======
# 🏠 Window Sales Chatbot

![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)
![Version](https://img.shields.io/badge/Version-1.5-blue)
![Python](https://img.shields.io/badge/Python-3.12-green)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-orange)

AI-powered chatbot for window/door sales industry. It handles initial customer contact before they reach a salesperson.

## Why this project?

I want to help salespeople in window industry by:
- 24/7 availability for customers
- Reducing workload of sales staff
- Automating measurement appointments
- Providing instant product information
- AI-powered natural conversations

## Tech Stack

- Python 3.12 - Backend programming language
- FastAPI - REST API framework
- Uvicorn - ASGI server
- OpenAI GPT-4o-mini - Artificial intelligence
- HTML/CSS/JavaScript - Frontend interface
- python-dotenv - Environment variables management

## Progress

### Stage 1 - Basic Chatbot (COMPLETED)
- Python environment setup
- Project structure
- intents.json with 6 categories
- Pattern matching logic
- Console version (chatbot.py)

### Stage 2 - REST API (COMPLETED)
- FastAPI integration
- Endpoints: /, /chat, /info, /clear
- Auto documentation at /docs
- CORS enabled for frontend
- Session-based conversation memory

### Stage 3 - Frontend (COMPLETED)
- HTML chat interface
- JavaScript API integration
- Real-time bot responses
- Clickable links support
- New conversation button

### Stage 4 - OpenAI Integration (COMPLETED)
- GPT-4o-mini model connected
- Natural language understanding
- Context-aware responses
- Conversation memory

### Stage 5 - RAG Knowledge Base (COMPLETED)
- Company knowledge base (wafam_oferta.txt)
- Product information (windows, doors, shutters, garage doors)
- Color database for all products
- Pricing inquiry workflow
- Contact information and social media links
- FAQ responses

### Stage 6 - To Do
- Advanced RAG with embeddings
- Deployment to cloud
- Integration with company website

## How to run?

### Step 1: Clone repository
```bash
git clone https://github.com/Kajhol/window-sales-chatbot.git
cd window-sales-chatbot
```

### Step 2: Create virtual environment
```bash
python -m venv venv
```

### Step 3: Activate virtual environment
Windows CMD:
```bash
venv\Scripts\activate
```

### Step 4: Install dependencies
```bash
pip install fastapi uvicorn python-multipart openai python-dotenv
```

### Step 5: Create .env file
Create file .env in window-sales-chatbot folder:
OPENAI_API_KEY=your-api-key-here
Get your API key from: https://platform.openai.com/api-keys

### Step 6: Run API server
```bash
cd window-sales-chatbot/src
uvicorn api:app --reload
```

### Step 7: Open frontend
Open in browser: window-sales-chatbot/frontend/index.html

## 📫 Contact
Questions or code review? Find me here:
- LinkedIn: https://www.linkedin.com/in/kajetan-hołdan-9b4a503a0/
- Author: Kajhol (Computer Science Student, Silesian University of Technology, 3rd year)

---

<<<<<<< HEAD
  *Star this repo to follow progress!*
>>>>>>> 23656e98e4065a1758d1960ee506775a0dbf731f
=======
*Star this repo to follow progress!*
>>>>>>> 548ab444eeffe872cfd304f1be7bd78501448504
