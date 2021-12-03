from clienteNF import ClienteNF
from itemNF import Item
from nota import Nota
from produto import Produto
def main():
    c=ClienteNF(1,"Kelly",479,'367.521.603-98')
    p=Produto(1,1568,'Alface',11)
    i=Item(1,1,2,p)
    p2=Produto(2,2340,'Vassoura',11.5)
    i2=Item(2,2,1,p2)
    p3=Produto(3,712,'Pá',10.7)
    i3=Item(3,3,1,p3)

    cup=Nota(1,479,c)
    cup.addItem(i)
    cup.addItem(i2)
    cup.addItem(i3)
    cup.calculeCupon()
    print("valor da nota="+str(c.v_cup))
    cup.prtCupon()

if __name__=="__main__":
    main()
