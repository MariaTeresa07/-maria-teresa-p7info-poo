class Client():
    def _init_(self,id,client,cod,cadastro):
        self._id=id
        self._client=client
        self._cod=cod
        self._cadastro=cadastro
    def str(self):
        s="\nid={3}\nnome={2}\ncodigo={1}\ncpf/cnpj={0}".format(self._cadastro,self._cod,self._client,self._id)
        return s
if _name_=='_main_':
    c=Client(1,"Kelly",479,'367.521.603-98')
    print(c.str())