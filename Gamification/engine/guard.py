import Chronicler
import dto

class Guard():

    repo = Chronicler.Chronicler()

    def Authenticate(self, username, password):
        user = self.repo.getUserByUsernameAndPassword(username, password)
        result = dto.authResult
        if user == None:
            result.message = "User not found"
            result.success = False

        else:
            result.message = "Authorized"
            result.success = True

        return result
