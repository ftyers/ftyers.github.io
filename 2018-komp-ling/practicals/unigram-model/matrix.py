import sys


rus = ['бы', 'вас', 'видит', 'всего', 'вы']
eng = ['a', 'absorbed', 'all', 'and', 'another']

m = {}

for wl in rus:
    if wl not in m:
        m[wl] = {}
    for w2 in eng:
        m[wl][w2] = 0

print('\t' + '\t'.join(eng))

for wl in m:
    print('%s\t' % (wl), end='')
    for w2 in m[wl]:
        print('%d\t' % (m[wl][w2]), end='')
    print('')
