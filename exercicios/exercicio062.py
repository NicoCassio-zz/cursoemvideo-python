t = int(input('Primeiro termo: '))
r = int(input('Razão: '))
i = 0
n = 10
a = -1
while a != 0:
    while i < n:
        print('{}'.format(t))
        t += r
        i += 1
    a = int(input('Quantos mais: '))
    n += a
