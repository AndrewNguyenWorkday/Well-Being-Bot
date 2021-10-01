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
    # there is the dictionary we can use to map back to the names like a tie (Currently it doesn't like it would be 10 10 9 if sorted) #duuplicates yea
    # 
    # 
   
    #IF TIME: get the sorted_values >>> eliminate duplicates >> and find any key with those values for 1,2,3
  
    #would list.index work? 
    # yea that works
    #https://www.geeksforgeeks.org/python-get-key-from-value-in-dictionary/
    #idk if this returns just one index or has potential to return a list of keys that match though
    #iterating through may be easier for the sake of time perhaps 

    # Gets the winners of the game
    # Return Type: Dictionary
    # Example Return: {1 : ["User1", "User3"], 2 : ["User2"], 3 : []}
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
            winnerDict[currentPlace].append( self.user_id_to_real_name[ user_id ] ) 
          else: # First winner in next podium spot
            currentPlace += 1
            winnerDict[currentPlace].append( self.user_id_to_real_name[ user_id ] )
          previousScore = user_score
          # traverse list
          indexOfDict += 1
        
        return winnerDict
          

    def resetScores(self):
        for key in users_to_points:
              users_to_points[key] = 0

    #def announceResults(self):
    #  winners = topScores()
    #  resetScores()
    #  return winners

    def resetScores(self):
      pass
    
    def send_wellnesstask(self):
      random_idx = random.randint(0,len(self.wellness_tasks) - 1)
      task = self.wellness_tasks[random_idx]

      # TODO: Add emojis if possible
      message = 'Good Morning!\n\nHere is your daily wellness challenge.\n' + task + '\n\nBe sure to upload an image to receive points. Have a wonderful workday!'
      return message


   




    


