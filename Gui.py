# TODO create one or two other classes that stores Gamestate and handles move checking
# DONE: created the general framework to select frames and make moves
# TODO general cleanup, encapsulating content of this file in one class, to make object oriented programming possible

from GameState import *

from tkinter import *
from PIL import ImageTk,Image


dimensions = 480

class GUI:
    def __init__(self, Board):
        self.Board = Board
        self.root = Tk()
        self.root.resizable(False, False)
        self.root.geometry("480x480")

        #assigning all the images
        # TODO assigning pieces images and storing them in a dictionary. 
        self.Board_img = ImageTk.PhotoImage(Image.open("./Images/Board1.png"))
        self.Border_img = ImageTk.PhotoImage(Image.open("./Images/Borders1.png"))

        self.k1_img = ImageTk.PhotoImage(Image.open("./Images/k1.png"))
        self.k0_img = ImageTk.PhotoImage(Image.open("./Images/k0.png"))

        self.img_dict = {
                "k1":self.k1_img,
                "k0":self.k0_img
                } 
        self.pieces = [ [None for x in range(8)] for y in range(8) ]

        #initialising Board positions of pieces


        self.canvas1 = Canvas(self.root,width = 480, height = 480)
        self.canvas1.pack()
        self.background = self.canvas1.create_image(0,0,anchor=NW, image = self.Board_img)
        self.border = None #first Boarder is set to nowhere, because we want to delete a boarder before we create a new one
        self.firstmove = True
        self.x1 = 0
        self.y1 = 0

        self.drawwholeBoard()
        print(self.Board)

        self.root.bind('<Button-1>',self.click)
        self.root.mainloop()

    def click(self,e):
        (a,b) = self.getcoord(e.x,e.y,dimensions)
        #executes with every mouseclick
        if(self.firstmove):
            self.moveBorder(a,b,dimensions)
            self.firstmove = False
            self.x1 = a
            self.y1 = b
        else:
            x1 = self.x1
            y1 = self.y1
            self.firstmove = True
            if (self.trymove(x1, y1, a,b)):
                self.redraw(x1, y1 ,a ,b)
            self.canvas1.delete(self.border)
            print(self.pieces)

    #TODO create function that draws piece to a tile, so it can be used by the other functions 

    def trymove(self,x1, y1 , x, y):
        ret_val =  self.Board.move(x1,y1,x,y)
        self.drawwholeBoard()
        print(self.Board)
        

    def redraw(self, x1 ,y1 ,a ,b):
        pass
    def drawwholeBoard(self):
        for i in range(8):
            for j in range(8):
                if self.pieces[i][j] is not None:
                    self.canvas1.delete(self.pieces[i][j])


        for i in range(8):
            for j in range(8):
                if self.Board.Tiles[i][j] is not None:
                    bx = i *(dimensions // 8)
                    by = j *(dimensions // 8)
                    self.pieces[i][j] = self.canvas1.create_image(bx,by,anchor=NW, image = self.img_dict[self.Board.Tiles[i][j].getKey()])
                else :
                    if self.pieces[i][j] is not None:
                            self.canvas1.delete(self.pieces[i][j])
                    self.pieces[i][j] = None
                    


    def getcoord(self, x,y, width) -> (int, int):
        i = width// 8
        return (x // i , y // i)

    def moveBorder(self, x,y,width):
        global border
        self.canvas1.delete(self.border)
        i = width // 8
        bx = x * i
        by = y * i
        self.border = self.canvas1.create_image(bx,by,anchor=NW, image = self.Border_img)
