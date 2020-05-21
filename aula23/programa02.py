try:
    r = int(input('Numerador: ')) / int(input('Denominador: '))
except ValueError:
    print('Digite um número...')
except ZeroDivisionError:
    print('Nunca dividirás por zero...')
except Exception as erro:
    print(f'Problema encontrado: {erro.__cause__}')
else:
    print(f'Resultado: {r}')
finally:
    print('FIM')
