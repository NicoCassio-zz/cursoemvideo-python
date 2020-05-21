def fatorial(n=1):
    """
    -> Calcúla o fatorial de um número e o retorna
    :param n: número
    """
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f
#  Programa principal
print(f'Fatorial: {fatorial(int(input("Número: ")))}')
