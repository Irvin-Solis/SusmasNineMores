from Player import Player
from Piece import Piece

conversionTable={'g1':(0,0),'g4':(0,3),'g7':(0,6),
                 'f2':(1,1),'f4':(1,3),'f6':(1,5),
                 'e3':(2,2),'e4':(2,3),'e5':(2,4),
                 'd1':(3,0),'d2':(3,1),'d3':(3,2),
                 'd5':(3,4),'d6':(3,5),'d7':(3,6),
                 'c3':(4,2),'c4':(4,3),'c5':(4,4),
                 'b2':(5,1),'b4':(5,3),'b6':(5,5),
                 'a1':(6,0),'a4':(6,3),'a7':(6,6)}
                 
              
class Board:
    def __init__(self):
        self.adjacency={'a1':['d1','a4'],'a4':['a1','a7','b4'],
                    'a7':['d7','a4'],'b2':['d2','b4'],
                    'b4':['a4','b2','b6','c4'],'b6':['b4','d6'],
                    'c3':['d3','c4'],'c4':['c3','c5','b4'],
                    'c5':['d5','c4'],'d1':['a1','g1','d2'],
                    'd2':['d1','d3','b2','f2'],'d3':['e3','c3'],
                    'd5':['d6','e5','c5'],'d6':['d5','d7','f6','b6'],
                    'd7':['a7','g7'],'e3':['d3','e4'],
                    'e4':['e3','e5','f4'],'e5':['d5','e4'],
                    'f2':['d2','f4'],'f4':['e4','f2','f6','g4'],
                    'f6':['f4','d6'],'g1':['d1','g4'],
                    'g4':['g1','g7','f4'],'g7':['d7','g4']}
        self.board=[[],[],[],[],[],[],[]]
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                self.board[i].append(' ')

        for keys in self.adjacency:
            coords=conversionTable[keys]
            x=coords[0]
            y=coords[1]
            self.board[x][y]='o'
##        for i in range(len(self.board)):
##            for j in range(len(self.board)):
##                print(self.board[i][j],end=' ')
##            print()
    def placePiece(self,x,y,Piece):
        self.board[x][y]=Piece
    def __str__(self):
        string=''
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                string+=(str(self.board[i][j])+' ')
            string+='\n'
        return string
        

                    
                    
                    
