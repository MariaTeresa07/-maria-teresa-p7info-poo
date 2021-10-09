from product import Product
class Item():
    def _init_(self,id,seq,qtd,prod):
        self._id=id
        self._seq=seq
        self._qtd=qtd
        self._prod=prod
        self._desc=self._prod.getDesc()
        self._v_unit=self._prod.getV_unit()
        self._v_item=float(self._qtd*self._v_unit)
    def str(self):
        s="\nid={5} sequencial={4} quantidade={3} produto={2} valor unitario={1} valor item={0}".format(self._v_item,self._v_unit,self._desc,self._seq,self._id)
        return s
    def getIs(self):
        return self._id
    def getSeq(self):
        return self._seq
    def getQtd(self):
        return self._qtd
    def getProd(self):
        return self._prod
    def getDesc(self):
        return self._desc
    def getVunit(self):
        return self._v_unit
    def getVitem(self):
        return self._v_item
if _name_=='_main_':
    prod=Product(1,1568,'Alface',11)
    print(prod.str())