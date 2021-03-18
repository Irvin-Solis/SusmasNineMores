from Piece import *
class Player:
    def __init__(self,name,color,turn=True):
        self.turn = turn
        self.name = name
        self.pieces=[]
        for i in range(9):
            self.pieces.append(Piece(color))
        self.color=color
