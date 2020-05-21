lista = list()
i = 1
while True:
    print('-' * 40)
    print(f'{f"JOGADOR {i}":^40}')
    print('-' * 40)
    lista.append({'nome':str(input('Nome: ')),
                 'partidas':int(input('Partidas: ')),
                  'gols':list(),
                  'total':0})
    for j in range(1, lista[-1]['partidas'] + 1):
        lista[-1]['gols'].append(int(input(f'Gols na partida {j}: ')))
        lista[-1]['total'] += lista[-1]['gols'][-1]
    i += 1
    print()
    op = ' '
    while op not in 'sn':
        op = str(input('Quer continuar? [s/n]'))
    if op == 'n':
        break
while True:
    print('=' * 40)
    print(f'COD {"NOME":<20} {"GOLS":<10} TOTAL')
    print('=' * 40)
    for i, l in enumerate(lista):
        print(f'{i + 1:>3} {l["nome"]:<20} {str(l["gols"]):<10} {l["total"]}')
    print('=' * 40)
    op = int(input('Ver dados do jogador: [999 para parar] '))
    if op == 999:
        break
    print('-' * 40)
    print(f'{lista[op - 1]["nome"].upper():^40}')
    print('-' * 40)
    for i in range(0, lista[op - 1]['partidas']):
        a = lista[op - 1]['gols'][i]
        print(f' Partida {i + 1}: {f"{a} gols":>20}')
