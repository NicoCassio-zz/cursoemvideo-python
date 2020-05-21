import datetime
a = int(input('Ano de Nascimento: '))
i = datetime.date.today().year - a
if i < 18:
    print('Ainda vai se alistar')
    print('Tempo: {} anos'.format(18 - i))
elif i == 18:
    print('Hora de se alistar')
else:
    print('Passou do tempo')
    print('Tempo: {} anos'.format(i - 18))
