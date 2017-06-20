# 03. Recebe um valor em minutos, retorna o
#     equivalente em horas e minutos.

def horas_e_minutos(minutos):
    h = minutos // 60
    m = minutos % 60
    return "%d:%d" % (h, m)

print(horas_e_minutos(200))
