# Ler um número pelo teclado e informar o fatorial do número lido.

def fatorial(n):
    num = n
    fat = 1
    while n > 0:
        fat *= n 
        n -= 1
    return num, fat

print("O fatorial de %d é %d." % fatorial(5))
