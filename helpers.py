supported_languages = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Italian": "it",
    "Portuguese": "pt",
    "Polish": "pl",
    "Turkish": "tr",
    "Russian": "ru",
    "Dutch": "nl",
    "Czech": "cs",
    "Arabic": "ar",
    "Chinese": "zh",
    "Japanese": "ja",
    "Hungarian": "hu",
    "Korean": "ko"
}

class Language:
    def __init__(self):
        self.supported_languages = supported_languages

    def get_supported_languages_names(self):
        return self.supported_languages.keys()
    
    def get_supported_languages_codes(self):
        return self.supported_languages.items()
    
    def get_language_code(self, language):
        return self.supported_languages[language]
    
    def get_language_name(self, code):
        for language, language_code in self.supported_languages.items():
            if language_code == code:
                return language
        return None
    
    def convert_to_translator_code(self, code):
        translator_code_table = {
            "en": "en-XX",
            "es": "es-XX",
            "fr": "fr-XX",
            "de": "de-DE",
            "it": "it-IT",
            "pt": "pt-XX",
            "pl": "pl-PL",
            "tr": "tr-TR",
            "ru": "ru-RU",
            "nl": "nl-XX",
            "cs": "cs-CZ",
            "ar": "ar-AR",
            "zh": "zh-CN",
            "ja": "ja-XX",
            #"hu": "hu-HU",
            "ko": "ko-KR"
        }
        return translator_code_table[code]