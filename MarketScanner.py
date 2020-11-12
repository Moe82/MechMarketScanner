import praw

class Scanner:
	
	def __init__(self, userSettings, subreddit="mechmarket"):
		subreddit = subreddit
		self.userSettings = userSettings

	def start(self):
		print(self.userSettings.nonOptionalKeywords)
		print(self.userSettings.optionalKeywords)
		print(self.userSettings.flair)

	def searchForKeyword():
		for submission in reddit.subreddit(subreddit).new(limit=25):
			if keyword.lower() in submission.title.lower() and submission.id not in posts_checked:
				posts_checked.append(submission.id)
				#send_email(submission.title, submission.url)
				reply_to_post(submission, "PM")
				PM_author(submission, keyword)
		print("Search complete")

	@staticmethod
	def isConnected(self, credentialsDict):
		self.reddit = praw.Reddit(client_id=credentialsDict['clientID'], client_secret=credentialsDict['clientSecret'], user_agent=credentialsDict['userAgent'], username=credentialsDict['username'], password=credentialsDict['password'])
		try:
			if self.reddit.user.me() == credentialsDict['username']:
				print ("\nAPI credentials have been verified!")
				return True
		except:
			print("\nYour Reddit API credentials are incorrect. Please try again.")
			return False
		