class Product():
    def _init_(self,id,cod,desc,v_unit):
        self._id=id
        self._cod=cod
        self._desc=desc
        self._v_unit=v_unit
    def getDesc(self):
        return self._desc
    def getV_unit(self):
        return self._v_unit
    def str(self):
        s="\nid={3}\ncodigo={2}\ndescricao={1}\nvalor unitario={0}".format(self._id,self._cod,self._desc,self._v_unit)
        return s
    if _name_=='_main_':
        prod=Product(1,1568,'Alface',11)
        print(prod.str())
