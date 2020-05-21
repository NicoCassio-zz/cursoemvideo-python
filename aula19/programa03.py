locadora = list()
for i in range(0, 3):
    locadora.append({'titulo':str(input('Título: ')),
                     'ano':int(input('Ano: ')),
                     'diretor':str(input('Diretor: '))})
for i, d in enumerate(locadora):
    print('-' * 40)
    print()
    print(f'{f"Filme {i + 1}":^40}')
    print()
    print('-' * 40)
    for k, v in d.items():
        print(f'Key {k:<15} Valor: {v}')
