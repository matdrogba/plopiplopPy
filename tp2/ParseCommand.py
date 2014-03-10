'''
Created on 3 fevr. 2014

@author: remimastriforti
'''
from tp2.Rectangle import Rectangle
from tp2.Cercle import Cercle
from tp2.Point import Point
from tp2.Groupe import Groupe
from tp2.Polygone import Polygone
import re;

class ParseCommand:
    def __init__(self, chaine):
        self._chaine = chaine;

    def parsePoint(self, sPoint):
        p = re.compile('[0-9]+');
        s = p.findall(sPoint);
        try:
            return Point(int(s[0]), int(s[1]));
        except Exception as inst:
            print(inst);
            raise;
    
    def parseRect(self,nom,sCouleur,sOrigine,sCaracteristique):
        
        origine = self.parsePoint(sOrigine);
        
        p = re.compile('[0-9]+');
        s = p.findall(sCaracteristique);
        try:
            lo = int(s[0]);
            la = int(s[1]);
        except Exception as inst:
            print(inst);
            raise;

        return Rectangle(nom, origine, sCouleur, lo, la);
        
    def parseCercle(self,nom,sCouleur,sOrigine,sCaracteristique):
        
        origine = self.parsePoint(sOrigine);
        rayon = int(sCaracteristique);
        
        return Cercle(nom, origine, sCouleur, rayon);
    
    def parsePoly(self,nom,sCouleur,sOrigine,sCaracteristique):

        origine = self.parsePoint(sOrigine);
        return Polygone(nom,origine,sCouleur,sCaracteristique);
        
        
        
    def parse(self):
        splitStringForme = self._chaine.split();
        
        type = splitStringForme[1];

        if 'cercle' in type:
            figure = self.parseCercle(splitStringForme[0], splitStringForme[2], splitStringForme[3], splitStringForme[4]);
        elif 'rectangle' in type:
            figure = self.parseRect(splitStringForme[0], splitStringForme[2], splitStringForme[3], splitStringForme[4]);
        elif 'polygone' in type:
            listePoints=[];
            for i in range(4, len(self.ensembleDePoint), 1):
                listePoints.append(self.parsePoint(splitStringForme[i]));
            figure = self.parsePoly(splitStringForme[0], splitStringForme[2], splitStringForme[3], listePoints);
        else:
            print('Type introuvable.');
        
        return figure;