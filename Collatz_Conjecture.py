num=int(input("Digite um número inteiro e positivo"))
import numpy as np
import matplotlib.pyplot as mpl

listanum=[num]
it=0

while num !=1:
    it=it+1
    if num % 2 ==0:
        num=num/2
    elif num %2==1:
        num=num*3+1
    listanum.append(num)
    print(num)

print(listanum)

mpl.plot(np.arange(0,it+1),listanum)
mpl.title("Collatz Conjecture")
mpl.xlabel("Numero de iterações")
mpl.ylabel("Numeros da lista")
mpl.grid()
mpl.show()