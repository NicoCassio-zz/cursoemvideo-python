lista = ('porta', 'janela', 'cortina', 'maçaneta', 'vidro')
for p in lista:
    print(p, end  = ' ')
    for l in p:
        if l in 'aeiou':
            print(f'{l} ', end = ' ')
    print()
