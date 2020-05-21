from pacotes import moeda
n = int(input('Valor: R$ '))
print(f'Aumentado: {moeda.aumentar(n, True)}')
print(f'Diminuido: {moeda.diminuir(n)}')
print(f'Dobro: {moeda.dobro(n, True)}')
print(f'Metade: {moeda.metade(n)}')
