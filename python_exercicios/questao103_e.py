def ficha(jog='desconhecido', gols=0):
    print(f'O jogador {jog} fez {gols} gols')

j = input('Nome do jogador: ')
g = input('Quantos gols: ')
if g.isalnum():
    g=int(g)
else:
    g=0
if j.strip()=='':
    ficha(gols=g)
else:
    ficha(j,g)


