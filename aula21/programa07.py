def par(n=0):
    """
    -> Verifica se um número é par
    :param n: número
    """
    if n % 2 == 0:
        return 'SIM'
    return 'NÃO'
#  Programa principal
print(f'Par: {par(int(input("Número: ")))}')
