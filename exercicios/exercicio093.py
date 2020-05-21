jogador = dict()
jogador['nome'] = str(input('Nome: '))
jogador['partidas'] = int(input('Total de Partidas: '))
jogador['gols'] = list()
jogador['total'] = 0
for i in range(0, jogador['partidas']):
    jogador['gols'].append(int(input(f'Gols da {i + 1}ª partida: ')))
for i in jogador['gols']:
    jogador['total'] += i
print('-' * 30)
print(f'{"SITUAÇÃO":^30}')
print('-' * 30)
for k, v in jogador.items():
    print(f'{k.capitalize():<15} {v}')
print('-' * 30)
print(f'{"PARTIDAS":^30}')
print('-' * 30)
for i, g in enumerate(jogador['gols']):
    print(f' {f"Partida {i + 1}:":>12} {g} gols')
