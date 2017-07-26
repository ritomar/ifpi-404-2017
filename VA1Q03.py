def soma_termos(quantidade):
    i = 1
    soma = 0
    while i <= quantidade:
        n = int(input("Digite o %d termo: " % i ))
        soma += n
        i += 1
    return soma

k = int(input("Digite a quantidade de termos:"))
print("Soma: %d" % soma_termos(k))

