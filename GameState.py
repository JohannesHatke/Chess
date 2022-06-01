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
 
class King(Piece):
    def __init__(self, col, x, y):
        Piece.__init__(self,col, "a")
        Piece.x = x
        Piece.y = y
        Piece.ty = "k" + str(col)
        print(self.col)
    def moveset(self):
        x = self.x
        y = self.y
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
        self.Tiles[1][0] = King(1,0,0)
        turn = 0 # 0 for white , 1 for black

    def move(self , x1 , y1 , x,y ):
        #check Turn with color of x1 y1

        tomove = self.Tiles[x1][y1]
        if tomove is not None and self.Tiles [x][y] is None:
            self.Tiles[x1][y1] = None
            tomove.x = x
            tomove.y = y
            self.Tiles[x][y] = tomove
            self.Tiles[x][y].changed = True
        return True

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
