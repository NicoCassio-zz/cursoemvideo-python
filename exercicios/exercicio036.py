v = float(input('Valor: R$ '))
s = float(input('Salário: R$ '))
a = int(input('Anos: '))
p = v / (a * 12)
if p > (0.3 * s):
    print('Empréstimo NEGADO...')
else:
    print('Prestação: R$ {:.2f}'.format(p))
