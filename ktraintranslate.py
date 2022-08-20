from textblob import TextBlob
import ktrain
from ktrain.text.translation import EnglishTranslator, Translator


class TranslateWithKTrain:
    def __init__(self) -> None:
        pass

    def translate_text_ktrain(self,text:str,src_lang:str)->str:
        translator = EnglishTranslator(src_lang)
        src_text=text
        #print(translator.translate(src_text))
        return translator.translate(src_text)
