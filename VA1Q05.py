k = int(input("Digite um número inteiro ou zero para finalizar: "))
maior = k
menor = k
soma = k
quantidade = 1
while k != 0:
    k = int(input("Digite um número inteiro ou zero para finalizar: "))
    if maior < k:
        maior = k
    if menor > k and k != 0:
        menor = k
    if k != 0:
        soma += k
        quantidade += 1

print("Maior: %d" % maior)
print("Menor: %d" % menor)
print("Média: %.2f" % (soma/quantidade))


