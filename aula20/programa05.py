def dobra(l):
    for i in range(0, len(l)):
        l[i] *= 2
    print(f'Lista em dobro: {l}')
#  Programa principal
v= [1, 2, 3, 4, 5]
print(f'Lista: {v}')
dobra(v)
