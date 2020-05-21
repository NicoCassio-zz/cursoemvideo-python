try:
    r = int(input('Numerador: ')) / int(input('Denominador: '))
except Exception as erro:
    print(f'Problema encontrado: {erro.__class__}')
else:
    print(f'Resultado: {r}')
finally:
    print('FIM')
