# Ler um número pelo teclado e informar quantos digitos tem o número lido.

def comprimento(n):
    i = 0
    while n > 0:
        i += 1
        n //= 10
    return i

print(comprimento(12345))
