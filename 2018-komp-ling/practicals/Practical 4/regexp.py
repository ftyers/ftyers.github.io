import re

s = 'Привет мир!'

print(re.search(r'м[а-я]+', s))

m = re.search(r'м[а-я]+', s)
print(m.group())
print(m.span())

print(re.sub('[а-я]', 'x', s))