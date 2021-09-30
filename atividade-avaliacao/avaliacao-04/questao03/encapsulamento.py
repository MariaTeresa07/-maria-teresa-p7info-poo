class caixa:
    def _init_(self,altura,largura,comprimento):
        self._altura=altura
        self._largura=largura
        self._comprimento=comprimento
    def setAltura(self,valor):
        if str(valor).isnumeric():
            self._altura=valor
    def getAltura(self):
        return self._altura
    def volume(self):
        return self._altura*self._largura*self._comprimento
s = caixa(2,4,7)
print(caixa.volume)
