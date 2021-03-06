from tkinter import *
from PIL import ImageTk,Image

class Piece():
    def __init__(self,col):
        self.col = col #int value 0 for white 1 for black
        self.ty = "a" #Placeholder
        self.img = None
        self.img_onc = None
        self.x = 0
        self.y = 0
        self.changed = True
    def domove(self,board,x ,y):
        pass #placeholder for Pawn
    def __repr__(self):
        return self.ty
    def __str__(self):
        return self.ty
    def moveset(self, board):
        print("top")
    def setx(self,x):
        self.x = x
    def sety(self,y):
        self.y = y
 
class King(Piece):
    def __init__(self, col, x, y):
        super().__init__(col)
        self.setx(x)
        self.sety(y)
        self.ty = "k" + str(col)
        print(self.col)
    def moveset(self, board):
        x = self.x
        y = self.y
        available = [ (x+1,y),(x+1,y+1),(x+1,y-1),(x,y+1),(x,y-1),(x-1,y+1),(x-1,y),(x-1,y-1) ]
        if self.col == 0:
            invcol = 1
        else:
            invcol = 0
        attacked = board.underattack(invcol)
        result = []
        print("-----------------------------------------------King----------------------------------------")
        for i in range(len(available)):
            if available[i] in attacked:
                print(f"this is attacked:{available[i]}")

            else:
                print(f"this is NOT attacked:{available[i]}")
                (b,c) = available[i]
                result += [(b,c)]

        print(f"this is the result:{result}")
                
        return result
        
    def getKey(self):
        return "k" + str(self.col)
    def __repr__(self):
        return self.getKey()

class Rook(Piece):
    def __init__(self, col,x, y):
        super().__init__(col)
        self.setx(x)
        self.sety(y)
        self.ty = "r" + str(col)
        print(self.col)

    def moveset(self, board):

        return board.checklines(self.x,self.y)

    def getKey(self):
        return "r" + str(self.col)

    def __repr__(self):
        return self.getKey()

class Bishop(Piece):
    def __init__(self,col,x,y):
        super().__init__(col)
        self.setx(x)
        self.sety(y)

    def moveset(self, board):

        return board.checkdiagonal(self.x,self.y)

    def getKey(self):
        return "b" + str(self.col)

    def __repr__(self):
        return self.getKey()

class Queen(Piece):
    def __init__(self,col,x,y):
        super().__init__(col)
        self.setx(x)
        self.sety(y)

    def moveset(self, board):

        return board.checkdiagonal(self.x,self.y) + board.checklines(self.x,self.y)

    def getKey(self):
        return "q" + str(self.col)

    def __repr__(self):
        return self.getKey()

class Knight(Piece):
    def __init__(self,col,x,y):
        super().__init__(col)
        self.setx(x)
        self.sety(y)

    def moveset(self, board):
        x = self.x
        y = self.y
        L = [ (x+2,y+1),(x+1,y+2), (x+2,y-1),(x+1,y-2), (x-2,y+1),(x-1,y+2), (x-1,y-2),(x-2,y-1) ]
        
        def inbounds(val) -> bool:
            return (val>-1) and (val<8)

        available = [ ]
        for e in L:
            i = e[0]
            j = e[1]
            if inbounds(i) and inbounds(j):
                available += [e]
        return available

    def getKey(self):
        return "kn" + str(self.col)

    def __repr__(self):
        return self.getKey()


