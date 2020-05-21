import random
loose = False
t = 0
while True:
    n = int(input('Número: '))
    op = str(input('Pra ou ímpar? [p/i] ')).lower()
    s = n + random.randint(0, 5)
    if (op == 'p' and s % 2 == 1 ) or (op == 'i' and s % 2 == 0 ):
        break
    t += 1
print(f'Vitórias: {t}')
