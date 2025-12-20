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
![Status](https://img.shields.io/badge/Status-In%20Progress-red)
![Version](https://img.shields.io/badge/Version-1.3-blue)

👋 A chatbot for window/door sales industry. It handles initial customer contact before they reach a salesperson.

### 💡 Why this project?
I want to help salespeople in window industry by:
1. **24/7** availability for customers
2. Reducing workload of sales staff
3. Automating measurement appointments

---

### ⚙️ Tech Stack
- **Python 3.12.9**
- **NLTK** - natural language processing
- **scikit-learn** - machine learning
- **NumPy** - calculations
- **HTML/CSS/JS** - frontend interface 

### 🛠️ What works?
### Stage 1 - Basic Chatbot (COMPLETED)
- Python environment setup
- intents.json with 6 categories
- Console version (chatbot.py)

### Stage 2 - REST API (COMPLETED)
- FastAPI integration
- JSON request/response format
- CORS enabled for frontend

### Stage 3 - Frontend (COMPLETED)
- HTML chat interface
- JavaScript API integration
- Real-time bot responses

### 🚧 To-Do
- **Stage 4** - OpenAI API integration
- **Stage 5** - RAG (knowledge base)
- **Stage 5** - Extensions (company data, deployment to cloud)

### 🚀 How to run?
1. Clone repository
   ```bash
   git clone https://github.com/Kajhol/chatbot-okna.git
   cd chatbot-okna
   ```
3. Create and activate virtual environment:
   ```bash
   python -m venv venv
   ```
   For windows:
   ```bash
   venv\Scripts\activate.bat
   ```
4. Install dependencies
   ```bash
   pip install fastapi uvicorn python-multipart nltk scikit-learn numpy
   ```
5. Run API server
   ```bash
   cd chatbot-okna/src
   uvicorn api:app --reload
   ```
6. Open in browser index.html:  
   chatbot-okna/chatbot-okna/frontend/index.html

### 📫 Contact
Questions or code review? Find me here:

- LinkedIn: https://www.linkedin.com/in/kajetan-hołdan-9b4a503a0/
- Author: Kajhol (Computer Science Student, Silesian University of Technology, 3rd year)
  
---

  *Star this repo to follow progress!*
>>>>>>> 23656e98e4065a1758d1960ee506775a0dbf731f
