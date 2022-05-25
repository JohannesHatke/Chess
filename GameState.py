from PIL import ImageTk,Image

class Piece():
    def __init__(self,col, typ):
        self.col = col #int value 0 for white 1 for black
        self.ty = typ #Placeholder
        self.img = None
        self.x = 1
        self.y = 0
    def __repr__(self):
        return self.ty
    def __str__(self):
        return self.ty
    def moveset(self):
        print("top")
    def setcorrImg(self):
        self.img =ImageTk.PhotoImage(Image.open("./Images/k1.png"))
 

class King(Piece):
    def __init__(self, col):
        Piece.__init__(self,col, "a")
        Piece.y = 0
        print(self.col)
    def moveset(self):
        x = self.x
        y = self.y
        available = [ (x+1,y),(x+1,y+1),(x+1,y-1),(x,y+1),(x,y-1),(x-1,y+1),(x-1,y),(x-1,y-1) ]
        return available
        print("lower")
    def setcorrImg(self):
        if col == 1:
            self.img=ImageTk.PhotoImage(Image.open("./Images/k1.png"))
        else :
            self.img=ImageTk.PhotoImage(Image.open("./Images/k0.png"))




class Board():
    def __init__(self):
        self.Tiles = [ [None for x in range(8)] for y in range(8) ]

    def move(self , x1 , y1 , x,y ):
        tomove = self.Tiles[x1][y1]
        self.Tiles[x1][y1] = None
        self.Tiles[x][y] = tomove

    def putPiece(self, piece, x , y ):
        self.Tiles[x][y] = piece

    def getxl(self, x) -> list:
        return self.Tiles[x]

    def __repr__(self):
        x = ""
        for j in range(8):
            for i in range(8):
                if(self.Tiles[i][j] is None):
                    x = x + "N "
                else:
                    x = x +str(self.Tiles[i][j])
            x = x + "\n"

        return x
        
 


x = King(0)
x.moveset()

y = Piece(0, "k")
y.moveset()
print(x.x)
print(x.y)
