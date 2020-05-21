def leiaDinheiro(t=''):
    """
    -> Lẽ e valida um número
    :param t: texto exibido na tela
    """
    while True:
        n = str(input(t))
        if n.replace(',', '.').isnumeric():
            return float(n)
        print('ERRO')
