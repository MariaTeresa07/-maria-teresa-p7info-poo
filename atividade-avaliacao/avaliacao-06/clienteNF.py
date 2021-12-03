from tipoC import TipoCliente
from flaskrod import db

class ClienteNF(db.Model):
    __tablename__="TB_CLIENTE"
    id = db.Column(db.Integer, primary_key = True)
    cliente = db.Column(db.String)
    cod = db.Column(db.String, unique = True)
    cadastro = db.Column (db.String, unique = True)
    
    def _init_(self,id,cliente,cod,cadastro):
        self._id=id
        self._cliente=cliente
        self._cod=cod
        self._cadastro=cadastro
    
    def str(self):
        s="\nid={3}\nnome={2}\ncodigo={1}\ncpf/cnpj={0}".format(self._cadastro,self._cod,self._client,self._id)
        return s

if __name__=="__main__":
    c=ClienteNF(1,"Kelly",479,'367.521.603-98')
    print(c.str())