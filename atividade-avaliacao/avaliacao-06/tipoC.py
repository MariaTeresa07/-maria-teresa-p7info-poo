import enum
class TipoCliente():
    fisica=1
    juridica=2

if __name__=="__main__":
    for t in (TipoCliente):
        print(type(t))
        print(t)