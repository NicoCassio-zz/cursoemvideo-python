from pacotes import moeda
n = int(input('Valor: R$ '))
print(f'Aumentado: {moeda.moeda(moeda.aumentar(n))}')
print(f'Diminuido: {moeda.moeda(moeda.diminuir(n))}')
print(f'Dobro: {moeda.moeda(moeda.dobro(n))}')
print(f'Metade: {moeda.moeda(moeda.metade(n))}')
