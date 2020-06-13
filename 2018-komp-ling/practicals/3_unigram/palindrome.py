
def is_palindrome(s):
    revers = ''
    if len(s) == 1:
        return False
    for i in range(1, len(s) + 1):
        revers += s[-i]
    if s == revers:
        return True
    else:
        return False

freq = open('text.txt').readlines()

for i in freq:
    line = [k.strip('\n').lower() for k in i.split('\t')]
    #print (line)
    if is_palindrome(line[1]) == True:
        print ('{}\t{}'.format(line[0], line[1]))
