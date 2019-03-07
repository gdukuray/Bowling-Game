from game import Game
import unittest


class TestBowlingGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

if __name__ == '__main__':
    unittest.main()

def assertEquals(var1, var2):
    if var1 == var2:
        return True
    else:
        return False 
