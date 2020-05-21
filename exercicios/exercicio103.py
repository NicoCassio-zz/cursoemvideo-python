def ficha(nome='<desconhecido>', gols=0):
    """
    -> Mostra o rendimento do jogador
    :param nome: nome do jogador
    :param gols: quantidade de gols do jogador
    """
    print(f'{nome:<20}{f"{gols} gols":>10}')
#  Programa principal
print('-' * 30)
n = str(input('Nome: '))
g = str(input('Gols: '))
g = int(g) if g.isnumeric() else 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)
print('-' * 30)
