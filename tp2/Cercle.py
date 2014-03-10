'''
Created on 3 fevr. 2014

@author: remimastriforti
'''

from tp2.FormesSimples import FormesSimples

class Cercle(FormesSimples):
    def __init__(self, nom, origine, couleur, rayon):
        super().__init__(nom,origine,couleur);
        self._rayon = rayon;
    
    def _get_rayon(self):
        return self._rayon;
    
    def _set_rayon(self, rayon):
        self._rayon = rayon;
        
    rayon = property(_get_rayon, _set_rayon);
        
    def show(self):
        super().show();
        print("Type : Cercle");
        print("Rayon:",self.rayon);