v = float(input('Velocidade: '))
if v > 80:
    print('M U T A D O')
    print('Valor: R$ {:.2f}'.format((v - 80) * 7))
