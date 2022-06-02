import Gui as g
from GameState import *

b = Board()
b.checklines(0,0)


b.path(0 , 0 , 4 , 0)
x = g.GUI(b)

