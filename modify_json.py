import json

with open ("german.json","r",encoding="utf-8") as f:
    data = json.load(f)

fields_to_keep = ["word","cefr_level","english_translation","example_sentence_native",
                  "example_sentence_english","gender","pos"]

cleaned_data = [
    {field: item.get(field) for field in fields_to_keep}
    for item in data
]

with open("cleaned_german_words.json","w",encoding="utf-8")as f:
    json.dump(cleaned_data,f,ensure_ascii=False,indent=2)