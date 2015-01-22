'''
5 parts
-Game state

--Generic/def next_player

/def who_acts_now
   # 

/def list_moves
   # NotImplementedError

/def game_over
   # NotImplementedError

/def winner
   # NotImplementedError
   
/def game_updater()
   # 





--Subtract Square
/self.start_val
   # random.choose(min&max given by client)

/def list_moves

/def game_over


/def winner

/def cur_val

/def game_updater


-Strategy

--Generic


--Specific (One for A1)
/def random_choice
    #For computer. Randomly choose from the available legel moves at the moment




-Game View
--Menu for choosing games
--specifc
--Program must be invoked from game_view.py




-Outsdie of classes. This is should be game-specific
while game_over() == False
    # Keep updating cur_val when game isn't over
    cur_val -= int(client's move)
    
    
    


'''




class GameState():
    ''' A representation of a generic game state ''' 
    def __init__(self, playerA, firstplayer_index):
        ''' Upon init, program needs info about 1) Client's name 2) Which player will go first'''
        self._playerA = playerA
        self._list_players = [playerA, "computer"]
        self._cur_player_index = firstplayer_index # IT'S A BOLLEAN!!
        
    def who_acts_now(self):
        '''(GameState) -> str '''
        return self._list_players[self._cur_player_index]
    def game_updater(self):
        '''(GameState) -> None 
        This method is meant to be invoked when either player makes a move. This method updates general information about the game
        like current player
        '''
        # Players take turn
        self._cur_player_index = not self._cur_player_index
    
    def list_moves(self):
        raise NotImplementedError
    
    def game_over(self):
        raise NotImplementedError
        
        
class SsGameState():
   def __init__(self, start_val):
      self._start_val = random.randint(game_min, game_max)
      
      
      
   def list_moves(self):
      
   def game_over(self):
      
   def game_updater(self):
      
      
        
        
        
        
        
        
    
    
        




#while game_over() == False:
 #   cur_val -= int()
 (game_min, game_max) = tuple(input("Please input the minimum and maximum for game's start value in following format: min, max")       # Ask user for start_val's range then assign them on this line.
