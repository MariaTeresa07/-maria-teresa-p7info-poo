class venda():
    def _init_(self,cod_venda,*produtos):
        self.cod_venda=cod_venda
        self.produtos=list(map(lambda x:x._dict_,produtos))
    def pay(self):
        for a in self.produtos:
            print(a["Nome"])
        print("total:",sum(list(map(lambda x : x["preco"], self.itens))))
class produto():
    def _init_(self,prod,valor):
        self.prod=prod
        self.valor=valor
vendaUm=venda(1,produto("banana",3.9),produto("feijao",7),produto("arroz",6.5))
vendaUm.pagamento()
