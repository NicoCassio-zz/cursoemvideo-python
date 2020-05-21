maioridade = 0
homens = 0
mulheres = 0
while True:
    i = int(input('Idade: '))
    s = str(input('Sexo [m/f]: ')).lower()
    if i >= 18:
        maioridade += 1
    if s == 'm':
        homens += 1
    elif s == 'f' and i < 20:
        mulheres += 1
    else:
        print('Sexo inválido')
    op = str(input('Quer continuar [s/n] ')).lower()
    if op == 'n':
        break
print(f'Maiores: {maioridade}')
print(f'Homens: {homens}')
print(f'Mulheres jovens: {mulheres}')
