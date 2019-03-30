import sys

freq = []

with open(sys.argv[1], 'r', encoding='utf-8') as f:
    for line in f.readlines():
        line = line.strip('\n')
        (f, w) = line.split('\t')
        freq.append((f, w))

def is_palindrome(s):
    rev = ''
    if len(s) == 1:
        return False
    for j in range(1, len(s) + 1):
        rev = rev + s[-j]
    if s == rev:
        return True
    return False


for i in freq:
    if is_palindrome(i[1]):
        print('%d\t%s' % (i[0], i[1]))