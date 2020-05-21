s = 0
t = 0
while True:
    n = int(input('Número: '))
    if n == 999:
        break
    s += n
    t += 1
print(f'Soma: {s}')
print(f'Total: {t}')
