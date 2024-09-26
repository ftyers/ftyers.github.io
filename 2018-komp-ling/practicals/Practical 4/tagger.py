import sys


def process_model(model):
    max_freq = 0
    m_f_tag = ''
    d = {}
    for line in model.readlines()[1:]:
        p, freq, tag, word = line.split('\t')
        if '-' in line:     # finding the most frequent tag
            if int(freq) > max_freq:
                max_freq = int(freq)
                m_f_tag = tag.strip()
        else:
            val = d.setdefault(word.lower().strip(), [])
            val.append((float(p), tag.strip()))
    return m_f_tag, d


def predict(sent, m_f_tag, d):
    for line in sent.readlines():
        if '\t' in line:
            line = line.split('\t')
            word = line[1].lower()
            if word in d:
                max_p = max([i[0] for i in d[word]])
                for t in d[word]:
                    if t[0] == max_p:
                        tag = t[1]
            else:
                tag = m_f_tag
            line.insert(2, tag)
            print('\t'.join(line).strip())


def main():
    with open(sys.argv[1], 'r', encoding='utf-8') as m:
        m_f_tag, d = process_model(m)
    with open(sys.argv[2], 'r', encoding='utf-8') as f:
        print(predict(f, m_f_tag, d))


if __name__ == '__main__':
    main()