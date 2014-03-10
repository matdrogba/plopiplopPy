'''
Created on 3 fevr. 2014

@author: remimastriforti
'''

from tp2.FormesSimples import FormesSimples

class Rectangle(FormesSimples):
    def __init__(self, nom, origine, couleur, lo, la):
        super().__init__(nom, origine, couleur);
        self._lo = lo;
        self._la = la;
        
    def _get_lo(self):
        return self._lo;
    
    def _set_lo(self, lo):
        self._lo = lo;
        
    longueur = property(_get_lo, _set_lo);
    
    def _get_la(self):
        return self._la;
    
    def _set_la(self, la):
        self._la = la;
        
    largeur = property(_get_la, _set_la);
    
    def show(self):
        super().show();
        print("Type : Rectangle");
        print("Longueur :[",self.longueur,"] Largeur :[",self.largeur,"]");