from pymongo import MongoClient
from datetime import datetime
import dto

client = MongoClient('localhost', 27017)

class Chronicler():

	def getUserByUsernameAndPassword(self, usernamex, passwordx):
		db = client.test
		Users = db.Users
		user = Users.find_one({ "username": usernamex, "password": passwordx})
		return user

	def insertMoodReport(self, moodReport):
		db = client.test
		newMoodReport = db.MoodReport
		newMoodReport.insert(
			{
				"who":moodReport.who,
				"what": moodReport.what,
				"when": moodReport.when,
				"how": moodReport.how
			}
		)

	def getLanguageValue(self, code, language):
		db = client.test
		LanguageValues = db.LanguageValues
		value = LanguageValues.find_one({ "code": code, "language": language})
		return value["value"]

	def getWorkTypes(self):
		types = {}
		db = client.test
		workTypesCollection = db.WorkTypes
		value = workTypesCollection.find({ "Parent" : { '$exists' : False } })

		for i in value:
			key = i["Id"]
			name = i["Name"]
			types[key] = name

		return types

	def getWorkSubTypes(self, parentId):
		types = {}
		db = client.test
		workTypesCollection = db.WorkTypes
		value = workTypesCollection.find({ "Parent" : int(parentId) })

		for i in value:
			print(i)
			key = i["Id"]
			name = i["Name"]
			types[key] = name

		print(parentId)
		return types


	def getMoods(self):
		moods = {}
		db = client.test
		moodsColl = db.Moods
		value = moodsColl.find({})

		for i in value:
			key = i["Id"]
			name = i["Name"]
			moods[key] = name

		return moods
