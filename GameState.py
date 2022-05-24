
class Piece():
    def __init__(self,col, typ):
        self.col = col #int value 0 for white 1 for black
        self.ty = typ #Placeholder
        self.img = None
    def __repr__(self):
        return self.ty
    def __self__(self):
        return self.ty

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
        
 



