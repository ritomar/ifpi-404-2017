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

def soma():
    op = '+'
    for i in range(1, 11):
        for j in range(1, 11):
            print("%d %s %d = %d" % (i, op, j, i + j))
        print("")

def subtrai():
    op = '-'
    for i in range(1, 11):
        for j in range(1, 11):
            print("%d %s %d = %d" % (i, op, j, i - j))
        print("")

def multiplica():
    op = '*'
    for i in range(1, 11):
        for j in range(1, 11):
            print("%d %s %d = %d" % (i, op, j, i * j))
        print("")

def divide():
    op = '/'
    for i in range(1, 11):
        for j in range(1, 11):
            print("%d %s %d = %d" % (i, op, j, i / j))
        print("")

op = menu()

while op != 5:
    if op == 1:
        soma()
    elif op == 2:
        subtrai()
    elif op == 3:
        multiplica()
    elif op == 4:
        divide()

    op = menu()




