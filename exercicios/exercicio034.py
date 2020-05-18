s = float(input('Salário: '))
print('Aumento: {:.2f}'.format(s * (0.1 if s > 1250 else 0.15)))
