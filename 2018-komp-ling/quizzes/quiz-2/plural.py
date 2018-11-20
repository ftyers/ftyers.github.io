import sys

soft1 = ['ch', 'sh', 'tz']
soft2 = 'sx'
vowels = 'aeiou'

for word in sys.stdin.read().split('\n'):
    word = word[0:-4]
    if word[-2:] in soft1 or word[-1] in soft2 and word[-2] in vowels:
        print(word + 'es')
    else:
        print(word + 's')


