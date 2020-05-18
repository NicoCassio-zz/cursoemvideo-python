f = str(input('Digite uma frase: '))
print('Quantiade de Rs: {}'.format(f.upper().count('R')))
print('Primeiro R: {}'.format(f.upper().find('R') + 1))
print('Último R: {}'.format(f.upper().rfind('R') + 1))
