from client import Client
from item import Item
from cupon import Cupon
from product import Product
def main():
    c=Client(1,"Kelly",479,'367.521.603-98')
    p=Product(1,1568,'Alface',11)
    i=Item(1,1,2,p)
    p2=Product(2,2340,'Vassoura',11.5)
    i2=Item(2,2,1,p2)
    p3=Product(3,712,'Pá',10.7)
    i3=Item(3,3,1,p3)
    cup=Cupon(1,479,c)
    cup.addItem(i)
    cup.addItem(i2)
    cup.addItem(i3)
    cup.calculeCupon()
    print("valor da nota="+str(c.v_cup))
    cup.prtCupon()
if _name_=="_main_":
    main()
