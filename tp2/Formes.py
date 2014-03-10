'''
Created on 3 fevr. 2014

@author: remimastriforti
'''

class Formes:
    def __init__(self, nom, origine):
        self._n = nom;
        self._o = origine;
    
    def _get_nom(self):
        return self._n;
    
    def _set_nom(self, nom):
        self._n = nom;
        
    nom = property(_get_nom, _set_nom);
    
    def _get_origine(self):
        return self._o;
        
    def _set_origine(self,origine):
        self._o=origine;
        
    origine = property(_get_origine, _set_origine);
    
    def show(self):
        print("Caracteristique de la forme nome :",self.nom);
        print("Origine :",self.origine.toString());
    
