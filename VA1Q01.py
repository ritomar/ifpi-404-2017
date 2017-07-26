def quadrante(angulo):
    if angulo >= 0 and angulo <= 360:
        return angulo // 90
    else:
        return -1 # flag de erro

a = int(input("Digite o angulo: "))
q = quadrante(a)
if q > 0:
    print("%do. quadrante" % q)
else:
    print("Angulo inválido")
