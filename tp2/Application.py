'''
Created on 13 fevr. 2014

@author: remimastriforti
'''
from tp2.ParseCommand import ParseCommand
from tp2.Dialog import *
from tkinter import *

class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master);
        self._master = master;
        self._canvas = Canvas(self._master, width=600, height=500)
        self._canvas.bind("<Button-1>", self.detectClickLeft)
        self._canvas.bind("<Button-2>", self.detectClickRight)
        self._menu = Menu(self._master, tearoff=0)
        self._xyClickRight = None
        self.createWidgets();

    def createWidgets(self):
        self.QUIT = Button(self, text="QUIT", fg="red", command=self._master.destroy);
        self.QUIT.pack(side="left");
        
        self._menu.add_command(label="Creer", command=self.creationFigure) 
        self._menu.add_command(label="Modifier", command=self.modifierFigure)
        self._menu.add_command(label="Supprimer", command=self.supprimerFigure)
        self._canvas.pack()
        

    def detectClickLeft(self,event):
        items = self._canvas.find_withtag("current")
        if not items:
            return
        self.item = items[0]
        self._canvas.itemconfigure("premier",width=0,tags=None)
        self._canvas.tag_raise(self.item)
        self._canvas.itemconfigure(self.item, outline='orange', width=3,tags="premier")

    def detectClickRight(self,event):
        self._xyClickRight = (event.x, event.y)
        self._menu.post(event.x_root, event.y_root)

    def creationFigure(self):
        d = RectangleDialog(self._master)
        resultat = d.result
        if resultat!=None:
            self._canvas.itemconfigure("premier",width=0,tags=None)
            commandForme = ParseCommand("{0} rectangle {1} ({2},{3}) lo{4}la{5}".format(resultat[0],resultat[1],self._xyClickRight[0],self._xyClickRight[1],resultat[2], resultat[3]))
            self._xyClickRight = None
            figure = commandForme.parse()
            rec1 = self._canvas.create_rectangle(figure.origine.x, figure.origine.y, figure.origine.x+figure.longueur, figure.origine.y+figure.largeur, fill=figure.couleur)
            self._canvas.itemconfigure(rec1,outline='orange', width=3,tags="premier")
        
        
    def modifierFigure(self,event):
        print("modifier")
        
    def supprimerFigure(self):
        item = self._canvas.find_withtag("current")
        self._canvas.delete(item)

    
    def say_hi(self):
        print("hi there, everyone!")
        
        