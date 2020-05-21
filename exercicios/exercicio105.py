def notas(*n, situação=False):
    """
    -> Analisa as notas
    :param *n: notas
    :param situação: (opcional) se quer ver a situação
    :return: dicionário com informações das notas
    """
    r = dict()
    ma = 0
    me = 0
    i = 0
    m = 0
    for l in n:
        if i == 0:
            ma = me = l
            i = 1
        elif l > ma:
            ma = l
        elif l < me:
            me = l
        m += l
    r = {'total':len(n),
         'maior':ma,
         'menor':me}
    if situação:
        if m < 4:
            s = 'REPROVADO'
        elif m < 6:
            s = 'RECUPERAÇÃO'
        else:
            s = 'APROVADO'
        r['situação'] = s
    return r
#  Programa principal