class Pawn(Piece):
    def __init__(self,col,x,y):
        super().__init__(col)
        self.setx(x)
        self.sety(y)
        self.moved = False
        self.enpassant = False

    def moveset(self, board):
        #need to define direction using d
        d = -1 + self.col * 2
        available = []
        if board.Tiles[self.x][self.y + d*1] is None:
            available += [(self.x,self.y+d*1)]
            if not self.moved and board.Tiles[self.x][self.y+d*2] is None:
                available += [(self.x,self.y+d*2)]
        if board.Tiles[self.x+1][self.y + d*1] is not None:
            available += [(self.x+1,self.y+d*1)]

        if board.Tiles[self.x-1][self.y + d*1] is not None:
            available += [(self.x-1,self.y+d*1)]

        # check enpassant 
        invcol = 0 #color of enemy
        if self.col == 0:
            invcol = 1

        if board.Tiles[self.x-1][self.y] is not None:
            if board.Tiles[self.x-1][self.y].getKey() == "p"+str(invcol):
                if board.Tiles[self.x-1][self.y].enpassant == True:
                    available += [(self.x-1,self.y+d*1)]

        return available
        



    def domove(self, board, x ,y):
        self.moved = True
        self.enpassant = False
        y1 = self.y
        x1 = self.x
        diff = y -y1

        invcol = 0 #color of enemy
        if self.col == 0:
            invcol = 1

        if diff == 2 or diff == -2:
            self.enpassant = True
        #check if move im doint is an enpassant move:
        if board.Tiles[self.x-1][self.y] is not None:
            if board.Tiles[self.x-1][self.y].getKey() == "p"+str(invcol) and board.Tiles[x][y] is None:
                board.Tiles[self.x-1][self.y] = None
        if board.Tiles[self.x+1][self.y] is not None:
            if board.Tiles[self.x+1][self.y].getKey() == "p"+str(invcol) and board.Tiles[x][y] is None:
                board.Tiles[self.x+1][self.y] = None
        

    def getKey(self):
        return "p" + str(self.col)

    def __repr__(self):
        return self.getKey()



