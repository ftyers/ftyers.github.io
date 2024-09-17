import scipy.linalg as sp
from math import sqrt
import numpy
import re


def open_conllu(pathtofile):
    with open(pathtofile, encoding="utf-8") as r:
        listsents = []
        listrow = []
        listwords = []
        listword = []
        file = r.readlines()
        for line in file:
            if re.sub(r"^([0-9]+)\t.+\n$", r"\1", line) is "1":
                if listrow != []:
                    listsents.append(listrow)
                    listwords.append(listword)
                    listrow = []
                    listword = []
            if re.sub(r"^([0-9]+)\t.+\n$", "", line) is "":
                row_num = re.sub(r"^([0-9]+)\t.+?\t.+?\t.+?\t.+?\t.+?\t([0-9]+)\t.+\n$", r"\1", line)
                row_vec = re.sub(r"^([0-9]+)\t.+?\t.+?\t.+?\t.+?\t.+?\t([0-9]+)\t.+\n$", r"\2", line)
                word = re.sub(r"^[0-9]+\t(.+?)\t.+?\t.+?\t.+?\t.+?\t[0-9]+\t.+\n$", r"\1", line)
                listrow.append((int(row_num) - 1, int(row_vec) - 1))
                listword.append(word)
        if listrow != []:
            listsents.append(listrow)
            listwords.append(listword)
        return listsents, listwords


def boundary_creator(vertex, edges):
    boundary = []
    for v in vertex:
        newboundary = []
        for e in edges:
            newboundary.append(1 if e[1] == v else -1 if e[0] == v else 0)
        boundary.append(newboundary)
    return boundary


"""CYCLE CHECKING AND REDUCTION: this part checks through nullspace if there is any cycle first. If nullspace sum is \
not 0, we do have cycles.Then takes any row and checks which row receives more than one edge. Takes the index of the \
starting vertex of the edges, and check which of the vertexes has more weight in the nullspace calculus. The one \
starting from the most weighted vertex then gets reduced and the nullspace is updated dinamically. The cycle repeats \
until the nullspace sum returns 0"""


def cycle_reductioner(boundary):
    boundarynull = sp.null_space(boundary)
    boundarynull = boundarynull * -sqrt(2)
    while numpy.sum(boundarynull) != 0 and len(boundarynull) != 0:
        listall = []
        for row in boundary:
            newlist = []
            if row.count(1) > 1:
                for index, number in enumerate(row):
                    if number == 1:
                        newlist.append(index)
                listall.append(newlist)
        for list in listall:
            maxvalue = 0
            maxindex = 0
            for index in list:
                value = abs(boundarynull[index][0])
                if value > maxvalue:
                    maxvalue = value
                    maxindex = index
        for row in boundary:
            if row.count(1) > 1:
                if row[maxindex] == 1:
                    row[maxindex] = 0
            if row[maxindex] == -1:
                row[maxindex] == 0
        boundarynull = sp.null_space(boundary)
        boundarynull = boundarynull * -sqrt(2)
    return boundary


def alg_return(reduced_object, words):
    sentence = []
    for word in reduced_object:
        verts = []
        wordsverts = []
        origin = word.index(-1)
        for i, x in enumerate(word):
            if x == 1:
                verts.append(i)
        for x in verts:
            wordsverts.append(words[x])
        sentence.append((words[origin], wordsverts))
    return sentence

if __name__=="__main__":
    doc, words = open_conllu("paragraph.conllu")
    finallist = []
    for i, sent in enumerate(doc):
        wordings = words[i]
        vertex = range(len(sent))
        edges = sent
        # vertex = [0, 1, 2, 3, 4, 5, 6]
        # edges = [[0, 1], [1, 3], [2, 3], [3, 4], [4, 6], [5, 6], [6, 1]]
        finallist.append(alg_return(cycle_reductioner(boundary_creator(vertex, edges)), wordings))
    print(finallist)
