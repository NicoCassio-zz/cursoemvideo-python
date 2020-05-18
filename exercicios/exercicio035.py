r1 = int(input('Reta 1: '))
r2 = int(input('Reta 2: '))
r3 = int(input('Reta 3: '))
p = True
if r1 + r2 < r3:
    p = False
if r1 + r3 < r2:
    p = False
if r3 + r2 < r1:
    p = False
if p:
    print('Pode!! :D')
else:
    print('Não pode...')
