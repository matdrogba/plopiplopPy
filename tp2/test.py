'''
Created on 3 fevr. 2014

@author: remimastriforti
'''

from tp2.Rectangle import Rectangle
from tp2.Cercle import Cercle
from tp2.Point import Point
from tp2.Groupe import Groupe
from tkinter import *
from tp2.Polygone import Polygone
from tp2.ParseCommand import ParseCommand
from tp2.Application import Application
import re;

'''origineRect1 = Point(4,5);

rect1 = Rectangle("monRectangle",origineRect1,(255, 255, 255, 1.0) ,3, 4);

origineCercle1 = Point(6,6);

cercle1 = Cercle("monCercle", origineCercle1, (255,255,255, 1.0), 5);

originePolygone3 = Point(5,7);

polygone1 = Polygone("monPolygone", originePolygone3, (255,255,255, 1.0), [origineRect1, origineCercle1])

origineGroupe1 = Point(4,7);

groupe1 = Groupe("monGroupe", origineGroupe1, [rect1, cercle1, polygone1]);

rect1.show();

cercle1.show();

polygone1.show();

groupe1.show();

stringParseForme = input("Que voulez vous faire ? (nom type couleur origine cracteristique)");'''

fenetre = Tk()
app = Application(master=fenetre)
app.mainloop()

'''canvas = Canvas(fenetre, width=600, height=500);

def callback(event):
    rec1 = canvas.create_rectangle(figure.origine.x, figure.origine.y, figure.origine.x+figure.longueur, figure.origine.y+figure.largeur, fill=figure.couleur)

canvas.bind("<Button-1>", callback)
canvas.pack()
canvas.mainloop(); '''