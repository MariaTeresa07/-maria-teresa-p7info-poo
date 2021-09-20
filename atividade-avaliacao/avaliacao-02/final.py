test=[
    "i luv u"
    "coal is so dark"
    "chondrocraniums"
]
for teste in test:
    newMsg=""
    bigstLen=""
    i=0
    while i<len(teste.split(" ")):
        newMsg+=str(len(teste.split(" ")[i]))+"-"
        if len(teste.split(" ")[i])>len(bigstLen):
            bigstLen=teste.split(" ")[i]
        i+=1
    newMsg=newMsg[-len(newMsg):-1]
    print("{:30s} {}".format(newMsg,bigstLen))