
# coding: utf-8

result = open(sys.argv[1], 'r')
correct = open(sys.argv[2], 'r')


def get_tags(file):

    tags = []
    
    for line in file.readlines():
        if '\t' in line:
            line = line.split('\t')
            tag = line[3]
            tags.append(tag)
    return tags    

 
res = get_tags(result)
cor = get_tags(correct)
        
total = 0
correct = 0
for i in range(0, len(res)):
    if res[i] == cor[i]:
        print('+', res[i], cor[i]);
        correct = correct + 1
    else:
        print('-', res[i], cor[i]);
    total = total + 1
print(correct/total)

