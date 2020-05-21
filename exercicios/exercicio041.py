import datetime
a = int(input('Ano de Nascimento: '))
i = datetime.date.today().year - a
if i < 9:
    c = 'MIRIM'
elif i < 14:
    c = 'INFANTIL'
elif i < 19:
    c = 'JUNIOR'
elif i < 20:
    c = 'SÊNIOR'
else:
    c = 'MASTER'
print('Categoria: {}'.format(c))
