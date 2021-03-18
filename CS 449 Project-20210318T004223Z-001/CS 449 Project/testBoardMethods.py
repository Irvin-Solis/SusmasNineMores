import unittest
from Board import *

class Test_Board_Methods(unittest.TestCase):

    def testBoardCreation(self):
        board=Board()
        for i in range(len(board.board)):
            for j in range(len(board.board[i])):
                self.assertEqual(type(board.board[i][j]),str)
    def test_placePiece(self):
        board=Board()
        p=Piece('black')
        board.placePiece(0,0,p)
        self.assertEqual(board.board[0][0],p)
        

if __name__ == '__main__':
    unittest.main()
