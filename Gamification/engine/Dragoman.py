import Chronicler

class Dragoman:

    currentLanguageCode = ""
    chron = Chronicler.Chronicler()


    def __init__(self):
        None

    def getValue(self, code):
        value = self.chron.getLanguageValue(code, self.currentLanguageCode)
        return value

    def getValueInSpecificLanguage(self, code, language):
        value = self.chron.getLanguageValue(code, language)
        return value
