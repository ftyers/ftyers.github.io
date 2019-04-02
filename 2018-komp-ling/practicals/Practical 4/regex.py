import re

s = 'Привет мир!'
re.search(r'м[а-я]+', s)
m = re.search(r'м[а-я]+', s)
print(m.group())
print(m.span())
