import random 

#Keep track of users and their points - The game bot
class WellBeingBot:
    
    def __init__(self):
        # Dictionary of users to their respective scores.     id : score
        # { userID <string>: points <int> }
        self.users_to_points = {}
        # { userID <string>: name <string> }
        self.user_id_to_real_name = {}

        # Wellness tasks that'll be randomly selected daily.
        self.wellness_tasks = [
          'Go outside and take a walk.', 
          'Read at least 10 pages of a book.',
          'Hang out with a workmate.',
          'Try a new restaurant.',
          'Go for a bike ride.',
          'Share a pic of your favorite hobby.',
          'Switch it up & try a new workspace (i.e. coffee shop, living room, etc.)',
          'Post a funny meme in this channel.',
          'Give someone a compliment.',
          'Message a workmate you haven’t spoken to in a while.',
          'Post a joke in the slack channel.',
          'Eat a healthy snack.',
          'Listen to this song or music playlist.',
          'Call/text someone important in life eg. parents.',
          'Dance break (link for them song or have them reply their favorite song).',
          'Add a serving of fruits or veggies to your lunch.',
          'Setup a game night with your team / workmates.'
        ]
  
    def printOutTasks(self):
      print("These are the current tasks we have: ")
      for task in self.wellness_tasks:
        print(task)
    
    # Functions for commands

    # Add a user to the game
    def add_user(self, user_id, user_real_name):
      self.users_to_points[user_id] = 0
      self.user_id_to_real_name[user_id] = user_real_name

    
    # Adds points to user's score when a photo is uploaded
    def add_points(self, user, points):
      self.users_to_points[user] += points

    # Gets user's current score
    def get_score(self, userId):
        return self.users_to_points[userId]

    # Gets the top 3 users with the highest scores
    def topScores(self):
        #Sort scores
        sorted_values = sorted(self.users_to_points.values()) # Sort the values
        numUsers = len(self.users_to_points)
        counter = 0
        while counter < 3 and counter < numUsers:
          print(sorted_values[counter])
          counter += 1

    def calculate_points(self, messages): #BASED OFF OF A REACTION.GET Response 
        if message["type"] == "message" and message["type"]["timestamp"] > lastTimeCalculated and 
            message["type"]["user"] == BOT ID:

        elif message["type"] == "file" and message["type"]["timestamp"] > lastTimeCalculated and
            message["type"]["user"] == != BOT ID:  


        #if(message["user"] == ) # users who reacted get point for completion
        #else() # user posted a photo completing a task  wellbeing bot: U02FU4B08CX


        #print("Message Content: " + str(message["text"]))
        #print("Time sent: " + str(message["ts"]))


    # Selects a random wellness task and outputs a message to the channel
    def send_wellnesstask(self):
      random_idx = random.randint(0,len(self.wellness_tasks) - 1)
      task = self.wellness_tasks[random_idx]

      # TODO: Add emojis if possible
      message = 'Good Morning!\n\nHere is your daily wellness challenge.\n' + task + '\n\nBe sure to upload an image to receive points. Have a wonderful workday!'
      return message


   




    


