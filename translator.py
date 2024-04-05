from transformers import MBartForConditionalGeneration, MBart50TokenizerFast
from xtts_live.xtts_live import Helpers
import langid


lcc = Helpers().language_code_conversion
class Translator:
    def __init__(self):
        langid.set_languages(Helpers().supported_languages)
        model = MBartForConditionalGeneration.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")
        self.tokenizer = MBart50TokenizerFast.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")
        self.model = model.cuda()

    def translate(self, text, target_lang, source_lang=None):
        if not source_lang:
            source_lang = langid.classify(text)[0]
        
        self.tokenizer.src_lang = lcc[source_lang]
        encoded_text = self.tokenizer(text, return_tensors="pt").to("cuda")
        generated_tokens = self.model.generate(
            **encoded_text,
            forced_bos_token_id=self.tokenizer.lang_code_to_id[lcc[target_lang]]
        )
        output_text = self.tokenizer.batch_decode(generated_tokens.cpu(), skip_special_tokens=True)[0]
        return output_text

def main():
    translator = Translator()
    while True:
        text = input("Enter text to translate: ")
        target_lang = input("Enter target language: ")
        print(translator.translate(text, target_lang))

if __name__ == "__main__":
    main()