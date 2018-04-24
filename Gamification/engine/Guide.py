import guard
import dungeonMaster
import dto

class Guide():

    def __init__(self):
        None

    g = guard.Guard()
    dm = dungeonMaster.DungeonMaster()
    username = ""
    token = ""
    authorized = False


    def getWorkTypes(self):
        return self.dm.getWorkTypes()

    def getWorkSubTypes(self, parentId):
        return self.dm.getWorkSubTypes(parentId)

    def auth(self):
        print("What is your name ?")
        name = raw_input()
        print("What is your password ?")
        password = raw_input()
        result = self.g.Authenticate(name, password)
        if result.success:
            self.username = name
            self.authorized = True
        return result

    def getMoodTypes(self):
        moods = self.dm.getMoods()
        return moods

    def getWelcomeMessage(self):
        message = self.dm.greet()
        return message

    def reportMood(self, moodReport):
        return self.dm.reportMood(moodReport)
