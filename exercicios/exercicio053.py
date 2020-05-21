f = str(input('Digite uma frase: ')).replace(' ', '').lower()
p = True
for i in range(0, len(f)):
    if f[i] != f[len(f) - i - 1]:
        p = False
if p:
    print('Palíndromo!!')
else:
    print('Normal...')
