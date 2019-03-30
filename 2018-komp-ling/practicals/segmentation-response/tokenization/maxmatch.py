import sys

final_list=[]
def maxmatch(sentence, dictionary):
    global final_list
    if len(sentence) == 0:
        return 'Empty list.'
    for i in range(len(sentence), -1, -1):
        firstword = sentence[0:i]
        remainder = sentence[i:]
        if firstword in dictionary:
            final_list.append(firstword)
            return maxmatch(remainder, dictionary)
        if i == 1:
            firstword = sentence[0]
            remainder = sentence[1:]
            final_list.append(remainder)
            final_list.append(firstword)

def main():
	
    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        dictionary = [l.strip('\n') for l in f]
		
    global final_list
    results = []

    for sentence in open(sys.argv[2], 'r', encoding='utf-8'):
        maxmatch(sentence, dictionary)
        results.append(final_list)
        final_list=[]

    output = open("maxmatch_results.txt", 'w', encoding='utf-8')
    for i in results:
        output.write(' '.join(i))
    output.close()

main()