import datetime
t = 0
for i in range(0, 7):
    a = int(input('Ano de Nascimento {}: '.format(i + 1)))
    if datetime.date.today().year - a >= 21:
        t += 1
print('Maiores: {}'.format(t))
