# coding: utf-8

import sys

def get_tags(m):
    
    max_tag_count = 0
    max_tag = ''
    d_word_all_tags = {}
    d_word_max_tag = {}

    for line in m.readlines()[1:]:
        p, count, tag, form = line.split('\t')
        if int(count) > max_tag_count:
            max_tag_count = int(count)
            max_tag = tag
        else:
            value = (float(p), tag)
            if form.strip() in d_word_all_tags:
                d_word_all_tags[form.strip()].append(value)
            else:
                d_word_all_tags[form.strip()] = [value]
        
    for form in d_word_all_tags:
        max_value = max(tag[0] for tag in d_word_all_tags[form])
        for tag in d_word_all_tags[form]:
            if tag[0] == max_value:
                d_word_max_tag[form] = tag[1]
            
    return max_tag, d_word_max_tag

            

def predict_tags(text, new_text, max_tag, d_word_max_tag):
    for line in text.readlines():
        if '\t' not in line:
            new_text.write(line)
        if '\t' in line:
            line = line.split('\t')
            form = line[1].lower()
            if form in d_word_max_tag:
                line[3] = d_word_max_tag[form]
            else:
                line[3] = max_tag
            line_new = '\t'.join(map(str,line))
            new_text.write(line_new)
           
    text.close()
    new_text.close()
    
def main():
    model = open(sys.argv[1], 'r')
    max_tag, d_word_max_tag = get_tags(model)
    text = open(sys.argv[2], 'r')
    new_text = open(sys.argv[3], 'w')
    result = predict_tags(text, new_text, max_tag, d_word_max_tag)
    
if __name__ == '__main__':
    main()

