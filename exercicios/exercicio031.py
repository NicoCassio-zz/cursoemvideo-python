d = float(input('Distância: '))
print('Preço: R$ {:.2f}'.format(d * (0.5 if d <= 200 else 0.45)))
