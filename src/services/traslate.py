from translate import Translator

class Translate:

    def translador(self,text_to_translate):
        # Crea un objeto Translator
        translator = Translator(to_lang="es")

        # Divide el texto en fragmentos de menos de 500 caracteres
        chunk_size = 500
        translated_text = ""

        for i in range(0, len(text_to_translate), chunk_size):
            chunk = text_to_translate[i:i+chunk_size]
            translated_chunk = translator.translate(chunk)
            translated_text += translated_chunk

        return translated_text
    


