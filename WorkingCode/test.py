import unittest
from Nine import *
class Test_GUI_Methods(unittest.TestCase):

    def test_switchTurn(self):
        g=GUI(Player('a','white',True),Player('b','black',False))
        g.switchTurn()
        self.assertEqual(g.player1.turn, False)
        self.assertEqual(g.player2.turn, True)

    def test_whoseTurn(self):
        g=GUI(Player('a','white',True),Player('b','black',False))
        whose_turn=g.whoseTurn()
        self.assertEqual(whose_turn,g.player1)
        
    def test_validClick(self):
        g=GUI(Player('a','white',True),Player('b','black',False))
        x1,y1,x2,y2,x3,y3,x4,y4=98,99,145,155,498,502,501,305
        
        self.assertEqual(g.validClick(x1,y1),True)
        self.assertEqual(g.validClick(x2,y2),True)
        self.assertEqual(g.validClick(x3,y3),True)
        self.assertEqual(g.validClick(x4,y4),True)

    def test_retRange(self):
        g=GUI(Player('a','white',True),Player('b','black',False))
        x1,y1,x2,y2,x3,y3,x4,y4=98,99,145,155,498,502,501,305
        
        self.assertEqual(g.retRange(x1,y1),(100,100))
        self.assertEqual(g.retRange(x2,y2),(150,150))
        self.assertEqual(g.retRange(x3,y3),(500,500))
        self.assertEqual(g.retRange(x4,y4),(500,300))
        

if __name__ == '__main__':
    unittest.main()
