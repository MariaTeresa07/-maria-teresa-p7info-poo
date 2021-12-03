from datetime import datetime
from clienteNF import ClienteNF
from itemNF import Item
class Nota:
    def _init_(self,id,cod,client):
        self._id=id
        self._cod=cod
        self._client=client
        self._date=datetime.today()
        self.items=[]
        self._v_cup=0.0
    def setClient(self, client):
        if isinstance(client,ClienteNF):
            self._client=client
            return self._client
    def addItem(self,item):
        if isinstance(item,Item):
            self._items.append(item)
    def calculeCupon(self):
        v=0.0
        for item in self._items:
            v+=item._v_item
        self._v_cup=v
    def prtCupon(self):
        print(f'''---------------------------------------------------------------------------------------------------
Nota FISCAL \t\t\t\t {self._date}
Cliente: {self._client._cod}\t\t\t\t Nome: {self._client._nome}
CPF/CNPJ: {self._client._cadastro}
---------------------------------------------------------------------------------------------------
PRODUTOS
---------------------------------------------------------------------------------------------------
Seq                        Descrição                           QTD   Valor Unit         Preço
---- -------------------------------------------------------- ----- ------------ ------------------''')
        for a in range(0,3):
            print('{0:17}{1:^34}{2:^28}{3:<8}{4}'.format(self._items[a].getSeq(),self._items[a].getDesc(),self._items[a].getQtd(),self._items[a].getV_unit,self._items.getV_item()))
            print('Valor total:',self._v_cup)