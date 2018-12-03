import sys

rus = ['бы', 'вас', 'видит', 'всего', 'вы']
eng = ['a', 'absorbed', 'all', 'and', 'another']

m = {}

for w1 in rus:
	if w1 not in m:
		m[w1] = {}
	for w2 in eng:
		m[w1][w2] = 0


print('\t' + '\t'.join(eng))
for w1 in m:
    print('%s\t' % (w1), end='')
    for w2 in m[w1]:
            print('%d\t' % (m[w1][w2]), end='')
    print('')

