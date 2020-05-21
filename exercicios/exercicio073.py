times = ('flamengo', 'santos', 'palmeiras', 'grêmio', 'athletico-pr', 'são paulo', 'internacional', 'corinthians', 'fortaleza ec', 'goiás', 'bahia', 'vasco da gama', 'atlético-mg', 'fluminense', 'botafogo', 'ceará', 'cruzeiro', 'csa', 'chapecoense', 'avaí')
for t in times[:5]:
    print(t)
for t in times[-4:]:
    print(t)
print(sorted(times))
p = times.index('chapecoense') + 1
print(f'Chapecoense: {p}')
