n = list()
for i in range(0, 5):
    n.append(int(input(f'Número {i + 1}: ')))
    if i == 0:
        ma = me = n[i]
    elif n[i] > ma:
        ma = n[i]
    elif n[i] < me:
        me = n[i]
print(f'Maior: {ma}[{n.index(ma) + 1}]')
print(f'Menor: {me}[{n.index(me) + 1}]')
