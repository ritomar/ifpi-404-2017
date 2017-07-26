quantidade = 0
soma = 0

n = int(input("Digite um valor qualquer, zero para terminar: "))

while n != 0:
    quantidade += 1
    soma += n
    n = int(input("Digite um valor qualquer, zero para terminar: "))

print("Quantidade:", quantidade)
print("Soma:", soma)
print("Média:", soma/quantidade)
