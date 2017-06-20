def estado(sigla):
    if sigla.upper() == 'CE':
        return 'CEARENSE'
    elif sigla.upper() == 'SP':
        return 'PAULISTA'
    elif sigla.lower() == 'mg':
        return 'MINEIRO'
    else:
        return 'OUTROS ESTADOS'

uf = input("Digite a sigla do seu estado: ")
print(estado(uf))
