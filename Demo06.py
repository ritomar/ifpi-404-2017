def menu():
    opcao = 0
    while opcao == 0:
        print("Escolha uma das opções abaixo:")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")
        try:
            opcao = int(input("Digite a sua opção: "))
            if (opcao < 1) or (opcao > 5):
                opcao = 0
        except:
            opcao = 0
    return opcao

def soma(a, b):
    return a + b

def subtrai(a, b):
    return a - b

def multiplica(a, b):
    return a * b

def divide(a, b):
    return a / b

a = float(input("Digite o valor do operando: "))
b = float(input("Digite o valor do operador: "))

op = menu()

while op != 5:
    if op == 1:
        print("%.2f + %.2f = %.2f" % (a, b, soma(a, b)))
    elif op == 2:
        print("%.2f - %.2f = %.2f" % (a, b, subtrai(a, b)))
    elif op == 3:
        print("%.2f x %.2f = %.2f" % (a, b, multiplica(a, b)))
    elif op == 4:
        try:
            print("%.2f / %.2f = %.2f" % (a, b, divide(a, b)))
        except:
            print("Divisão por zero inválida")
              
    op = menu()




