l = ('Pão', 1, 'Caneta', 1.5, 'Caderno', 12, 'Notebook', 1500)
for i in range(0, len(l), 2):
    print(f'{l[i]}..R$ {l[i + 1]:.2f}')
