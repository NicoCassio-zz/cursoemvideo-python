import random
n = int(input('Adivinhe o número: '))
if n == random.randint(0, 5):
    print('ACERTOU!! :D')
else:
    print('Errou...')
