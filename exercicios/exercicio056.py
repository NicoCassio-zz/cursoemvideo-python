soma = 0
m = 0
mulheres = 0
for c in range(0, 4):
    n = str(input('Nome {}: '.format(c + 1))).strip().split()[0].capitalize()
    i = int(input('Idade {}: '.format(c + 1)))
    s = str(input('Sexo {} [m/f] : '.format(c + 1))).lower()
    soma += i
    if i > m and s == 'm':
        maisVelho = n
    if i < 20 and s == 'f':
        mulheres += 1
print('Média: {:.2f}'.format(soma / 4))
print('Mais velho: {}'.format(maisVelho))
print('Mulheres jovens: {}'.format(mulheres))
