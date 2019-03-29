#!/usr/bin/python

import sys, getopt

def main(argv):
    inputfile = ''
    outputfile = '__translitareted.conllu'
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print('test.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print( 'test.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    print( 'Input file is:', inputfile)
    print( 'Output file is:', outputfile)
    
    vocab = []
    test = open(inputfile,'r',encoding='utf8') 
    for line in test.readlines():
        if '\t' not in line:
            continue
        row = line.replace('\n','').split('\t')
        if len(row) != 10:
            continue
        vocab.append(row)
    test.close()  
    
    #magic KOI-8r
    for i in enumerate(vocab):
        try:
            oldone = i[1][1].encode('koi8-r')
            newone = ''.join([chr(c & 0x7F) for c in oldone])
            vocab[i[0]][9] = newone
        except:
            continue
              
    with open(outputfile, 'w+',encoding='utf8') as fd:
        for w in vocab:
            fd.write('\t'.join(w)+'\n')
              
if __name__ == "__main__":
    main(sys.argv[1:])
