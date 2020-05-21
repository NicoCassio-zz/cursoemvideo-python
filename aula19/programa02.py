filme = {'titulo':'Star Wars',
         'ano':1977,
         'diretor':'George Lucas'}
print(filme.values())
print(filme.keys())
print(filme.items())
for k, v in filme.items():
    print(f'Key: {k:<15} Valor: {v}')
