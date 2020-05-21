p = 0
n1 = int(input('Número 1: '))
n2 = int(input('Número 2: '))
n3 = int(input('Número 3: '))
n4 = int(input('Número 4: '))
n = (n1, n2, n3, n4)
for i in n:
    if i % 2 == 0:
        p += 1
print(f'9: {n.count(9)}')
print(f'3: {n.index(3)}')
print(f'Pares: {p}')
