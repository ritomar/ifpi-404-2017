# Ler um número pelo teclado e informar a soma dos dígitos do número lido.

def soma_digitos(n):
    i = 0
    while n > 0:
        i += (n % 10)
        n //= 10
    return i

print(soma_digitos(12345))
