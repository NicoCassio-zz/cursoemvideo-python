ma = 0
me = 0
for i in range(0, 5):
    p = float(input('Peso {}: '.format(i + 1)))
    if p > ma:
        ma = p
    elif p < me:
        me = p
print('Maior: {:.1f}'.format(ma))
print('Menor: {:.1f}'.format(me))
