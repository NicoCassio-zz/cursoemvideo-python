n = int(input('Número: '))
print('-------------------')
print('  [1] binário      ')
print('  [2] octal        ')
print('  [3] hexadecimal  ')
print('-------------------')
op =int(input(' Opção: '))
if op == 1:
    print('Binário: {}'.format(bin(n)[2:]))
elif op == 2:
    print('Octal: {}'.format(oct(n)[2:]))
elif op == 3:
    print('Hexadecimal: {}'.format(hex(n)[2:]))
else:
    print('Opção inválida...')
