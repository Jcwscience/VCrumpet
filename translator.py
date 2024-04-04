from transformers import pipeline

model_list = {
    "ja": "Helsinki-NLP/opus-tatoeba-en-ja"
}

class Translator:
    def __init__(self):
        self.translator = None
        self.target_language = None
        self.model_language = None
        self.model_name = None
        

    def load_model(self):
        if self.target_language:
            self.translator = pipeline("translation", model=model_list[self.target_language], device=0)
            self.model_language = self.target_language
            self.model_name = model_list[self.target_language]
        else:
            self.translator = None
            self.model_language = None
            self.model_name = None

    def translate(self, text):
        if self.target_language != self.model_language:
            self.load_model()
        if self.target_language:
            return self.translator(text)[0]['translation_text']
        else:
            return text
