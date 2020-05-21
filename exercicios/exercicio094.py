lista = list()
listaM = list()
listaI = list()
m = 0
while True:
    lista.append({'nome':str(input('Nome: ')),
                  'idade':int(input('Idade: ')),
                  'sexo':str(input('Sexo [m/f]: '))})
    m += lista[-1]['idade']
    op = ' '
    while op not in 'sn':
        op =str(input('Quer continuar? [s/n]')).lower()[0]
    if op == 'n':
        break
m /= len(lista)
print('-' * 45)
print(f'{"GERAL":^45}')
print('-' * 45)
print(f'Total: {len(lista)}')
print(f'Média: {m:.1f}')
for i in lista:
    if i['sexo'] == 'f':
        listaM.append(i)
    if i['idade'] > m:
        listaI.append(i)
print('-' * 45)
print(f'{"MULHERES":^45}')
print('-' * 45)
for i in listaM:
    for k, v in i.items():
        print(f'{f"{k.capitalize()}: {v}":<15}', end='')
    print()
print('-' * 45)
print(f'{"ACIMA DA MÉDIA":^45}')
print('-' * 45)
for i in listaI:
    for k, v in i.items():
        print(f'{f"{k.capitalize()}: {v}":<15}', end='')
    print()
