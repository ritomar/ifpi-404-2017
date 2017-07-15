# Ler um número pelo teclado e informar o fatorial do número lido.

def fatorial(n):
    i = 1
    while n > 0:
        i *= n 
        n -= 1
    return i

print(fatorial(5))
