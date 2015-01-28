import math
import random
class GameState():
    ''' 
    A representation of a generic game state 
    ''' 
    def __init__(self, playerA, firstplayer_index):
        ''' Upon init, program needs info about 
        1) Which game they want to play
        2) Which player will go first
        3) The computer's strategy for the game
        '''
        
        self.playerA = playerA
        self.list_players = ("Computer", playerA)
        self.cur_player_index = firstplayer_index # IT'S A BOOLEAN!!

    def who_acts_now(self):
        '''(GameState) -> str 
        Determines whose move it is.
        >>> self.list_players = (playerA, "Computer")
        >>> firstplayer_index = 0
        >>> self.cur_player_index = firstplayer_index
        >>> who_acts_now()
        playerA
        
        '''
        return self.list_players[self.cur_player_index]

    def game_updater(self):
        '''(GameState) -> None 
        This method is meant to be invoked when either player makes a move. 
        This method updates general information about the game
        like current player
        '''
        # Players take turn
        self.cur_player_index = not self.cur_player_index
    
    def list_moves(self):
        raise NotImplementedError
    
    def game_over(self):
        raise NotImplementedError
    
    def __str__(self):
        pass
    def __repr__(self):
        pass
    def __eq__(self):
        pass
        
        

class SsGameState(GameState):
    """
    A subclass of GameState specific to the game Subtract Square
    """
    def __init__(self, playerA, firstplayer_index):
        
        self.start_val = random.randint(int(start_val_range[0]), int(start_val_range[1]))  #unassigned var
        GameState.__init__(self, playerA, firstplayer_index)


    def list_moves(self):
        """SsGameState(GameState) -> str
        Presents list of legal moves in the game as a string
        >>> start_val = 20
        >>> list_moves()
        'Choice 1: 1\nChoice 2: 4\nChoice 3: 9\nChoice 4: 16\n'
        """
        counter = 1
        list_moves_str = "" 
        for number in range(1,self.start_val):
            if math.sqrt(number) % 1 == 0.0:
                list_moves_str += "Choice " + (str(counter) + ": " + str(number) + "\n")
                counter += 1
        return list_moves_str    
    
       
    def game_over(self):
        """
        SsGameState(GameState) -> Boolean
        
        Determines if the game is over by checking if the current number
        is equal to zero
        """
        
        if self.start_val == 0:
            return True
        else: 
            return False
       
    def ssgame_updater(self, client_move):
        """
        SsGameState(GameState) -> NoneType
        Updates game state by checking if game is over. If not, it is the
        next players turn
        """
        
        if self.game_over() == True:
            return None
        else:
            self.start_val -= client_move  #unassigned var
            
            
    def __str__(self):
        pass
    
    def __repr__(self):
        pass
    
    def __eq__(self):
        pass
            
class Strategy():
    def __init__(self):
        pass
    
    def __str__ (self):
        pass
    
    def __repr__(self):
        pass
    
    def __eq__(self):
        pass
            
        
class RandomMove(Strategy):
    ''' 
    Subclass of Strategy specific to Subtract Square game.
    Choose a random number from list of legal moves, returns that integer value
    '''
       # Parse for int val from a given list of moves 
    def __init__(self, list_moves):
        self.list_moves = list_moves()
        self.list_moves = self.listmoves.split('\n')  #['Choice 1: 1', 'Choice 2: 4']
    def random_choice(self):
        ''' 
        (list) - > str
        Computer randomly picks one of the legal moves in list_moves
        >>>random_choice(['Choice 1: 1', 'Choice 4: 4'])
        'Choice 1: 1'
        '''
        self.choice = random.choice(self.list_moves)  # 'Choice 1: 1'
        while choice == '':                  # To avoid cases where the list contains '' "
            self.choice = random.choice(self.list_moves)
         
         
    def ssparse_int_from_move(self):
        ''' 
        (str) -> list of str
        Take string version of choice (e.g. 'Choice 1: 1') and split string
        into list of Choice number and value.
        >>>ssparse_int_from_move('Choice 1: 1')
        ['Choice 1', '1']
        '''
        # Codes below are specific to SubtractSquare
        choice_break_down = self.choice.split(': ')  # ['Choice 1', '1']
        return int(choice_break_down[-1])    # index is hardcoded, hence position must be in form like above
    
    def ai_pick_move(self):
        random_choice()
        ssparse_int_from_move()
        
    def __str__(self):
        pass
    
    def __repr__(self):
        pass
    
    def __eq__(self):
        pass



