#!/usr/bin/python

import sys, getopt

def main(argv):
    inputfile = ''
    outputfile = 'ranked.txt'
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
    
    freq = []
    with open(inputfile, 'r',encoding='utf8') as fd:
        for line in fd.readlines():
            line = line.strip('\n')
            (f, w) = line.split('\t')
            freq.append((int(f), w)) 
    rank = 1
    min = freq[0][0]
    ranks = []
    for i in range(0, len(freq)): 
        if freq[i][0] < min: 
            rank = rank + 1
            min = freq[i][0]
        ranks.append((rank, freq[i][0], freq[i][1]))   
              
    with open(outputfile, 'w+',encoding='utf8') as fd:
        for w in vocab:
            fd.write(ranks)
              
if __name__ == "__main__":
    main(sys.argv[1:])
