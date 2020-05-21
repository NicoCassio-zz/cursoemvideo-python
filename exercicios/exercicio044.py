p = float(input('Preço: R$ '))
print('-----------------------')
print('{:^22}'.format('Método de Pagamento'))
print('-' * 22)
print('  [1] Dinheiro/Cheque  ')
print('  [2] Cartão à vista   ')
print('  [3] 2x Cartão       ')
print('  [4] 3x ou mais cartão')
print('-' * 22)
op = int(input(' Opção: '))
if op == 1:
    v = 0.9 * p
elif op == 2:
    v = 0.95 * p
elif op == 3:
    v = p
elif op == 4:
    v = 1.2 * p
else:
    v = '[OPÇÃO INVÁLIDA]'
print('Preço final: {}'.format(v))
