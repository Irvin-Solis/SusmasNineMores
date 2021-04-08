from tkinter import Tk, Canvas, Frame, BOTH
from Board import Board
from Piece import Piece
from Player import Player

ca             =[(100,100),(300,100),(500,100),#coordinate array for placement dots
                 (150,150),(300,150),(450,150),
                 (200,200),(300,200),(400,200),
                 (100,300),(150,300),(200,300),
                 (400,300),(450,300),(500,300),
                 (200,400),(300,400),(400,400),
                 (150,450),(300,450),(450,450),
                 (100,500),(300,500),(500,500)]

coordinateArrayToBoardCoordiantes = {(100,100):(0,0),(300,100):(0,3),(500,100):(0,6),#coordinate array for placement dots
                                     (150,150):(1,1),(300,150):(1,3),(450,150):(1,5),
                                     (200,200):(2,2),(300,200):(2,3),(400,200):(2,4),
                                     (100,300):(3,0),(150,300):(3,1),(200,300):(3,2),
                                     (400,300):(3,4),(450,300):(3,5),(500,300):(3,6),
                                     (200,400):(4,2),(300,400):(4,3),(400,400):(4,4),
                                     (150,450):(5,1),(300,450):(5,3),(450,450):(5,5),
                                     (100,500):(6,0),(300,500):(6,3),(500,500):(6,6)}
boardCoordinatesToCoordinateArray = {(0,0):(100,100),(0,3):(300,100),(0,6):(500,100),#coordinate array for placement dots
                                     (1,1):(150,150),(1,3):(300,150),(1,5):(450,150),
                                     (2,2):(200,200),(2,3):(300,200),(2,4):(400,200),
                                     (3,0):(100,300),(3,1):(150,300),(3,2):(200,300),
                                     (3,4):(400,300),(3,5):(450,300),(3,6):(500,300),
                                     (4,2):(200,400),(4,3):(300,400),(4,4):(400,400),
                                     (5,1):(150,450),(5,3):(300,450),(5,5):(450,450),
                                     (6,0):(100,500),(6,3):(300,500),(6,6):(500,500)}



class GUI:
    def __init__(self,player1,player2):#Whenever Gui class created the game starts.
        self.board = Board()#parameters of GUI board,p1,p2.
        self.player1=player1
        self.player2=player2
        self.pieces=[]
        self.turn=None
        self.root=None
        self.frame=None

    def draw_board(self):
        self.frame.delete('all')#deletes everything from the screen
        whose_turn = self.whoseTurn()#whose turn is it
        #Notifies users whose turn is it
        self.frame.create_text(100,50,font=("Purisa",20), text = (whose_turn.name+"'s Turn"))
        for i in range(len(self.pieces)):#removes all pieces if there are some
            self.frame.delete(i)
        #####################################################
        big_rect=self.frame.create_rectangle(100,100,500,500)
        med_rect=self.frame.create_rectangle(150,150,450,450)
        sma_rect=self.frame.create_rectangle(200,200,400,400)
        line1 = self.frame.create_line(100,300,200,300)
        line2 = self.frame.create_line(300,100,300,200)           #Draws Empty board on a screen
        line3 = self.frame.create_line(400,300,500,300)
        line4 = self.frame.create_line(300,400,300,500)
        placementDots=[]
        r=5
        for i in range(len(ca)):
            x,y=ca[i][0],ca[i][1]
            placementDots.append(self.frame.create_oval(x-r,y-r,x+r,y+r,fill='black'))
        #####################################################
        xi=100
        yi=520
        for i in range(1,8):
            self.frame.create_text(xi,yi,text=str(i)) #draws 1-7 
            if i in (3,4):
                xi+=50
            xi+=50
        xi=80
        yi=500

        
        for i in range(97, 104):# draws a-g 
            self.frame.create_text(xi,yi,text=chr(i))
            if i in (99,100):
                yi-=50
            yi-=50

        ##### Gives some info about the players what color are they and the names
        self.frame.create_text(300, 600, font=("Purisa", 30), text= "Nine Men's Morris")
        self.frame.create_text(600,100, font=("Purisa",20), text = "Player 1")
        self.frame.create_text(600,200, font=("Purisa",20), text = (self.player1.name+"  -  "))
        self.frame.create_oval(685,185,715,215,fill=self.player1.color)
        self.frame.create_text(600,300, font=("Purisa",20), text = "Player 2")
        self.frame.create_text(600,400, font=("Purisa",20), text = (self.player2.name+"  -  "))
        self.frame.create_oval(685,385,715,415,fill=self.player2.color)
        #####
        
        for keys in boardCoordinatesToCoordinateArray:# checks Board object if there are pieces draws them 
            xBoard,yBoard=keys[0],keys[1]
            possiblyPiece=self.board.board[xBoard][yBoard]
            if type(possiblyPiece)==Piece:
                R=15
                xy=boardCoordinatesToCoordinateArray[keys]
                x,y=xy[0],xy[1]
                self.pieces.append(self.frame.create_oval(x-R,y-R,x+R,y+R,fill=possiblyPiece.color))
                
            

        
    def click(self,event):
        x,y = event.x, event.y
        self.frame.delete(self.turn)
##        print('clicked {}, {}'.format(x, y))
##        print(self.validClick(x,y))
        if self.validClick(x,y): #if it is valid click on the board where pieces can be possibly placed
            R=15
            circleCentre=self.retRange(x,y)#ca[i]
##            print("circleCentre: ",circleCentre)
            boardCoordinates=coordinateArrayToBoardCoordiantes[circleCentre]#ca[i]:(x,y)
            xOnBoard,yOnBoard=boardCoordinates[0],boardCoordinates[1]
##            print("boardCoordinates: ",boardCoordinates)
            X,Y=circleCentre[0],circleCentre[1]
##            print("X={} Y={}".format(X,Y))
            validSpotOnBoard=self.board.board[boardCoordinates[0]][boardCoordinates[1]]=='o'
##            print("validSpotOnBoard=self.board.board[{}][{}]=={}==o".format(boardCoordinates[0],boardCoordinates[1],self.board.board[boardCoordinates[0]][boardCoordinates[1]]))
            playerTurn=self.whoseTurn()
##            print(playerTurn.name)
            if validSpotOnBoard and len(playerTurn.pieces)>0:
                self.switchTurn()
                p=playerTurn.pieces[0]
                self.board.placePiece(xOnBoard,yOnBoard,p)
                playerTurn.pieces.pop()
                self.draw_board()
                         
##        print(self.board)
    def switchTurn(self):
        self.player1.turn=not self.player1.turn
        self.player2.turn=not self.player2.turn
        
    def whoseTurn(self):
        if self.player1.turn:
            return self.player1
        return self.player2


    def validClick(self,x,y):
        for i in range(len(ca)):
            X,Y,r=ca[i][0],ca[i][1],5
            if x in range(X-r,X+r+1) and y in range(Y-r,Y+r+1):
                return True
        return False
    
    def retRange(self,x,y):
        for i in range(len(ca)):
            
            X,Y,r=ca[i][0],ca[i][1],5
            if x in range(X-r,X+r+1) and y in range(Y-r,Y+r+1):
                return ca[i]
    def run(self):
        self.root = Tk()
        self.frame = Canvas(self.root, width = 900, height = 900)
        self.draw_board()
        self.frame.bind('<Button-1>',self.click)
        self.frame.pack()
        self.root.mainloop()
        


if __name__=="__main__":
    g=GUI(Player('Default-1','white',True),Player('Default-2','black',False))
    g.run()
        
        
        
            
                    

       




