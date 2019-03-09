from game import *
import unittest


class TestBowlingGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.testGutterGame()
        self.testAllOnes()
        self.testOneSpare()
        self.testOneStrike()
        self.testPerfectGame()

    def rollMany(self, n, pins):
        for i in range(n):
            self.game.roll(pins)

    def testGutterGame(self):
        self.rollMany(20, 0)
        if (self.score() == 0):
            return True
        else:
            return False
        
            
    def testAllOnes(self):
        self.rollMany(20, 1)
        if self.score == 20:
            return True
        else:
            return False

    def rollSpare(self):
        self.game.roll(5)
        self.game.roll(5)

    def rollStrike(self):
        self.roll(10)

    def testOneSpare(self):
        self.rollSpare()
        self.roll(3)
        self.rollMany(17, 0)
        if (self.score() == 16):
            return True
        else:
            return False

    def testOneStrike(self):
        self.rollStrike()
        self.roll(3)
        self.roll(4)
        self.rollMany(16, 0)
        if (self.score() == 24):
            return True
        else:
            return False

    def testPerfectGame(self):
        self.rollMany(12, 10)
        if (self.score() == 300):
            return True
        else:
            return False


        
if __name__ == '__main__':
    unittest.main()

def assertEquals(var1, var2):
    if var1 == var2:
        return True
    else:
        return False 
