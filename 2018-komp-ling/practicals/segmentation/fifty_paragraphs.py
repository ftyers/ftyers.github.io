wiki = open('fifty.txt')

# f = open('fifty.txt', 'w')

a = wiki.read()

print (a)

b = a.split('\n')

print (len(b))