# Aimming to resue this UI as much as possible

#Pre-game UI
class GameView():
    
    def __init__(self):
        self.dict_games = {1:'Subtract Square'}  # Will add more on a2 & a3
        self.strategies_dict = {1: 'Random_move'}
        self.yorn_dict = {'Y': True, 'N': False}
        
    def general_welcome(self):
        print("**********Weclome to the Game.**********")
        
    def pick_game(self):
        '''(GameView, str) -> int'''
        print('\t\t'.join(['Options', 'Games']))
        # Print number of game and name of game on the same line.
        for choice_num in self.dict_games:
            print('\t\t'.join((str(choice_num), self.dict_games[choice_num])))                      
        self.user_game = int(input("Please enter the number for the game you'd like to play: "))
        while not (int(self.user_game) in self.dict_games):
            print("You've chosen a game that is not on the list")
            self.user_game = int(input("Please enter the number for the game you'd like to play: "))
        return int(self.user_game)
    
    def pick_strategy(self):
        '''(GameView, str) -> int'''
        print('\t\t'.join(['Options', 'Difficulties']))
        for choice_num in self.strategies_dict:
                    print('\t\t'.join((str(choice_num), self.strategies_dict[choice_num]))) 
        self.user_strategy = int(input("There are various levels of difficulty for this game. Please enter the number for the difficulty you'd like to play: "))
        while not (int(self.user_strategy) in self.strategies_dict):
            print("You've chosen a difficulty level that is not on the list")
            self.user_strategy = int(input("There are various levels of difficulty for this game. Please enter the number for the difficulty you'd like to play: "))

        return int(self.user_strategy)
    
    def pick_who_first(self):
        '''(GameView, Boolean) -> Boolean'''
        self.user_who_first = input("\nWould you like to act first? (Y/N):")
        while not (self.user_who_first in self.yorn_dict):
            print("You've chosen an option that is not on the list")
            self.user_who_first = input("\nWould you like to act first? (Y/N):")
        return self.yorn_dict[self.user_who_first]
    def get_name(self):
        self.user_name = input("Please enter your name: ")
        return self.user_name
    def start_val_range(self):
        '''(GameView, Tuple) -> Tuple of str'''
        self.user_choice_min = input("Please enter a whole number for the minimum for the start value: ")
        while not (self.user_choice_min.isnumeric):
            print("You've entered an invalid  entry")
            self.user_choice_min = input("Please enter a whole number for the minimum for the start value: ")

        self.user_choice_max = input(("Please enter the maximum for the start value: "))
        while not (self.user_choice_max.isnumeric):
            print("You've entered an invalid  entry")
            self.user_choice_min = input("Please enter a whole number for the maximum for the start value: ")
        return (self.user_choice_min, (self.user_choice_max))
    
    
            
            




def game_help():
    if gameview.user_game == 1:
        subtract_square_help()
        
def subtract_square_help():
    print('\n**********Welcome to Subtract Square!**********\n')
    print('In this game you and the computer will take turns choosing positive square numbers. The chosen numbers will be subtracted from the starting value. In addition, you may decide what the starting value is and who picks the first number\n')
    print("Game's Rules:")
    print('1. You must choose a square number smaller than the current number.')
    print('2. Play continues until there are no more legal moves available. The player about to make a move at that point loses.\n\n')
    print('You may enter game_help() anytime during the game to see these rules again')
    
def display_info():
    ''' Can't be used until subtact square has started'''
    #try:
    print('It is now your turn to pick a number')
    print("The current value is " + str(ssgamestate.start_val))
    print('Your available options are as follow:')
    print(ssgamestate.list_moves())
    #except NameError:
        #print('Game is not set up yet')


