'''
Created on 3 fevr. 2014

@author: remimastriforti
'''
class Point:
    def __init__(self, ordx, ordy):
        self._x = ordx;
        self._y = ordy;
        
    def _get_x(self):
        return self._x;
    
    def _set_x(self, ordx):
        self._x = ordx;
        
    x = property(_get_x, _set_x);
        
    def _get_y(self):
        return self._y;
    
    def _set_y(self, ordy):
        self._y = ordy;
        
    y = property(_get_y, _set_y);
    
    def show(self):
        print("x[",self.x,"] y[",self.y,"]");
        
    def toString(self):
        s = "x[{x}] y[{y}]"
        return s.format(x=self.x, y=self.y);