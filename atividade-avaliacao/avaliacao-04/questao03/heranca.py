class pessoa:
    def _init_(self,nome,idade):
        self.nome=nome
        self.idade=idade
  
    def mostrarNome(self):
        print(self.nome)
  
    def mostrarIdade(self):
        print(self.idade)
 
class estudante(pessoa):
    def _init_(self,nome,idade,matricula):
        pessoa._init_(self,nome,idade)
        self.matricula=matricula    
   
    def mostrarMatricula(self):
        print(self.matricula)
p=pessoa("marcos",30)
p.mostrarIdade()
s=estudante("isabel",20,100)
s.mostrarNome()
s.mostrarMatricula()