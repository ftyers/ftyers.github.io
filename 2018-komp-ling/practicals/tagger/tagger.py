#!/usr/bin/python3
# -*- coding: utf-8 -*-
import csv
import sys
import io
from io import StringIO

if len(sys.argv) > 1:
    with open(sys.argv[1], 'r', encoding="UTF-8") as model:
        reader = csv.reader(model, delimiter='\t')
        next(reader, None)  # skip the headers
        pos = {}
        lex  = {}
        probs = {}
        for a in reader:
            if a[3] == "–" and a[2] != "PUNCT":
                pos[a[2]] = a[0]
            else:
                if a[3] in probs:
                    if probs[a[3]] < a[0]:
                        probs[a[3]] = a[0]
                        lex[a[3]] = a[2]
                else:
                    lex[a[3]] = a[2]
                    probs[a[3]] = a[0]
        defpos  = max(pos, key=pos.get)
        input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
        for x in input_stream.readlines():
            x  = x.rstrip()
            if x[0] == "#": # it is a comment line
                print(x)
            else:
                inputio = StringIO(x)
                r2 = csv.reader(inputio, delimiter='\t')
                row  = next(r2) 
                token = row[1]
                pos  = defpos
                row[3] = lex[token] if token in lex else defpos
                print("\t".join(row))