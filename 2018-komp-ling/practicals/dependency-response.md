# Practical 4
author: Oleg Serikov

**Contents:**
* UDPipe
* Maximal Spanning Tree

click & run code available at (link: https://colab.research.google.com/drive/1580cWwQ2nIz4uKHknf_Nze7p8yJA0Ezv) 

## UdPipe

**Note:** I haven't trained the model myself but it can easily be performed with smth like `udpipe --train model.output [--heldout=heldout_data] training_file ...
` as is shown in the docs. The training data and config for the models used in the practical is provided at (link: https://lindat.mff.cuni.cz/repository/xmlui/handle/11234/1-2898)

---

I was able to make UdPipe working having executed the following code in the google colab (See Pt1 at (link: https://colab.research.google.com/drive/1580cWwQ2nIz4uKHknf_Nze7p8yJA0Ezv))

```
# receive and build udpipe
git clone https://github.com/ufal/udpipe.git
cd udpipe/src
make

# receive the model for the russian lang
wget https://lindat.mff.cuni.cz/repository/xmlui/bitstream/handle/11234/1-2898/russian-syntagrus-ud-2.3-181115.udpipe
mv russian-syntagrus-ud-2.3-181115.udpipe russian-syntagrus.udpipe

# receive the War and Peace text 
# and perform some naive preprocessing
wget https://royallib.com/get/txt/tolstoy_lev/voyna_i_mir_tom_1.zip
unzip voyna_i_mir_tom_1.zip
rm *.url
mv *Лев* voyna_i_mir_tom_1.txt.cp1251
iconv -t UTF-8 -f WINDOWS-1251 voyna_i_mir_tom_1.txt.cp1251 > voyna_i_mir_tom_1.txt
grep -v -P "^\s*$" voyna_i_mir_tom_1.txt > voyna_i_mir_tom_1-pretty.txt

# analyze the text with udpipe
cat voyna_i_mir_tom_1-pretty.txt | ./udpipe --tokenize --tag --parse russian-syntagrus.udpipe > res.res
```

the head of the resulting file looks like this:
```
...
# sent_id = 6
# text = Нет, я вас предупреждаю, если вы мне не скажете, что у нас война, если вы еще позволите себе защищать все гадости, все ужасы этого Антихриста (право, я верю, что он Антихрист) — я вас больше не знаю, вы уж не друг мой, вы уж не мой верный раб, как вы говорите.
1	Нет	нет	PART	_	_	5	parataxis	_	SpaceAfter=No
2	,	,	PUNCT	_	_	1	punct	_	_
3	я	я	PRON	_	Case=Nom|Number=Sing|Person=1	5	nsubj	_	_
4	вас	вы	PRON	_	Case=Acc|Number=Plur|Person=2	5	obj	_	_
5	предупреждаю	предупреждать	VERB	_	Aspect=Imp|Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin|Voice=Act	0	root	_	SpaceAfter=No
6	,	,	PUNCT	_	_	11	punct	_	_
7	если	если	SCONJ	_	_	11	mark	_	_
8	вы	вы	PRON	_	Case=Nom|Number=Plur|Person=2	11	nsubj	_	_
9	мне	я	PRON	_	Case=Dat|Number=Sing|Person=1	11	iobj	_	_
10	не	не	PART	_	_	11	advmod	_	_
11	скажете	сказать	VERB	_	Aspect=Perf|Mood=Ind|Number=Plur|Person=2|Tense=Fut|VerbForm=Fin|Voice=Act	5	advcl	_	SpaceAfter=No
12	,	,	PUNCT	_	_	51	punct	_	_
13	что	что	SCONJ	_	_	51	mark	_	_
14	у	у	ADP	_	_	15	case	_	_
15	нас	мы	PRON	_	Case=Gen|Number=Plur|Person=1	51	nmod	_	_
16	война	война	NOUN	_	Animacy=Inan|Case=Nom|Gender=Fem|Number=Sing	51	obl	_	SpaceAfter=No
17	,	,	PUNCT	_	_	21	punct	_	_
18	если	если	SCONJ	_	_	21	mark	_	_
19	вы	вы	PRON	_	Case=Nom|Number=Plur|Person=2	21	nsubj	_	_
20	еще	еще	ADV	_	Degree=Pos	21	advmod	_	_
21	позволите	позволить	VERB	_	Aspect=Perf|Mood=Imp|Number=Plur|Person=2|VerbForm=Fin|Voice=Act	16	advcl	_	_
22	себе	себя	PRON	_	Case=Dat	21	iobj	_	_
23	защищать	защищать	VERB	_	Aspect=Imp|VerbForm=Inf|Voice=Act	21	xcomp	_	_
24	все	весь	DET	_	Case=Acc|Number=Plur	25	det	_	_
25	гадости	гадость	NOUN	_	Animacy=Inan|Case=Acc|Gender=Fem|Number=Plur	23	obj	_	SpaceAfter=No
26	,	,	PUNCT	_	_	46	punct	_	_
27	все	весь	DET	_	Case=Acc|Number=Plur	28	det	_	_
28	ужасы	ужас	NOUN	_	Animacy=Inan|Case=Acc|Gender=Masc|Number=Plur	46	obj	_	_
29	этого	этот	DET	_	Case=Gen|Gender=Masc|Number=Sing	30	det	_	_
30	Антихриста	Антихристос	PROPN	_	Animacy=Anim|Case=Gen|Gender=Masc|Number=Sing	28	nmod	_	_
31	(	(	PUNCT	_	_	32	punct	_	SpaceAfter=No
32	право	право	NOUN	_	Animacy=Inan|Case=Acc|Gender=Neut|Number=Sing	46	obj	_	SpaceAfter=No
33	,	,	PUNCT	_	_	35	punct	_	_
34	я	я	PRON	_	Case=Nom|Number=Sing|Person=1	35	nsubj	_	_
35	верю	верить	VERB	_	Aspect=Imp|Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin|Voice=Act	32	conj	_	SpaceAfter=No
36	,	,	PUNCT	_	_	39	punct	_	_
37	что	что	SCONJ	_	_	39	mark	_	_
38	он	он	PRON	_	Case=Nom|Gender=Masc|Number=Sing|Person=3	39	nsubj	_	_
39	Антихрист	Антихрист	PROPN	_	Animacy=Inan|Case=Nom|Gender=Masc|Number=Sing	35	ccomp	_	SpaceAfter=No
40	)	)	PUNCT	_	_	32	punct	_	SpacesAfter= 
41	—	—	PUNCT	_	_	32	punct	_	_
42	я	я	PRON	_	Case=Nom|Number=Sing|Person=1	46	nsubj	_	_
43	вас	вы	PRON	_	Case=Acc|Number=Plur|Person=2	46	obj	_	_
44	больше	больше	ADV	_	Degree=Cmp	46	advmod	_	_
45	не	не	PART	_	_	46	advmod	_	_
46	знаю	знать	VERB	_	Aspect=Imp|Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin|Voice=Act	25	acl:relcl	_	SpaceAfter=No
47	,	,	PUNCT	_	_	21	punct	_	_
48	вы	вы	PRON	_	Case=Nom|Number=Plur|Person=2	51	nsubj	_	_
49	уж	уж	PART	_	_	51	advmod	_	_
50	не	не	PART	_	_	51	advmod	_	_
51	друг	друг	NOUN	_	Animacy=Anim|Case=Nom|Gender=Masc|Number=Sing	11	ccomp	_	_
52	мой	мой	DET	_	Case=Nom|Gender=Masc|Number=Sing	51	det	_	SpaceAfter=No
53	,	,	PUNCT	_	_	59	punct	_	_
54	вы	вы	PRON	_	Case=Nom|Number=Plur|Person=2	59	nsubj	_	_
55	уж	уж	PART	_	_	59	advmod	_	_
56	не	не	PART	_	_	57	advmod	_	_
57	мой	мой	DET	_	Case=Nom|Gender=Masc|Number=Sing	59	det	_	_
58	верный	верный	ADJ	_	Case=Nom|Degree=Pos|Gender=Masc|Number=Sing	59	amod	_	_
59	раб	раб	NOUN	_	Animacy=Inan|Case=Nom|Gender=Masc|Number=Sing	5	conj	_	SpaceAfter=No
60	,	,	PUNCT	_	_	63	punct	_	_
61	как	как	SCONJ	_	_	63	advmod	_	_
62	вы	вы	PRON	_	Case=Nom|Number=Plur|Person=2	63	nsubj	_	_
63	говорите	говорить	VERB	_	Aspect=Imp|Mood=Ind|Number=Plur|Person=2|Tense=Pres|VerbForm=Fin|Voice=Act	59	acl	_	SpaceAfter=No
64	.	.	PUNCT	_	_	5	punct	_	_
...
```

## Maximal spanning tree
I implemented the maximal spanning tree search via Prim's algorithm following mostly the EMaxx description (link: http://e-maxx.ru/algo/mst_prim)

execution output examples, then the source code provided below.
click & run code available at Pt2 of (link: https://colab.research.google.com/drive/1580cWwQ2nIz4uKHknf_Nze7p8yJA0Ezv)

### execution examples
#### demo results


```
coincidence weights matrix:
[0, 2, 0, 6, 0]
[2, 0, 3, 8, 5]
[0, 3, 0, 0, 7]
[6, 8, 0, 0, 9]
[0, 5, 7, 9, 0]
minimal spanning tree edges: [(0, 1), (0, 3), (1, 4), (1, 2)] spanning tree weight: 16
maximal spanning tree edges: [(0, 3), (3, 1), (3, 4), (4, 2)] spanning tree weight: 30

coincidence weights matrix:
[0, 2, 0, 6]
[2, 0, 3, 8]
[0, 3, 0, 0]
[6, 8, 0, 0]
minimal spanning tree edges: [(0, 1), (0, 3), (1, 2)] spanning tree weight: 11
maximal spanning tree edges: [(0, 3), (1, 2), (3, 1)] spanning tree weight: 17

coincidence weights matrix:
[1, 1, 1, 1]
[1, 1, 1, 1]
[1, 1, 1, 1]
[1, 1, 1, 1]
minimal spanning tree edges: [(0, 1), (0, 3), (1, 2)] spanning tree weight: 3
maximal spanning tree edges: [(0, 1), (0, 3), (1, 2)] spanning tree weight: 3

coincidence weights matrix:
[1, 2, 3, 4]
[5, 6, 7, 8]
[9, 10, 11, 12]
[13, 14, 15, 16]
minimal spanning tree edges: [(0, 1), (0, 3), (0, 2)] spanning tree weight: 9
maximal spanning tree edges: [(0, 3), (3, 1), (3, 2)] spanning tree weight: 33

coincidence weights matrix:
[0, -202, 3, 4]
[5, 6, 7, 8]
[9, 10, 11, 12]
[13, 14, 15, 16]
minimal spanning tree edges: [(0, 1), (0, 3), (0, 2)] spanning tree weight: -195
maximal spanning tree edges: [(0, 3), (3, 1), (3, 2)] spanning tree weight: 33
```

#### demo code
```python
demonstrate_prim(WeightedGraph([[0, 2, 0, 6, 0],
                                [2, 0, 3, 8, 5],
                                [0, 3, 0, 0, 7],
                                [6, 8, 0, 0, 9],
                                [0, 5, 7, 9, 0]]))
print()
demonstrate_prim(WeightedGraph([[0, 2, 0, 6],
                                [2, 0, 3, 8],
                                [0, 3, 0, 0],
                                [6, 8, 0, 0]]))
print()
demonstrate_prim(WeightedGraph([[1, 1, 1, 1],
                                [1, 1, 1, 1],
                                [1, 1, 1, 1],
                                [1, 1, 1, 1]]))
print()
demonstrate_prim(WeightedGraph([[1, 2, 3, 4],
                                [5, 6, 7, 8],
                                [9, 10, 11, 12],
                                [13, 14, 15, 16]]))
print()
"^__^"  # hi ;)
demonstrate_prim(WeightedGraph([[0, -202, 3, 4],
                                [5, 6, 7, 8],
                                [9, 10, 11, 12],
                                [13, 14, 15, 16]]))
```

### code
```python
class WeightedGraph:
    def __init__(self, matrix):
        assert all([len(matrix) == len(row) for row in matrix])

        self.vertices = len(matrix)
        self.graph = matrix

        
# Mostly based on the E-Maxx description
# see: http://e-maxx.ru/algo/mst_prim
def prim(G, looking_for_maximal=False):
    MST = set()
    X = set()  # the set of vertices contained in MST

    def exists_path(x, k):
        return G.graph[x][k] != 0

    X.add(0)  # truly Prim's should work with any of the starting vertices
    while len(X) != G.vertices:
        edges_outcoming_from_X = set()

        for x in X:
            for k in range(G.vertices):
                if k not in X and exists_path(x, k):
                    edges_outcoming_from_X.add((x, k))

        reverse = looking_for_maximal
        smallest_outcoming_edge = sorted(edges_outcoming_from_X,
                                         key=lambda e:G.graph[e[0]][e[1]],
                                         reverse=reverse)[0]
        MST.add(smallest_outcoming_edge)

        added_edge_destination_vertex = smallest_outcoming_edge[1]
        X.add(added_edge_destination_vertex)
    return MST


def demonstrate_prim(graph):
    MinST = prim(graph)
    MaxST = prim(graph, looking_for_maximal=True)

    print("coincidence weights matrix:")
    [print(row) for row in graph.graph]

    print("minimal spanning tree edges:",
          sorted(MinST, key=lambda e: e[0]),
          "spanning tree weight:",
          sum([graph.graph[a][b] for a,b in MinST]))

    print("maximal spanning tree edges:",
          sorted(MaxST, key=lambda e: e[0]),
          "spanning tree weight:",
          sum([graph.graph[a][b] for a,b in MaxST]))
```

