while True:
    op = str(input('Digite o comando: [FIM para sair] ')).lower().strip()
    if op == 'fim':
        break
    help(op)
