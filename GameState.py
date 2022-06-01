from tkinter import *
from PIL import ImageTk,Image

class Piece():
    def __init__(self,col, typ):
        self.col = col #int value 0 for white 1 for black
        self.ty = typ #Placeholder
        self.img = None
        self.img_onc = None
        self.x = 0
        self.y = 0
        self.changed = True
    def __repr__(self):
        return self.ty
    def __str__(self):
        return self.ty
    def moveset(self):
        print("top")
    def setx(self,x):
        self.x = x
    def sety(self,y):
        self.y = y
 
class King(Piece):
    def __init__(self, col, x, y):
        Piece.__init__(self,col, "a")
        self.x = x
        self.y = y
        self.ty = "k" + str(col)
        print(self.col)
    def moveset(self):
        x = self.x
        y = self.y
        print(f"calc Moveset {x}{y}")

        available = [ (x+1,y),(x+1,y+1),(x+1,y-1),(x,y+1),(x,y-1),(x-1,y+1),(x-1,y),(x-1,y-1) ]
        return available
        print("lower")
    def getKey(self):
        return "k" + str(self.col)
    def __repr__(self):
        return self.getKey()

class Board():
    def __init__(self):
        self.Tiles = [ [None for x in range(8)] for y in range(8) ]
        self.Tiles[0][0] = King(0,0,0)
        self.Tiles[3][0] = King(1,3,0)
        print(f"was sit"+ str(self.Tiles[3][0]))
        #self.Tiles[1][0] = King(1,0,0)
        turn = 0 # 0 for white , 1 for black

    def move(self , x1 , y1 , x,y ):
        #check Turn with color of x1 y1

        print(f"{x1}|{y1} -> {x}|{y}")
        tomove = self.Tiles[x1][y1]
        if tomove is None:
            return False
        if not (x,y) in tomove.moveset():
            print(tomove.moveset())
            print(tomove.x)
            print(tomove.y)
            print("notinmoveset")
            return False
        if self.Tiles[x][y] is None:
            print("hä")
            self.Tiles[x1][y1] = None
            tomove.setx(x) 
            tomove.sety(y)
            self.Tiles[x][y] = tomove
            self.Tiles[x][y].changed = True
            return True
        elif self.Tiles[x][y].col is not tomove.col:
            self.Tiles[x1][y1] = None
            self.Tiles[x][y] = None
            self.Tiles[x][y] = tomove
            tomove.setx(x)
            tomove.sety(y)

    def checkdiagonal(self, x1 ,y1 ,x ,y):
        pass
    def checklines(self,x1,y1):
        #horizontal:
        tempresult = [ ]
        result = [ ]
        ok = True
        i = x1 +1
        while i < 8:
            if self.Tiles[i][y1]:
                result + [(i,y1)]
                i += 1
            else:
                i = 8
        i = x1 -1
        while i > -1:
            if self.Tiles[i][y1]:
                result + [(i,y1)]
                i -= 1
            else:
                i = -8
        #vertikal:
        i = y1 +1
        while i < 8:
            if self.Tiles[x1][i]:
                result + [(x1, i)]
                i += 1
            else:
                i=8

        i = y1 -1
        while i > -1:
            if self.Tiles[x1][i]:
                result + [(x1,i)]
                i -=1
            else:
                i = -1
        
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
                    x = x + "N "
                else:
                    x = x +repr(self.Tiles[i][j])
            x = x + "\n"

        return x
