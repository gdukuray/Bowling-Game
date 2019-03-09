from game import *
import unittest


class TestBowlingGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def rollMany(self, pins):
        for i in range(20):
            self.game.roll(pins)
            
    def testAllOnes(self):
        self.rollMany(20)

    def rollSpare(self):
        self.game.roll(5)
        self.game.roll(5)

    def testOneSpare(self):
        self.rollSpare()
        
if __name__ == '__main__':
    unittest.main()

def assertEquals(var1, var2):
    if var1 == var2:
        return True
    else:
        return False 
