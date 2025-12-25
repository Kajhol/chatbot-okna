import json
import os

# Ścieżki do plików
script_dir = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(script_dir, '..', 'data', 'wafam_oferta.txt')
output_file = os.path.join(script_dir, '..', 'data', 'wafam_chunks.json')

# Definicja sekcji do wyodrębnienia
SECTIONS = [
    {"id": "firma", "title": "O firmie", "keywords": ["o firmie", "wafam działa", "20 lat"]},
    {"id": "handlowcy", "title": "Zespół handlowców", "keywords": ["handlowcy", "zadzwoń"]},
    {"id": "okna_standard", "title": "Okna standardowe", "keywords": ["okna standardowe", "decco 82", "ideal 7000"]},
    {"id": "okna_premium", "title": "Okna premium", "keywords": ["okna premium", "salamander", "decco 83"]},
    {"id": "systemy_przesuwne", "title": "Systemy przesuwne", "keywords": ["psk", "smart-slide", "hst"]},
    {"id": "system_tarasowy", "title": "System tarasowy", "keywords": ["system tarasowy", "słupek ruchomy", "niski próg"]},
    {"id": "drzwi", "title": "Drzwi", "keywords": ["drzwi pełne", "drzwi przeszklone"]},
    {"id": "rolety", "title": "Rolety zewnętrzne", "keywords": ["rolety podtynkowe", "rolety nadstawne", "moskitier"]},
    {"id": "zaluzje", "title": "Żaluzje fasadowe", "keywords": ["żaluzje fasadowe", "regulacja światła"]},
    {"id": "bramy", "title": "Bramy garażowe", "keywords": ["bramy garażowe", "gwarancja producenta"]},
    {"id": "dodatki_okienne", "title": "Dodatki okienne", "keywords": ["swisspacer", "hoppe secustik"]},
    {"id": "montaz", "title": "Montaż", "keywords": ["montaż", "ekipa montażowa", "ciepły montaż"]},
    {"id": "doradztwo", "title": "Doradztwo", "keywords": ["doradztwo", "czyste powietrze"]},
    {"id": "wycena", "title": "Wycena i oferta", "keywords": ["wycena", "oferta w 24h"]},
    {"id": "kontakt", "title": "Dane kontaktowe", "keywords": ["kontakt", "telefon", "e-mail", "godziny otwarcia"]},
    {"id": "social_media", "title": "Social media i opinie", "keywords": ["facebook", "google maps", "opinie"]},
    {"id": "kolory_rolety", "title": "Kolory rolet", "keywords": ["kolory", "rolety", "srebrny", "biały"]},
    {"id": "kolory_drzwi", "title": "Kolory drzwi", "keywords": ["kolory", "drzwi", "antracyt"]},
    {"id": "kolory_bramy", "title": "Kolory bram", "keywords": ["kolory", "bramy", "winchester"]},
    {"id": "kolory_okna", "title": "Kolory okien", "keywords": ["folia dekoracyjna", "kolory", "okna"]},
    {"id": "parametry", "title": "Parametry techniczne", "keywords": ["parametry techniczne", "uw", "komór"]},
]

def load_document():
    with open(input_file, 'r', encoding='utf-8') as f:
        return f.read()

def split_into_chunks(text):
    chunks = []
    lines = text.split('\n')
    
    current_chunk = []
    current_section = None
    
    for line in lines:
        line_lower = line.lower().strip()
        
        # Sprawdź czy to nowa sekcja
        new_section = None
        for section in SECTIONS:
            if any(keyword in line_lower for keyword in section["keywords"]):
                if len(line.strip()) < 100:  # To prawdopodobnie nagłówek
                    new_section = section
                    break
        
        if new_section and current_chunk:
            # Zapisz poprzedni chunk
            chunk_text = '\n'.join(current_chunk).strip()
            if chunk_text and len(chunk_text) > 50:
                chunks.append({
                    "id": current_section["id"] if current_section else "intro",
                    "title": current_section["title"] if current_section else "Wprowadzenie",
                    "content": chunk_text,
                    "char_count": len(chunk_text)
                })
            current_chunk = []
            current_section = new_section
        
        current_chunk.append(line)
    
    # Zapisz ostatni chunk
    if current_chunk:
        chunk_text = '\n'.join(current_chunk).strip()
        if chunk_text and len(chunk_text) > 50:
            chunks.append({
                "id": current_section["id"] if current_section else "outro",
                "title": current_section["title"] if current_section else "Inne",
                "content": chunk_text,
                "char_count": len(chunk_text)
            })
    
    return chunks

def main():
    print("=" * 50)
    print("WAFAM Knowledge Base Preparation")
    print("=" * 50)
    
    # Wczytaj dokument
    print("\n[1/3] Wczytywanie dokumentu...")
    text = load_document()
    print(f"Wczytano {len(text)} znaków")
    
    # Podziel na chunki
    print("\n[2/3] Dzielenie na fragmenty...")
    chunks = split_into_chunks(text)
    print(f"Utworzono {len(chunks)} fragmentów")
    
    # Zapisz do JSON
    print("\n[3/3] Zapisywanie do pliku...")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(chunks, f, ensure_ascii=False, indent=2)
    print(f"Zapisano do: {output_file}")
    
    # Pokaż podsumowanie
    print("\n" + "=" * 50)
    print("Podsumowanie fragmentów:")
    print("=" * 50)
    for i, chunk in enumerate(chunks):
        print(f"{i+1}. {chunk['title']} ({chunk['char_count']} znaków)")
    
    print("\nGotowe!")

if __name__ == "__main__":
    main()