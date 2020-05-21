def leiaInt(t):
    """
    -> Lê um número, se não for número, retorna 0
    :param t: texto mostrado antes de ler o número
    :return: número lido
    """
    while True:
        n = str(input(t))
        if n.isnumeric():
            break
        print('ERRO')
    return int(n)
#  Programa principal
print(f'Digitado: {leiaInt("Número: ")}')
