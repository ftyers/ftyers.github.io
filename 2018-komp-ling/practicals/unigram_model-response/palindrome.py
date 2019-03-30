freq = []
file = open('freq.txt', 'r', encoding='utf8')
for line in file.readlines():
	line = line.strip()
	(f,w) = line.split('\t')
	freq.append((int(f),w))
file.close()

'''
for i in freq:
	palindrome = False
	rev = ''
	if len(i[1]) == 1:
		continue
	for j in range(1, len(i[1]) + 1):
		rev = rev + i[1][-j]
	if i[1] == rev: 
		palindrome = True 

	if palindrome:
		print('%d\t%s' % (i[0], i[1]))
'''

def is_palindrome(s):
	"""Return True if the given string is a palindrome."""
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