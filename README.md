# 🇩🇪 German Dictionary

A simple German-English dictionary web application built with Python and Streamlit.

## Features

* 🔍 Instant German word search
* 🇬🇧 English translations
* 📚 CEFR language levels (A1, A2, B1, etc.)
* 📝 Part of speech information
* 🇩🇪 German example sentences
* 🌍 English translations of example sentences
* 🎨 Clean and user-friendly interface

## Technologies Used

* Python
* Streamlit
* JSON

## Installation

### Clone the repository

```bash
git clone https://github.com/saitarunaditya/German-Thesaurus.git
cd German-Thesaurus
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
streamlit run main.py
```

## Dataset Structure

Each dictionary entry contains:

```json
{
  "word": "sein",
  "cefr_level": "A1",
  "english_translation": "to be",
  "example_sentence_native": "Er will Arzt sein.",
  "example_sentence_english": "He wants to be a doctor.",
  "gender": "",
  "pos": "verb"
}
```

## Screenshot

<img width="1007" height="800" alt="image" src="https://github.com/user-attachments/assets/6568a373-479e-41f3-ac02-ec966f353b89" />


## Future Improvements

* ⭐ Favorite words
* 🎲 Random word generator
* 🃏 Flashcard mode
* 🎯 Quiz mode
* 🔊 Pronunciation support
* 📈 Learning statistics

## Author

**Sai Tharun Aditya, Kesana**
