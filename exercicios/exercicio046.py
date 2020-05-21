import time
print('CONTAGEM REGRESSIVA:')
for c in range(10, 0, -1):
    print('{}s'.format(c))
    time.sleep(1)
print('*ESTOURO*')
