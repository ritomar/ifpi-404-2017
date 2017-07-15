# Ler um número pelo teclado e informar o produto dos dígitos do número lido.

def produto(n):
    i = 1
    while n > 0:
        i *= (n % 10)
        n //= 10
    return i

print(produto(12345))
