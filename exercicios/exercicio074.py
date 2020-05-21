import random
n = (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10))
print(n)
print(f'Maior: {sorted(n)[-1]}')
print(f'Menor: {sorted(n)[0]}')
