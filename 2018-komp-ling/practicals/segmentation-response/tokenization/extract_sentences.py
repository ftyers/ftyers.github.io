data = input("Enter name of the test file: ")
sentences = []
reference_sentences = []
print_count = 0
with open(data, "r", encoding = 'utf-8') as data:
    parsed_sentence = [] 
    for line in data:
        row = line.split('\t')
        if('# text = ' in row[0]):
            sentences.append(row[0][9:-1])
        if(str(row[0]).isdigit()):
            parsed_sentence.append(row[1])
        else:
            if parsed_sentence:
                reference_sentences.append(' '.join(parsed_sentence))
            parsed_sentence = []

sent = open("sentences.txt", "w+", encoding="utf-8")
for line in sentences:
	sent.write(line+'\n')
sent.close()

ref_sent = open("reference_sentences.txt", "w+", encoding="utf-8")
for line in reference_sentences:
	ref_sent.write(line+'\n')
ref_sent.close()