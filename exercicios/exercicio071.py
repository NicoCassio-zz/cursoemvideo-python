p = int(input('Valor: R$ '))
c = 50
t = 0
while True:
    if p >= c:
        p -= c
        t += 1
    else:
        if t > 0:
            print(f'{t} x R$ {c:.2f}')
            t = 0
        if c == 50:
            c = 20
        elif c == 20:
            c = 10
        elif c == 10:
            c = 1
        if p == 0:
            break
