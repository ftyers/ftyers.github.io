import sys

def strip_html(h):
        o = ''
        inTag = False
        for c in h: 
                if c == '<':
                        inTag = True
                        continue
                if c == '>':
                        inTag = False
                        continue
                if not inTag:
                        o = o + c
        return o

stem = '_'
zkod = '_'
ipa = '_'
h1 = '_'
for line in sys.stdin.readlines(): 
        if line.count('<h1>') > 0:
                h1 = strip_html(line)

        if h1.strip() != 'Русский':
                continue
        line = line.strip()
        text = strip_html(line);

        if text.count('Корень:') > 0:
                stem = text.split(':')[1].strip('.')
                if "окончание" in stem:
                        stem = stem.split(";")[0]
        if text.count('МФА') > 0:
                ipa = text.split('[')[1].split(']')[0]
        if text.count('тип склонения') > 0:
                zkod = text.split('тип склонения')[1].strip().split(' ')[0].strip("^")

        if stem != '_' and zkod != '_' and ipa != '_':
                print('%s\t%s\t%s' % (stem, zkod, ipa))
                stem = '_'
                zkod = '_'
                ipa = '_'