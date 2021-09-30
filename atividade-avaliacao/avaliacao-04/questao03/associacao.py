class pintura():
    def _init_(self,cod_obra,titulo):
        self.cod_obra=cod_obra
        self.titulo=titulo
class Pintor():
    def _init_(self,codPintor,nome,lugar):
        self.codPintor=codPintor
        self.nome=nome
        self.lugar=lugar
        self.obras=list()
    def getPintura(self,pintura):
        self.obras.append(pintura)
    def showPintura(self):
        for a in self.obras:
            print(a[1])
            print()
artVG=Pintor(1,"Van Gogh","Países Baixos")
obraUm=[1,"Starry Night"]
obraDois=[2,"Sunflowers"]
artVG.getPintura(obraUm)
artVG.getPintura(obraDois)
artVG.showPintura()