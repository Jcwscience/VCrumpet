from transformers import pipeline

translator = pipeline("translation_en_to_ja", model="Helsinki-NLP/opus-tatoeba-en-ja", device=0)

def translate(text):
    print (translator(text))

translate("Hello, how are you?")
