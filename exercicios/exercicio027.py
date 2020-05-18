n = str(input('Nome Completo: ')).strip()
print('Primeiro nome: {}'.format(n.split()[0]))
print('Último nome: {}'.format(n.split()[len(n.split()) - 1]))
