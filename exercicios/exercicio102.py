def fatorial(número=1, show=True):
    """
    -> Calcula o fatorial de um número mostrando na tela
    :param n: número
    :param show: (opcional) mostra ou não a conta
    """
    f = 1
    s = ''
    for i in range(número, 0, -1):
        f *= i
        if show:
            if i != 1:
                s += f'{i} x '
            else:
                s += f'{i} = '
    if not show:
        return f
    return s + str(f)
#  Programa principal
print(f'Fatorial: {fatorial(int(input("Número: ")), True if str(input("Mostrar conta: [s/n] ").lower()[0]) == "s" else False)}')
