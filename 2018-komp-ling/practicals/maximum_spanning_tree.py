graph = {'a':{3:'b', 4:'g', 5:'f'}, 'b':{3:'g', 5:'c'}, 'c':{ 6:'g', 9:'d'}, 'd':{ 7:'g', 8:'e'},
         'e':{ 4:'g', 2:'f'}, 'f':{ 1:'g'} }
picked = ['a']
result_distance = 0
trace = []

while len(picked) < len(graph.keys()) + 1 :
    pool = {}
    for i in picked:
        try:
            for i2 in graph[i]:
                if graph[i][i2] not in picked:
                    pool[i2] = graph[i][i2]
        except:
            pass

    picked.append(pool[max(pool.keys())])
    result_distance += max(pool.keys())

    for start in graph:
        try:
            if graph[start][max(pool.keys())] == pool[max(pool.keys())]:
                trace.append(start + pool[max(pool.keys())])
                break
        except:
            pass

print('The longest distance is: ', result_distance)
print('The connected nodes are: ', trace)