'''
Created on 3 fevr. 2014

@author: remimastriforti
'''

from tp2.FormesSimples import FormesSimples

class Polygone(FormesSimples):
    def __init__(self, nom, origine, couleur, ensemblePoint):
        super().__init__(nom, origine, couleur)
        self._ensemblePoint = ensemblePoint;
        
    def _get_ensemblePoint(self):
        return self._ensemblePoint;
    
    def _set_ensemblePoint(self, ensemblePt):
        self._ensemblePoint = ensemblePt;
        
    ensembleDePoint = property(_get_ensemblePoint, _set_ensemblePoint);
    
    def addPoint(self, point):
        self._ensemblePoint.append(point);
        
    def show(self):
        super().show();
        print("Type : Polygone");
        print("Listage des points du polygone")
        for i in range(0, len(self.ensembleDePoint), 1):
            print("Point num",i," :",self.ensembleDePoint[i].toString());