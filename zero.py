N = int(input(""))
lista_de_numeros = []
for i in range(N):
    numero = int(input(''))
    if numero == 0:
        del(lista_de_numeros[-1])
    else:
        lista_de_numeros.append(numero)
print(sum(lista_de_numeros))