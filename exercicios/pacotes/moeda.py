def aumentar(n=0, f=False):
    """
    -> Aumenta um número em uma unidade
    :param n: número
    :param f: (opcional) formatação de moeda
    :return: número aumentado
    """
    r = n + 1
    if f:
        return moeda(r)
    return r
def diminuir(n=0, f=False):
    """
    -> Diminui um número em uma unidade
    :param n: número
    :param f: (opcional) formatação de moeda
    :return: número diminuido
    """
    r = n - 1
    if f:
        return moeda(r)
    return r
def dobro(n=0, f=False):
    """
    -> Calcula o dobro de um número
    :param n: número
    :param f: (opcional) formatação de moeda
    :return: dobro do número
    """
    r = n * 2
    if f:
        return moeda(r)
    return r
def metade(n=0, f=False):
    """
    -> Calcula a metade de um número
    :param n: número
    :param f: (opcional) formatação de moeda
    :return: metade do número
    """
    r = n / 2
    if f:
        return moeda(r)
    return r
def moeda(n=0):
    """
    -> Formata um número como moeda
    :param n: número
    :return: número formatado
    """
    return f'R$ {n:.2f}'
def resumo(n=0):
    """
    -> Exibe um resumo geral de um valor
    :param n: valor
    """
    print('-' * 40)
    print(f'{"RESUMO":^40}')
    print('-' * 40)
    print(f'{"Preço:":<30}{moeda(n):<10}')
    print(f'{"Aumentado:":<30}{aumentar(n, True):<10}')
    print(f'{"Dimiuido:":<30}{diminuir(n, True):<10}')
    print(f'{"Dobro:":<30}{dobro(n, True):<10}')
    print(f'{"Metade":<30}{metade(n, True):<10}')
    print('-' * 40)