if (__name__ == "__main__"):
    gameview = GameView()
    gameview.general_welcome()
    user_name = gameview.get_name()
    
    if gameview.pick_game() == 1:
        # Gathering pre-game info
        subtract_square_help()
        user_strategy = gameview.pick_strategy()
        user_who_first = gameview.pick_who_first()
        start_val_range = gameview.start_val_range()
        ssgamestate = SsGameState(user_name, gameview.user_who_first)
        # Player alternating turns till game is over
    
        while not ssgamestate.game_over():
            if ssgamestate.list_players[user_who_first] == user_name:
                display_info()
                client_choice_int = int(input("Please choose a value from the available choices:"))  # Limit it to the legal moves
                ssgamestate.ssgame_updater(client_choice_int)
            elif user_strategy  == 1 and ssgamestate.list_players[user_who_first] == "Computer":
                RandomMove(ssgamestate.list_moves()).ai_pick_move()
        
                
        
        
        
        
        
        
        
        
        
        
        
        
    
    
    
    ## Pick a game (General)
    #user_name = input('Please enter your name: ')
    #print(user_name + ". Here are the games to choose from: (Please choose by numbers given)\n" )
    #print('\t\t'.join(['Options', 'Games']))
    #print(('\t\t'.join(['1', 'Subtract Square']) + '\n'))
    #user_choice_game = input("Please enter the number for the game you'd like to play (eg. 1):  ")
    #while user_choice_game != '1':
        #print("You've chosen a game that is not on the list")
        #user_choice_game = input("Please enter the number for the game you'd like to play: ")
    ## The mechanism for choosing other games from list_games will be implemented here later
    
    ## Program goes into ss directly. If there were other games, selection mechanism has to be deployed
    ##Game_specific intro
    ## SS intro (specific)
    #print('\n**********Welcome to Subtract Square!**********\n')
    #print('In this game you and the computer will take turns choosing positive square numbers. The chosen numbers will be subtracted from the starting value. In addition, you may decide what the starting value is and who picks the first number\n')
    #print("Game's Rules:")
    #print('1. You must choose a square number smaller than the current number.')
    #print('2. Play continues until there are no more legal moves available. The player about to make a move at that point loses.\n\n')
    
    ## Pick a level of difficulty
    #print('\t\t'.join(['Options', 'Difficulties']))
    #print('1. Easy: Randomly choosing available moves\n')
    #strategies_dict = {1: 'Random_move'}
    #user_stra4comp = input("There are various level of difficulties for this game. Please pick the difficulty for the game, (eg. 1): ")
    #while user_stra4comp != '1':
        #print("You've chosen a difficulty level that is not on the list")
        #user_stra4comp = input("There are various level of difficulties for this game. Please pick the difficulty for the game, (eg. 1): ")
        
    ## who goes first
    #user_who_1st = input("\nWould you like to pick first? (Y/N):")
    #input_boolean_dict = {'Y': True, 'N': False}
    #while not (user_who_1st in input_boolean_dict):
        #print("You've chosen an option that is not on the list")
        #user_who_1st = input("\nWould you like to pick first? (Y/N):")
    
    ## Get starting-val's range (specific)
    #print("Before the game starts, you need to choose the maximum and minimum for the starting value.")
    #min_max = input("Please enter the minimum for the starting value: (eg. min)")
    #max_max = input("Please enter the maximum for the starting value: (eg. max)")
    #game_min = int(min_max)
    #game_max = int(max_max)
    
    
    
    
    
    
    
    ##Actaul game process 
    
    #print('The starting value is ' + str(ssgamestate.start_val))
    #counter = 0
    #while not ssgamestate.game_over():
        #counter += 1
        #if counter > 0:
            #print('The current value is ')
        ## for client
        #if ssgamestate.cur_player_index == 0:
            #print('You are available options are as follow:')
            #print(ssgamestate.list_moves())
            #client_choice_int = int(input("Please choose a value from the available choices, (eg. 9): "))
            #ssgamestate.ssgame_updater(client_choice_int)
    
        

    
    
    

    
    
    
    
    
    
    
