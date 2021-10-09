import enum
class TypeClient():
    fisica=1
    juridica=2
if _name_=='_main_':
    for t in (TypeClient):
        print(type(t))
        print(t)