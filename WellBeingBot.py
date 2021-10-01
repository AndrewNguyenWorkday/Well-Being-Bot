import random 

#Keep track of users and their points - The game bot
class WellBeingBot:
    
    def __init__(self):
        # Dictionary of users to their respective scores.     id : score
        # { userID <string>: points <int> }
        self.users_to_points = {}
        # { userID <string>: name <string> }
        self.user_id_to_real_name = {}
        self.excluded_users = set(["U02FU4B08CX", "USLACKBOT"])
        # Wellness tasks that'll be randomly selected daily.
        self.currentTask = 0
        self.wellness_tasks = [
          'Read at least 10 pages of a book. 📕',
          'Eat a healthy snack. 🍎',
          'Hang out with a workmate. 💙🧡',
          'Go outside and take a walk. 🚶‍♂️🚶‍♀️', 
          'Try a new restaurant. 🍗',
          'Go for a bike ride. 🚲',
          'Share a pic of your favorite hobby. 📸',
          'Switch it up & try a new workspace (i.e. coffee shop, living room, etc.) 🧑‍💻👩‍💻',
          'Post a funny meme in this channel. 😆',
          'Give someone a compliment. 😊',
          'Message a workmate you haven’t spoken to in a while. 🤳',
          'Post a joke in the slack channel. 😂',
          'Eat a healthy snack. 🍎',
          'Listen to this song or music playlist. 🎧',
          'Call/text someone important in life eg. parents. 📞',
          'Dance break! 🕺💃',
          'Add a serving of fruits or veggies to your lunch. 🥕',
          'Setup a game night with your team / workmates. 🎲'
        ]

    def printOutTasks(self):
      print("These are the current tasks we have: ")
      for task in self.wellness_tasks:
        print(task)
    
    # Functions for commands

    # Add a user to the game
    def add_user(self, user_id, user_real_name):
      if user_id not in self.excluded_users:
        self.users_to_points[user_id] = 0
        self.user_id_to_real_name[user_id] = user_real_name

    
    # Adds points to user's score when a photo is uploaded
    def add_points(self, user_id, points):
      if user_id not in self.excluded_users:    
        self.users_to_points[user_id] += points

    # Gets user's current score
    def get_score(self, user_id):
      if user_id not in self.excluded_users:
        return self.users_to_points[user_id]

    # Gets the winners of the game
    # Return Type: Dictionary
    # Example Return: ex: {1 : [("User1", 10), ("User3", 10)], 2 : [("User2", 8)], 3 : []}
    def topScores(self):
        numUsers = len(self.users_to_points)
        winnerDict = {1 : list(), 2 : list(), 3 : list()}

        #Edge case 
        if numUsers == 0:
          return winnerDict
        
        # Sort scores and setup variables
        sorted_users_by_score = sorted(self.users_to_points.items(), key=lambda item: item[1], reverse=True)
        currentPlace = 1
        indexOfDict = 0
        previousScore = sorted_users_by_score[0][1]
        
        # Use sorted list to determine winners
        while currentPlace <= 3 and indexOfDict < numUsers:
          user_id = sorted_users_by_score[indexOfDict][0] 
          user_score = sorted_users_by_score[indexOfDict][1]

          # If next top score matches previous score add to same place on podium 
          if sorted_users_by_score[indexOfDict][1] == previousScore: 
            winnerDict[currentPlace].append( (self.user_id_to_real_name[ user_id ], user_score) ) 
          else: # First winner in next podium spot
            currentPlace += 1
            # No fourth place, exit loop
            if currentPlace > 3:
              break
            winnerDict[currentPlace].append( (self.user_id_to_real_name[ user_id ], user_score) )
          previousScore = user_score
          # traverse list
          indexOfDict += 1
        
        return winnerDict
          

    def resetScores(self):
        for key in users_to_points:
              users_to_points[key] = 0
    
    def send_wellnesstask(self):  
      random_idx = random.randint(0,len(self.wellness_tasks) - 1)
      task = self.wellness_tasks[random_idx]

      # TODO: Add emojis if possible
      message = 'Good Morning! 🌅\n\nHere is your daily wellness challenge:\n' + task + '\n\nBe sure to upload an image to receive extra points. Popular posts earn extra points!\nHave a wonderful workday!'
      return message


   




    


