'''
Created on 3 fevr. 2014

@author: remimastriforti
'''

from tp2.Formes import Formes

class FormesSimples(Formes):
    def __init__(self, nom, origine, couleur):
        super().__init__(nom, origine);
        self._c = couleur;
        
    def _get_couleur(self):
        return self._c;
    
    def _set_couleur(self, couleur):
        self._c = couleur;

    couleur = property(_get_couleur, _set_couleur);
    
    def show(self):
        super().show();
        print("Couleur : ",self.couleur);