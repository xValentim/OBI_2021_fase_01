N = int(input(''))
registros_0 = []
for i in range(N):
    msg = input('').split()
    registros_0.append(msg)
#print(registro_0)
registros = [registros_0[0]]
for i in range(1, N):
    if registros_0[i][0] != 'T' and registros_0[i - 1][0] in ['R', 'E']:
        registros.append(['T', '1'])
    registros.append(registros_0[i])
#print(registros)
tempo = {}
for msg in registros:
    # start clock
    if msg[0] == 'R':
        if msg[1] not in tempo.keys():
            tempo[msg[1]] = [0, 'esperando']
        else:
            tempo[msg[1]][1] = 'esperando'
    # end clock
    elif msg[0] == 'E':
        tempo[msg[1]][1] = 'enviado'
    else:
        for amigo in tempo:
            if tempo[amigo][1] == 'esperando':
                tempo[amigo][0] += int(msg[1])
for t in tempo:
    if tempo[t][1] == 'esperando':
        tempo[t][0] = -1

amigos = list(tempo.keys())
amigos.sort()
tempo_total = [tempo[amigo][0] for amigo in amigos]

for i in range(len(amigos)):
    print(amigos[i], tempo_total[i])

    