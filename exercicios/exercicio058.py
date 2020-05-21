import random
r = random.randint(0, 10)
n = -1
p = 0
while n != r:
    n = int(input('Adivinhe o número: '))
    p += 1
    if n == r:
        print('ACERTOU!! :D')
        print('Palpites: {}'.format(p))
    else:
        print('Errou...')
