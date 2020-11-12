from user import UserSettings
from api_wrapper import APICaller

class App:

	def __init__(self):
		self.settings = UserSettings()

	def processKeywordString (self, string):
		keyWordlist = string.split(",")
		nonOptionalKeywords = []
		optionalKeywords = []
		for keyword in keyWordlist:
			if (keyword[len(keyword)-1] == "+"):
				nonOptionalKeywords.append(keyword[0:len(keyword)-1])
			else:
				optionalKeywords.append(keyword)
		self.settings.optionalKeywords = optionalKeywords
		self.settings.nonOptionalKeywords = nonOptionalKeywords;

	def requestFlair(self):
		print("Would you like add flair? (press enter to search without flair)")
		flair = " "
		while flair not in ["buying","selling","trading", ""]:
			flair = input("[buying/selling/trading]:")
		self.settings.flair = flair 

	def requestKeywords(self):
		keywordString = input("Keywords: ")
		self.processKeywordString(keywordString)

	def displayInstructions(self):
		print("\n***********************************************************************************")
		print("Please enter the keywords for the product you are looking for (seperated by commas).")
		print("If a keyword must be included, append a '+' sign to the end of it.")
		print("\nExamples:\n\n\t Target: any Oblivion set \n\t Keywords: oblivion+ \n\n\t Terget: GMK Oblivion \n\t keywords: gmk+, oblivion+ \n\n\t Terget: Satisfaction75 \n\t keywords: satisfaction, sat75, satisfaction75, sat, 75")
		print("\nAfter you enter the keywords, you will have the option of picking 1 of 3 flairs:")
		print("\n\t-Buying\n\t-Selling\n\t-Trading")
		print("***********************************************************************************")
	
	def inputLoop(self, *args):
		while (True):
			if len(args) == 1:
				answer = input("[y/n]: ")
				if answer.lower() == 'y':
					args[0](True)
					return True
				elif answer.lower() == 'n':
					args[0](False)
					return False
			else:
				answer = input("[y/n]: ")
				if answer.lower() == 'y':
					return True
				elif answer.lower() == 'n':
					return False

	def requestOptionsForSettings(self):
			print("\nWould you like to reply to posts that match your search term?")
			if self.inputLoop(self.settings.setReplyOption) == True:
				print("The default reply is 'PM!'. Would you like to set your own reply")
				if self.inputLoop() == True:	
					self.settings.replyMessage = input("Please enter a reply \n:")
			print("\nWould you like to send a message to the authors of posts that match your search term?")
			if self.inputLoop(self.settings.setSendMsgOption) == True:
				print("The default message is 'Hello, I'm interested in (buying/trading/selling) _____'. Would you like to set your own message?")
				if self.inputLoop() == True:	
					self.settings.message = input("Please enter a message \n:")	

	def requestAPICredentials(self):
		clientID = input("client ID: ")
		clientSecret = input("client secret: ")
		user_agent = input("user agent: ")
		username = input("username: ")
		password = input("password: ")
		self.settings.setAPICredentials(clientID, clientSecret, user_agent, username, password)
	
	def start(self):
		print("\nWelcome to the MechMarket Scanner!")
		if (self.settings.credentialsVerified != True):
			print("Please enter your Reddit API credentials.")
		while (self.settings.credentialsVerified != True):	
			self.requestAPICredentials()
			if APICaller.verifyAPICredentials(self.settings.getCredentialsDict()) == True:
				self.settings.credentialsVerified = True
				self.settings.updateSettingsFile()
		self.requestOptionsForSettings();
		self.displayInstructions();
		self.requestKeywords();
		self.requestFlair();
		caller = APICaller(self.settings)
		caller.start()

if __name__ == "__main__":
	app = App()
	app.start()