class bankAcc():
    extrato=900
    def _init_(self,saldo):
        self._saldo=saldo
        bankAcc.extrato+=saldo
    def saque(self,v):
        self._saldo-=v
        bankAcc.extrato-=v
    def deposito(self,v):
        self._saldo+=v
        bankAcc.extrato+=v
    def getExtrato(self):
        return self._saldo
    def setSaldo(self,new):
        self._saldo=new 
bankUm=bankAcc(900)
bankUm.deposito(8000)
print(bankUm.getExtrato())
bankUm.saque(400)
print(bankUm.getExtrato())
print(bankAcc.extrato)
