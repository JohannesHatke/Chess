import Gui as g
from GameState import Board, Piece

k1 = Piece(1,"k1")
b = Board()
b.putPiece(k1,0,0)
x = g.GUI(b)


