import csv
import random
from rows import Row
from cols import Cols

class Data:
    def __init__(self,src,fun):
        self.rows=[]
        self.cols=None
        self.adds(src,fun)

    def adds(self,src,fun):
        if isinstance(src,str):
            for x in csv.reader(src.splitlines()):
                self.add(x, fun)
        else:
            for x in src or []:
                self.add(x,fun)
        return self
    
    def add(self,t,fun,row):
        row=t.get('cells',None) or Row.new(t)
        if self.cols:
            if fun:
                fun(self,row)
            self.rows.append(self.cols.add(row))
        else:
            self.cols=Cols.new(row)

    def stats(self, cols, fun, ndivs, u):
        u = {".N": len(self.rows)}
        for col in self.cols[cols or "y"]:
            u[col.txt] = round(getattr(col, fun or "mid")(), ndivs)
        return u