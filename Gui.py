# TODO create one or two other classes that stores Gamestate and handles move checking
# DONE: created the general framework to select frames and make moves
# TODO general cleanup, encapsulating content of this file in one class, to make object oriented programming possible

from tkinter import *
from PIL import ImageTk,Image

dimensions = 480

class GUI:
    def __init__(self):
        self.root = Tk()
        self.root.resizable(False, False)
        self.root.geometry("480x480")

        #assigning all the images
        # TODO assigning pieces images and storing them in a dictionary. 
        Board_img = ImageTk.PhotoImage(Image.open("./Images/Board1.png"))
        self.Border_img = ImageTk.PhotoImage(Image.open("./Images/Borders1.png"))

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
            global x1
            global y1
            x1 = a
            y1 = b
        else:
            self.firstmove = True
            if(self.ismovevalid(x1,y1,a,b)):
                self.domove(x1,y1,a,b)
                print("move successful")

    def getcoord(self, x,y, width) -> (int, int):
        i = width// 8
        return (x // i , y // i)

    
    def domove(self, x1,y1,x2,y2):
        pass #TODO
        #outsource to other class

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


x = GUI()
    

