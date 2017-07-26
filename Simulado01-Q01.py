# Escreva um programa que pergunte o depósito incial e a taxa de
# juros de uma poupança. Escreva os valores mes a mes para os primeiros
# 24 meses. Escreva o total ganho com juros no período.

def evolucao_juros_compostos(capital, taxa, tempo):
    montante = capital
    for i in range(tempo+1):
        print("%4d - %8.2f - %3d%% a.m." % (i, montante, taxa))
        if i == tempo:
            print("Juros = %.2f" % (montante - capital))
        else:
            montante = montante + (montante * (taxa / 100))


evolucao_juros_compostos(100, 1, 24)

