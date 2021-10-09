from cupon import Cupon
from product import Product
class ItemCupon:
    def _init_(self):
        self._cupons=[]
        self._prods=[]
    def addCuponProd(self,cupon,prod):
        if isinstance(cupon, Cupon) and isinstance(prod, Product):
            self._cupons.append(cupon)
            self._prods.append(prod)