class Board():
    def __init__(self):
        self.Tiles = [ [None for x in range(8)] for y in range(8) ]
        self.Tiles[0][0] = King(0,0,0)
        self.Tiles[3][0] = King(1,3,0)
        self.Tiles[2][2] = Rook(0,2,2)
        self.Tiles[7][7] = Bishop(1,7,7)
        self.Tiles[4][4] = Queen(0,4,4)
        self.Tiles[5][6] = Pawn(0,5,6)
        self.Tiles[6][1] = Pawn(1,6,1)
        self.Tiles[0][7] = Knight(1,0,7)

        print(f"was sit"+ str(self.Tiles[3][0]))
        #self.Tiles[1][0] = King(1,0,0)
        self.turn = 0 # 0 for white , 1 for black
    def nextturn(self):
        if self.turn == 0:
            self.turn = 1
        else:
            self.turn = 0

    def move(self , x1 , y1 , x,y ):
        #checks all the requirements, before calling actualmove, when they are met
        #check Turn with color of x1 y1

        print(f"{x1}|{y1} -> {x}|{y}")
        tomove = self.Tiles[x1][y1]
        if tomove is None:
            return False
        #normal checks
        if tomove.col != self.turn:
            print("-------------------------------------------Wrong Color----------------------------------------------")
            return False
        if not (x,y) in tomove.moveset(self): #moveset includes captures
            print(tomove.moveset(self))
            print(tomove.x)
            print(tomove.y)
            print("notinmoveset")
            return False
        if self.Tiles[x][y] is None:
            self.actualmove(x1,y1,x,y)
            return True
        elif self.Tiles[x][y].col is not tomove.col: #keep
            self.actualmove(x1,y1,x,y)
            return True

    def actualmove(self, x1,y1, x,y):
        #function that actually changes coordinates and does everything for move
        self.nextturn()
        tomove = self.Tiles[x1][y1]
        tomove.domove(self,x,y)#has to be called before changing coordinate attributes
        self.Tiles[x1][y1] = None
        self.Tiles[x][y] = None
        self.Tiles[x][y] = tomove
        tomove.setx(x)
        tomove.sety(y)

    def checkdiagonal(self, x1 ,y1):
        result = []
        i = 1
        while i+x1 <8 and i + y1 < 8:
            if self.Tiles[x1+i][y1+i] is None:
                result += [(x1+i,y1+i)]
                i+=1
            else:
                result += [(x1+i, y1+i)]
                i = 8
        i = 1
        while x1+i <8 and y1-i > -1:
            if self.Tiles[x1+i][y1-i] is None:
                result += [(x1+i,y1-i)]
                i+=1
            else:
                result += [(x1+i, y1-i)]
                i = 8
        i = 1
        while x1-i >-1 and i + y1 < 8:
            if self.Tiles[x1-i][y1+i] is None:
                result += [(x1-i,y1+i)]
                i += 1
            else:
                result += [(x1-i, y1+i)]
                i = 8
        i = -1
        while i+x1 >-1 and i + y1 >-1 :
            if self.Tiles[x1+i][y1+i] is None:
                result += [(x1+i,y1+i)]
                i -= 1
            else:
                result += [(x1+i, y1+i)]
                i = -8

        
        return result
    def checklines(self,x1,y1):
        #horizontal:
        tempresult = [ ]
        result = []
        ok = True
        i = x1 +1
        print(i)
        print("checklines")
        while (i < 8):
            print(i)
            if self.Tiles[i][y1] is None:
                print(i)
                result += [(i,y1)]
                i += 1
            else:
                result += [(i,y1)]
                i = 8
        i = x1 -1
        while i > -1:
            if self.Tiles[i][y1] is None:
                result += [(i,y1)]
                i -= 1
            else:
                result += [(i,y1)]
                i = -8
        #vertikal:
        i = y1 +1
        while i < 8:
            if self.Tiles[x1][i] is None:
                result += [(x1, i)]
                i += 1
            else:
                result += [(x1,i)]
                i=8

        i = y1 -1
        while i > -1:
            if self.Tiles[x1][i] is None:
                result += [(x1,i)]
                i -=1
            else:
                result += [(x1,i)]
                i = -1
        
        print(result)
        return result
    def underattack(self, col):
        #col of the Player thats attacking
        result = []
        for i in range(0,8):
            for j in range(0,8):
                if self.Tiles[i][j] is not None:
                    if self.Tiles[i][j].col == col and not (self.Tiles[i][j].getKey() == "k0" or self.Tiles[i][j].getKey() == "k1"):
                        result += self.Tiles[i][j].moveset(self)

        return result

    
            
    def path(self, x1 ,y1 ,x ,y):


        print(f"path from {x1}|{y1} to {x}|{y}")
        offx = x1 -x
        offy = y1 -y
        print(offx)
        print(offy)
        result = True
        if (offx == offy):
            if offx < 0:
                j = offx +1
                while j is not 0:
                    result = result and not self.Tiles[x1+j][y1+j]
                    j += 1

            if offx > 0:
                j = offx -1
                while j is not 0:
                    result = result and not self.Tiles[x1+j][y1+j]
                    j -= 1


        elif (offx == -1 * offy):
            pass 


            #diagonal
        elif(offy == 0):
            print("horizontal")
            #horizontal
            if x > x1:
                for i in range(x1+1,x):
                    result = result and not self.Tiles[i][y]
                    print(f"x:{x},y:{i},{result}")
            if x < x1:
                for i in range(x+1,x1):
                    result = result and not self.Tiles[i][y]
                    print(f"x:{x},y:{i},{result}")
                

        elif(offx == 0):
            print("vertical")
            #vertical
            if y > y1:
                for i in range(y1+1,y):
                    result = result and not self.Tiles[x][i]
                    print(f"x:{x},y:{i},{result}")
            if y < y1:
                for i in range(y+1, y1):
                    result = result and not self.Tiles[x][i]
                    print(f"x:{x},y:{i},{result}")
        return result

    def putPiece(self, piece, x , y ):
        self.Tiles[x][y] = piece

    def getxl(self, x) -> list:
        return self.Tiles[x]

    def changeTurn(self):
        if self.turn == 0:
            self.turn = 1
        else:
            self.turn = 0

    def __repr__(self):
        x = ""
        for j in range(8):
            for i in range(8):
                if(self.Tiles[i][j] is None):
                    x = x + "N"
                else:
                    x = x +repr(self.Tiles[i][j])
                x += "\t"
            x = x + "\n"

        return x
