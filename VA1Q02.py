def potencia(b, n):
    pot = 1
    for i in range(n):
        pot *= b
    return pot

print(potencia(2, 3))
