# 03. Recebe um valor em minutos, retorna o
#     equivalente em horas e minutos.

def horas_e_minutos(minutos):
    h = minutos // 60
    m = minutos % 60
    return h, m

h, m = horas_e_minutos(200)
h += 1
m += 5
print("%d:%d" % (h, m))
