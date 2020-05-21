import datetime
def voto(a=2020):
    """
    -> Verifica a idade e retorna a situação de voto
    :param a: ano de nascimento
    """
    i = datetime.date.today().year - a
    if i < 16:
        return 'NEGADO'
    elif i < 18 or i > 65:
        return 'OPCIONAL'
    return 'OBRIGATÓRIO'
#  Programa principal
print(f'Voto: {voto(int(input("Ano de Nascimento: ")))}')
