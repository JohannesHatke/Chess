# TODO create one or two other classes that stores Gamestate and handles move checking
# DONE: created the general framework to select frames and make moves
# TODO general cleanup, encapsulating content of this file in one class, to make object oriented programming possible

from GameState import Board

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
        Board_img = ImageTk.PhotoImage(Image.open("./Images/Board1.png"))
        self.Border_img = ImageTk.PhotoImage(Image.open("./Images/Borders1.png"))

        self.k1_img = ImageTk.PhotoImage(Image.open("./Images/k1.png"))

        self.img_dict = {
                "k1":self.k1_img,
                }
        self.piece_imgs = [ [None for x in range(8)] for y in range(8) ]
        

        #initialising Board positions of pieces


        self.canvas1 = Canvas(self.root,width = 480, height = 480)
        self.canvas1.pack()
        self.background = self.canvas1.create_image(0,0,anchor=NW, image = Board_img)
        self.border = None #first Boarder is set to nowhere, because we want to delete a boarder before we create a new one
        self.firstmove = True
        self.x1 = 0
        self.y1 = 0

        self.root.bind('<Button-1>',self.click)
        self.root.mainloop()

        
    def click(self,e):
        #executes with every mouseclick
        self.trymove(e.x,e.y)

    #TODO create function that draws piece to a tile, so it can be used by the other functions 

    def trymove(self,x, y):

        (a,b) = self.getcoord(x,y,dimensions)

        if(self.firstmove):
            self.moveBorder(a,b,dimensions)
            self.firstmove = False
            self.x1 = a
            self.y1 = b
        else:
            x1 = self.x1
            y1 = self.y1

            self.firstmove = True

            print(x1,y1,a,b)
            self.Board.move(x1,y1,a,b)
            self.canvas1.delete(self.border)
            #self.redraw2x(x1,a)
            print(self.Board)
            self.drawpiece(self.Board.Tiles[a][b], a,b)

    def redraw2x(self, x1,x):
        line1 = self.Board.getxl(x1)
        print(line1)
        line2 = self.Board.getxl(x)
        print(line2)
        for i in range(len(line1)):
            fig = line1[i]
            if line1[i] is None and self.piece_imgs[x][i] is not None:
                self.canvas1.delete(self.piece_imgs[x][i])
                
            else:
                self.drawpiece(fig,x ,i)
        for i in range(len(line2)):
            fig = line2[i]
            self.drawpiece(fig, x, i)

    def getcoord(self, x,y, width) -> (int, int):
        i = width// 8
        return (x // i , y // i)

    def drawpiece(self,piece, x ,y ):
        if piece is not None:
            if piece.img is not None:
                self.canvas1.delete(piece.img)
            i = dimensions // 8
            bx = x * i
            by = y * i
            piece.img = self.canvas1.create_image(bx,by,anchor=NW, image = self.img_dict[piece.ty])
        else :
            print("leer")

       #

    

    def moveBorder(self, x,y,width):
        global border
        self.canvas1.delete(self.border)
        i = width // 8
        bx = x * i
        by = y * i
        self.border = self.canvas1.create_image(bx,by,anchor=NW, image = self.Border_img)

    def ismovevalid(self, x1,y1,x2,y2) -> bool:
        global border
        self.canvas1.delete(self.border)
        border = None
        return True #TODO
        #outsource to other class


    

