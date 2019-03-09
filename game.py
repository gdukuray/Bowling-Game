class Game(object):

    '''The Game is Bowling! One game has TEN frames. In each frame, there are 1 or
        2 rolls. The TENTH frame has 2 or 3 rolls(different from other frames).'''

    def __init__(self):
        self.rolls = [0 for i in range(21)]
        self.currentRoll = 0

        
    def roll(self, pins):
        '''called everytime a player rolls a ball. Input 'pins' is the number of
            pins knocked down.'''
        self.currentRoll += 1
        self.rolls[self.currentRoll] = pins


    def score(self):
        '''Called at the very end of game, and returns the total score for the
            game. This function must iterate through all the frames of the game
            and calculate all their scores.
            The score for a spare or a strike depends on the frame's successor.'''
        score = 0
        frameIndex = 0
        for frame in 10:
            if (self.isStrike(frameIndex)):
                score += 10 + self.strikeBonus(frameIndex);
                frameIndex+=1
            elif (self.isSpare(frameIndex)):
                score += 10 + self.spareBonus(frameIndex)
                frameIndex += 2
        else:
            score += self.sumOfBallsInFrame(frameIndex)
            frameIndex += 2

        return score
        

    def isStrike(self, frameIndex):
        return self.rolls[frameIndex] == 10

    def sumOfBallsInFrame(self, frameIndex):
        return self.rolls[frameIndex] + self.rolls[frameIndex+1]

    def spareBonus(self, frameIndex):
        return self.rolls[frameIndex+2]

    def strikeBonus(self, frameIndex):
        return self.rolls[frameIndex+1] + self.rolls[frameIndex+2]

    def isSpare(self, frameIndex):
        return self.rolls[frameIndex] + self.rolls[frameIndex+1] == 10


