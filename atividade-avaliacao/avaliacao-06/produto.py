from flaskrod import db

class Produto(db.Model):
    __tablename__ = "TB_PRODUTO"
    id=db.Column(db.Integer, primary_key=True)
    cod=db.Column(db.String, unique=True)
    desc=db.Column(db.String)
    v_unit=db.Column(db.Float)

    def __init__(self,id,cod,desc,v_unit):
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

if __name__=="__main__":
    prod=Produto(1,1568,'Alface',11)
    print(prod.str())
