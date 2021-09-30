import math
class ponto(object):
    def _init_(self,x,y):
        self.x=x
        self.y=y
    def getPonto(self):
        print(f'\nx: {self.x}\t y: {self.y}')
    def set_x(self,x):
        self.x=x
    def set_y(self,y):
      self.y=y

class reta(object):
    def _init_(self,ax,ay,bx,by):
       self.ax=ax
       self.ay=ay
       self.bx=bx
       self.by=by
    def getDistancia(self):
        d=math.sqrt((self.bx-self.ax)*(self.bx-self.ax)+(self.by - self.ay)*(self.by - self.ay))
        print("a distancia e igual a {}".format(d))
    def setA(self,a):
        self.a=a
    def setB(self,b):
        self.b=b
if name=="main":
    x=int(input("insira um valor para x: "))
    y=int(input("insira um valor para y: "))
    print("Forme o ponto a com ax e ay")
    ax=int(input("insira um valor para ax: "))
    ay=int(input("insira um valor para ay: "))
    print("***")
    bx=int(input("insira um valor para bx: "))
    by=int(input("insira um valor para by: "))
    r=ponto(x, y)
    r.getPonto()
    s=reta(ax,ay,bx,by)
    s.getDistancia()