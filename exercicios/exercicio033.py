n1 = int(input('Número 1: '))
n2 = int(input('Número 2: '))
n3 = int(input('Número 3: '))
if n1 > n2:
    m = n1
else:
    m = n2
if n3 > m:
    m = n3
print('Maior: {}'.format(m))
