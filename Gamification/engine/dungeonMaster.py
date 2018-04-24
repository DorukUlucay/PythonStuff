import dto
import Chronicler
import Dragoman
import static

repo = Chronicler.Chronicler()
dragoman = Dragoman.Dragoman()

class DungeonMaster:

    message_welcome = ""

    def __init__(self):
        self.message_welcome = dragoman.getValueInSpecificLanguage("welcomeMessage", "tr")

    def getWorkTypes(self):
        return repo.getWorkTypes()

    def getWorkSubTypes(self, parentId):
        return repo.getWorkSubTypes(parentId)

    def getMoods(self):
        return repo.getMoods()

    def greet(self):
        return self.message_welcome

    def reportMood(self, moodReport):
        repo.insertMoodReport(moodReport)
        return True
