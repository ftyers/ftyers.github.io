

```python
def go_over_dict_val(dic):
    keys = []
    vals = []
    for k, v in dic.items():
        #print(k, v)
        keys.append(k)
        vals.append(v)
    return keys, vals

def tags_calc(tags):
    units = []
    tokens_count = sum(tags.values())
    for k, v in tags.items():
        p = v/tokens_count
        unit = [str(round (p,2)), str (v), k, '-']
        units.append(unit)
    return units

def word_calc(word_tag):
    units = []
    for k, v in word_tag.items():
        if(len(v) == 1):
            tag, tag_freq = go_over_dict_val(v)
            unit = ['1.00', str (tag_freq[0]), tag[0], k]
            units.append(unit)
            #print(unit)
        elif(len(v) > 1):
            tag, tag_freq = go_over_dict_val(v)
            p_lict = []
            p_sum = 0
            for p_ind in range(len(v)):
                p_lict.append(tag_freq[p_ind])
                p_sum += tag_freq[p_ind]
            for calc_p_ind in range(len(v)):
                p_lict[calc_p_ind] /= p_sum
            for ind in range(len(v)):
                unit = [str(p_lict[ind]),str (tag_freq[ind]),tag[ind],k]
                units.append(unit)
    return  units

test_conllu = 'C://input/rus_tag.conluu'
output_file = "C://input/unigam//unigram.txt"
with open(test_conllu, "r", encoding = 'utf-8') as data:
    tokens_read = 0 
    tags_freq = {}
    word_tag = {}
    #collect possible tags
    for read_tag in data:
        row = read_tag.split('\t')
        
        if(str(row[0]).isdigit()):
            word = row[1]
            tag = row[3]
            if(tag not in tags_freq):
                tags_freq[tag] = 1
            else:
                tags_freq[tag] += 1
            
            if(word in word_tag):
                if(tag not in word_tag[row[1]]):
                    word_tag[word]
                    word_tag[word][tag] = 1
                else:
                    word_tag[word][tag] += 1
            else:
                word_tag[word] = {}
                word_tag[word] [tag] = 1

            tokens_read += 1
    tag_units = tags_calc(tags_freq)
    word_units = word_calc(word_tag)
    output_units = tag_units + word_units
     
    with open(output_file, "w+", encoding = 'utf-8') as data:  
        data.write("# P	count	tag	form\n")
        for un in output_units:
            data.write(un[0] + '\t'+ un[1] + '\t' + un[2] + '\t' + un[3] + '\n')

```
