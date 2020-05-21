pares = list()
impares = list()
l = list()
for i in range(0, 7):
    n = int(input('Número: '))
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
l.append(pares[:])
l.append(impares[:])
l[0].sort()
l[1].sort()
print(f'Pares: {l[0]}')
print(f'Ímpares: {l[1]}')
