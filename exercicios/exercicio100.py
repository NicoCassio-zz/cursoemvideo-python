import random
def sorteia(n):
    for i in range(0, 5):
        n.append(random.randint(1, 10))
    print('Valores: ', end='')
    for i in n:
        print(i, end=' ')
    print()
def somaPar(n):
    s = 0
    for i in n:
        if i % 2 == 0:
            s += i
    print(f'Soma dos pares: {s}')
#  Programa principal
números = list()
sorteia(números)
somaPar(números)
