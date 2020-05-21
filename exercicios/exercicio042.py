r1 = int(input('Reta 1: '))
r2 = int(input('Reta 2: '))
r3 = int(input('Reta 3: '))
p = True
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    if r1 == r2 and r1 == r3:
        print('Triângulo equilátero')
    elif r1 == r2 or r1 ==r3 or r2 == r3:
        print('Triângulo isóceles')
    else:
        print('Triângulo escaleno')
else:
    print('Não é triângulo')
