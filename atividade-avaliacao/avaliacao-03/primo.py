print("Digite um numero:")
a=int(input())
def primo(pri):
    count=0
    for i in range(1, pri+1):
        if pri%i==0:
	        count=count+1
    if count==2:
        return True
    else:
        return False
def showPri(a):	
    s=0
    numero=0
    count2=0 
    while count2<a:	 
        if primo(numero):
            count2=count2+1
            s=s+numero
        numero=numero+1    	
    return s
print(showPri(a))