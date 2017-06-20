import random

def ePar(n):
    return n % 2 == 0

def parOuImpar(n):
    return "PAR" if ePar(n) else "IMPAR"

def printParOuImpar(n):
    print(n, "é", parOuImpar(n))

n = random.randrange(0, 11)
print(printParOuImpar(n))




      


    
