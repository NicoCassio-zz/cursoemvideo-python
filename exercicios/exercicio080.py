l = list()
for i in range(0, 5):
    n = int(input('Número: '))
    if i == 0 or n > l[-1]:
        l.append(n)
    else:
        for x in l:
            if n <= x:
                l.insert(l.index(x), n)
                break
print(l)
