'''
Created on 3 fevr. 2014

@author: remimastriforti
'''
from tp2.Formes import Formes

class Groupe(Formes):
    def __init__(self, nom, origine, ensembleFigure):
        super().__init__(nom, origine);
        self._ensembleFigure = ensembleFigure;
        
    def _get_ensembleFigure(self):
        return self._ensembleFigure;
    
    def _set_ensembleFigure(self, ensembleFig):
        self._ensembleFigure = ensembleFig;
    
    ensembleFigure = property(_get_ensembleFigure, _set_ensembleFigure);
    
    def addFigure(self, figure):
        self._ensembleFigure.append(figure);
        
    def delFigure(self, figure):
        self._ensembleFigure.remove(figure);
        
    def show(self):
        super().show();
        print("Type : Groupe");
        for i in range(0, len(self.ensembleFigure), 1):
            self.ensembleFigure[i].show();
                