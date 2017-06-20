from random import randrange

def digitoMeio(n):
    if n >= 100 and n <= 999:
        return (n // 10) % 10
    else:
        pass

n = randrange(0, 200)

if digitoMeio(n) != None:
    print("O dígito do meio de %d é %d." % (n, digitoMeio(n)))
else:
    print(n, "não tem 3 dígitos")



