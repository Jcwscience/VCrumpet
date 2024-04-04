from transformers import pipeline

model_list = {
    "ja": "Helsinki-NLP/opus-tatoeba-en-ja"
}

class Translator:
    def __init__(self):
        self.translation_pipeline = None
        self.model_language = None
        self.model_name = None
        
    def load_model(self, language=None):
        if language in model_list:
            if self.model_language == language and self.translation_pipeline:
                return f'Model already loaded: "{self.model_name}"'
            print(f"Loading model: {model_list[language]}")
            self.translation_pipeline = pipeline("translation", model=model_list[self.target_language], device=0)
            self.model_language = self.target_language
            self.model_name = model_list[self.target_language]
            return "Model loaded."
        else:
            print(f'No model available for language code "{self.target_language}"')

    def clear_model(self):
        self.translation_pipeline = None
        self.model_language = None
        self.model_name = None
        
    def translate(self, text):
        if self.translation_pipeline:
            return self.translation_pipeline(text)[0]['translation_text']
        else:
            return "No translation model loaded."
