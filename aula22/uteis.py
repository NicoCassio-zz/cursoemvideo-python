def fatorial(n=1):
    """
    -> Calcula o fatorial de um número
    :param n: número
    :return: fatorial do número
    """
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f
def dobro(n=0):
    """
    -> Calcula o dobro de um número
    :param n: número
    :return: dobro do número
    """
    return n * 2
def triplo(n=0):
    """
    -> Calcula o triplo de um número
    :param n: número
    :return: triplo do número
    """
    return n * 3
