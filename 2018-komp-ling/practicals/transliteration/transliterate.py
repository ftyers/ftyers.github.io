import sys

def translit(word, transl):
    new = ''
    w_new = ''
    for w in word:
        if w in transl:
            w_new = transl[w]
        elif w.lower() in transl:
            w_new = transl[w.lower()].upper()
        else:
            w_new = w
        new += w_new
    return(new)

dict_transl = {}
with open(sys.argv[2], 'r') as f:
	for line in f:
		l = line.strip().split('\t')
		dict_transl[l[0]] = l[1]

with open(sys.argv[1], 'r') as file:
	for line in file:
		if '\t' not in line:
			print(line.strip())
			continue
		row = line.strip().split('\t')
		if len(row) != 10:
			print(line.strip())
			continue
		row[9] = 'Translit='+translit(row[1], dict_transl)
		print(*row, sep = '\t')