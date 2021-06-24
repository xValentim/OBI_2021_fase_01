valores = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13']
naipes = ['C', 'E', 'U', 'P']
baralho_completo = []
for valor in valores:
    for naipe in naipes:
        baralho_completo.append(valor + naipe)
baralho_in = input('')
faltas = {
    'C': 0,
    'E': 0,
    'U': 0,
    'P': 0
}

lista_in = []
repeticoes = []
for i in range(0, len(baralho_in), 3):
    carta_in = baralho_in[i:i+3]
    if carta_in not in lista_in:
        lista_in.append(carta_in)
    else:
        repeticoes.append(carta_in)
for rep in repeticoes:
    naipe_erro = rep[-1]
    faltas[naipe_erro] = 'erro'
for carta in baralho_completo:
    naipe = carta[-1]
    if faltas[naipe] != 'erro' and carta not in lista_in:
        faltas[naipe] += 1

print(faltas['C'])
print(faltas['E'])
print(faltas['U'])
print(faltas['P'])

