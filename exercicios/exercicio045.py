import random
print('-------------')
print('   JOKENPÔ   ')
print('-' * 13)
print('  [1] Pedra')
print('  [2] Papel')
print('  [3] Tesoura')
print('-' * 13)
op = int(input(' Opção: '))
c = random.randrange(3)
lista = ['Pedra', 'Papel', 'Tesoura']
print('{} x {}'.format(lista[c], lista[op - 1]))
if (op == 1 and c == 2) or (op == 2 and c == 0) or (op == 3 and c == 1):
    print('Você Ganhou!!! :D')
elif (op == 1 and c == 1) or (op == 2 and c == 2) or (op == 3 and c == 0):
    print('Computador ganhou!')
else:
    print('Empate...')
