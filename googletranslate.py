from googletrans import Translator



class TranslateWithGoogle:
    def __init__(self) -> None:
        pass

    def translate_text(self,text:str)->str:
        translator = Translator()
        output=translator.translate(text,dest='en')
        print(output)
        return output
