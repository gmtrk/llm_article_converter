# Article to HTML Converter

This project is a Python application that converts plain text articles into structured HTML format using OpenAI's GPT-4 model. It's designed to automatically identify potential places for images and create appropriate HTML placeholders with descriptive alt text.

## Features

- Converts plain text articles to structured HTML
- Automatically identifies and suggests image placements
- Generates descriptive alt text for images based on context
- Adds appropriate HTML tags for titles, paragraphs, and sections
- Supports UTF-8 encoding for proper handling of special characters

## Prerequisites

- Python 3.6 or higher
- OpenAI API key

## Installation

1. Clone this repository:
```bash
git clone https://github.com/gmtrk/llm_article_converter
cd llm_article_converter
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root directory and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage

1. Place your article text in a file named `artykul.txt` in the project root directory.

2. Run the converter:
```bash
python converter.py
```

3. The converted HTML will be saved to `artykul.html` in the same directory.

## How It Works

1. The script reads the content from `artykul.txt`
2. It sends the content to OpenAI's GPT-4 model with specific formatting instructions
3. The model processes the text and returns structured HTML with:
   - Proper HTML tags for content structure
   - Image placeholders with descriptive alt text
   - Captions for images
4. The resulting HTML is saved to `artykul.html`

## Notes

- The script uses GPT-4 model with temperature set to 0 for consistent output
- Image placeholders use "image_placeholder.jpg" as the source
- The generated HTML excludes `<html>`, `<head>`, and `<body>` tags
- No CSS or JavaScript is included in the output

---

# Konwerter Artykułów do HTML

Ten projekt to aplikacja w Pythonie, która konwertuje artykuły tekstowe na ustrukturyzowany format HTML przy użyciu modelu GPT-4 od OpenAI. Jest zaprojektowana do automatycznego identyfikowania potencjalnych miejsc na obrazy i tworzenia odpowiednich znaczników HTML z opisowymi tekstami alternatywnymi.

## Funkcje

- Konwertuje artykuły tekstowe na ustrukturyzowany HTML
- Automatycznie identyfikuje i sugeruje miejsca na obrazy
- Generuje opisowe teksty alternatywne dla obrazów na podstawie kontekstu
- Dodaje odpowiednie znaczniki HTML dla tytułów, paragrafów i sekcji
- Obsługuje kodowanie UTF-8 dla prawidłowej obsługi znaków specjalnych

## Wymagania

- Python 3.6 lub nowszy
- Klucz API OpenAI

## Instalacja

1. Sklonuj repozytorium:
```bash
git clone <url-repozytorium>
cd article-converter
```

2. Zainstaluj wymagane pakiety:
```bash
pip install -r requirements.txt
```

3. Utwórz plik `.env` w głównym katalogu projektu i dodaj swój klucz API OpenAI:
```
OPENAI_API_KEY=twoj_klucz_api
```

## Użytkowanie

1. Umieść tekst artykułu w pliku o nazwie `artykul.txt` w głównym katalogu projektu.

2. Uruchom konwerter:
```bash
python converter.py
```

3. Przekonwertowany HTML zostanie zapisany do pliku `artykul.html` w tym samym katalogu.

## Jak To Działa

1. Skrypt odczytuje zawartość z `artykul.txt`
2. Wysyła zawartość do modelu GPT-4 OpenAI ze szczegółowymi instrukcjami formatowania
3. Model przetwarza tekst i zwraca ustrukturyzowany HTML z:
   - Odpowiednimi znacznikami HTML dla struktury treści
   - Zaślepkami obrazów z opisowymi tekstami alternatywnymi
   - Podpisami dla obrazów
4. Wynikowy HTML jest zapisywany do `artykul.html`

## Uwagi

- Skrypt używa modelu GPT-4 z parametrem temperature ustawionym na 0 dla spójnych wyników
- Zaślepki obrazów używają "image_placeholder.jpg" jako źródła
- Wygenerowany HTML nie zawiera znaczników `<html>`, `<head>` i `<body>`
- W wyniku nie jest zawarte CSS ani JavaScript
