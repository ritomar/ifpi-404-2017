def imprime_intervalo(inicio, final, incremento):
   for i in range(inicio, final+1, incremento):
        print(i)

limite = int(input("Limite superior: "))
inc = int(input("Incremento: "))
imprime_intervalo(0, limite, inc)
