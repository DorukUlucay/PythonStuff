class authResult:

    success = False
    token = ""
    message = ""

    def __init__(self, success, token, message):
        self.success = success
        self.token = token
        self.message = message

class moodReport:

    how = ""
    who = ""
    when = ""
    what = ""

    def __init__(self, who, how, when, what = None):
        self.who = who
        self.how = how
        self.when = when
        self.what = what

class workReport:
    workType = 0
    doneBy = 0
    doneAt = None
    timeSpent = 0
    additionalInfo = None
