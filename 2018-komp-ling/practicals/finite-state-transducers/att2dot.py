import sys

print('digraph G { rankdir="LR"')
print('node [fontname="Tahoma",shape=circle,fontsize=14,fixedsize=true,fillcolor="grey",style=filled]')
print('edge [fontname="FreeMono",fontsize=14]')
for line in sys.stdin.readlines():
        line = line.strip()
        row = line.split('\t')
        if len(row) >= 4:
                print('%s [label="%s"];' % (row[0], row[0]))
                print('%s -> %s [label="%s:%s"];' % (row[0], row[1], row[2], row[3]))
        elif len(row) == 2: # Final state
                print('%s [label="%s",shape=doublecircle];' % (row[0], row[0]))

print('}')
