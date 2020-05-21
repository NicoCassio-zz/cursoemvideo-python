p = float(input('Peso: '))
a = float(input('Altura: '))
imc = p / (a ** 2)
if imc < 18.5:
    s = 'Abaixo do peso'
elif imc < 25:
    s = 'Peso ideal'
elif imc < 30:
    s = 'Sobrepeso'
elif imc < 40:
    s = 'Obsidade'
else:
    s = 'Obesidade mórbida'
print('Situação: {}'.format(s))
