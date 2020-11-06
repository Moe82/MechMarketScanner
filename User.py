import pandas as pd

class UserSettings:

	def __init__ (self):
		self.saveCredentials = False
		self.credentialsVerified = False
		self.readCredentialsFile()
	
	def readCredentialsFile(self):
		try:
			data = pd.read_csv("Settings.csv")
			try:
				data = pd.read_csv("Settings.csv")
				self.credentialsVerified = True if data.iloc[0][1] == 'Yes' else False
				self.__credentialsDict = {
					'clientID': data.iloc[1][1],
					'clientSecret': data.iloc[2][1],
					'userAgent': data.iloc[3][1],
					'username': data.iloc[4][1],
					'password': data.iloc[5][1]
				}
			except:
				print("Error: Settings.csv unreadable. Rebuilding.")
				self.buildSettingsFile()
		except FileNotFoundError:
			self.buildSettingsFile()
	
	def buildSettingsFile(self):
		emptyDict = {
			'save credentials': 'No ANSWER',
			'client ID': 'NO ANSWER', 
			'client secret': 'NO ANSWER', 
			'user agent': 'NO ANSWER', 
			'username': 'NO ANSWER', 
			'password': 'NO ANSWER', 
			}
		pd.DataFrame.from_dict(dict(**emptyDict), orient='index').to_csv('Settings.csv')
		self.readCredentialsFile();

	def updateSettingsFile(self):
		pd.DataFrame.from_dict(dict({'save credentials:': 'Yes'}, **self.__credentialsDict), orient='index').to_csv('Settings.csv')

	def setAPICredentials(self, clientID, clientSecret, user_agent, username, password):
		self.__credentialsDict['clientID'] =  clientID
		self.__credentialsDict['clientSecret'] = clientSecret
		self.__credentialsDict['userAgent'] = user_agent
		self.__credentialsDict['username'] = username
		self.__credentialsDict['password'] = password
		if self.saveCredentials == True:
			self.updateSettingsFile()

	def getCredentialsDict(self):
		return self.__credentialsDict

	def setReplyOption(self, option):
		self.replyToPost = option
		if option == True:
			self.postReplyMessage = "PM!"

	def setSendMsgOption(self, option):
		self.messageAuthor = option
		if option == True:
			self.message= "Hello, I'm interested in purchasing"