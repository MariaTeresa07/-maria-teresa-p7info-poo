from nota import Nota
from produto import Produto
class ItemNF:
    def _init_(self):
        self._notas=[]
        self._prods=[]
    def addCuponProd(self,nota,prod):
        if isinstance(nota, Nota) and isinstance(prod, Produto):
            self._notas.append(nota)
            self._prods.append(prod)

