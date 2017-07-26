notas = [6, 7.5, 8, 6, 5, 10, 9]

soma = 0

for nota in notas:
    soma += nota

print("Média: %.2f" % (soma / len(notas)))

