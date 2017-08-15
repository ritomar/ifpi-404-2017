from random import randrange
def CriaLista(n):
    L = []
    for i in range(n):
        L.append(randrange(100))
    return L


def MostraLista(L):
    for item in L:
        print(item, end=" ")
    print()

L1 = CriaLista(5)
MostraLista(L1)
L2 = CriaLista(7)
MostraLista(L2)
