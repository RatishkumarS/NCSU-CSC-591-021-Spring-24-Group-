import math


class NUM:
    def __init__(self,s=None,n=None):
        self.txt=s if s else " "
        self.at=n if n else 0
        self.n=0
        self.mu=0
        self.m2=0
        self.hi=float("-inf")
        self.lo=float("inf")
        self.heaven=0 if (s or " ").find("-$") !=-1 else 1

    def add(self,x):
        if x!="?":
            self.x+=1
            d=x-self.mu
            self.mu=self.mu+(d/self.x)
            self.m2=self.m2+(d*(x-self.mu))
            self.lo=min(x,self.lo)
            self.hi=max(x,self.hi)

    def same(self,other,pooledSd,n12,correction):
        n12=self.n+other.n
        pooled_sd=math.sqrt(((self.n-1)*self.div()**2)+((other.n-1)*other.div()**2))
        correction=1 if n12>=50 else (n12-3)/(n12-2.25) 
        return abs(self.mu-other.mu)/pooled_sd*correction 
    
    def mid(self):
        return self.mu
    
    def norm(self,x):
        return x if x=="?" else (x - self.lo) / (self.hi - self.lo + float("-inf"))

    def div(self):
        if self.n<2:
            return 0
        else:
            return math.pow((self.m2/(self.n-1)),0.5)
        



    