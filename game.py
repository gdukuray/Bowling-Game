class Game(object):

    '''The Game is Bowling! One game has TEN frames. In each frame, there are 1 or
        2 rolls. The TENTH frame has 2 or 3 rolls(different from other frames).'''

    def __init__(self):
        self.rolls = [0 for i in range(21)]
        self.currentRoll = 0
        
    def roll(self, pins):
        '''called everytime a player rolls a ball. Input 'pins' is the number of
            pins knocked down.'''
        self.currentRoll += pins

    def score():
        '''Called at the very end of game, and returns the total score for the
            game. This function must iterate through all the frames of the game
            and calculate all their scores.
            The score for a spare or a strike depends on the frame's successor.'''
        return score
        
    
