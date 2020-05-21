n = int(input('Número: '))
i = 0
a = 0
b = 1
print(a)
print(b)
while i < n - 2:
    t = a + b
    a = b
    b = t
    print(t)
    i += 1
