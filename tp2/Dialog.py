'''
Created on 20 fevr. 2014

@author: remimastriforti
'''

from tkinter import *
import tkinter.simpledialog

class RectangleDialog(tkinter.simpledialog.Dialog):
    
    def body(self, master):
        Label(master, text="Nom:").grid(row=0)
        Label(master, text="Couleur:").grid(row=1)
        Label(master, text="Longueur:").grid(row=2)
        Label(master, text="Largeur:").grid(row=3)
        self.e1 = Entry(master)
        self.e2 = Entry(master)
        self.e3 = Entry(master)
        self.e4 = Entry(master)
        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        self.e3.grid(row=2, column=1)
        self.e4.grid(row=3, column=1) 
        
        '''if self._rectangle != None :
            self.e1.insert(0, self._rectangle.nom)
            self.e2.insert(0, self._rectangle.couleur)
            self.e3.insert(0, self._rectangle.longueur)
            self.e4.insert(0, self._rectangle.largeur)'''
            
        return self.e1 # initial focus
            
    
    def apply(self):
        nom = self.e1.get()
        couleur = self.e2.get()
        longueur = self.e3.get()
        largeur = self.e4.get()
        self.result = nom,couleur,longueur,largeur        