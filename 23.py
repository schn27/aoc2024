from aocd import data
from aocd import submit

connections = {}

for k, v in map(lambda e: e.split('-'), data.split('\n')):
    if k not in connections:
        connections[k] = set()
    connections[k].add(v)
    if v not in connections:
        connections[v] = set()
    connections[v].add(k)

t_triangles = set()

for k in filter(lambda e: e[0] == 't', connections.keys()):
    nodes = list(connections[k])
    for i, ni in enumerate(nodes[:-1]):
        for nj in nodes[i + 1:]:
            if nj in connections[ni]:
                t_triangles.add(','.join(sorted([k, ni, nj])))

submit(len(t_triangles), part='a')

# Bron-Kerbosh
def get_cliques(connections):
    res = []
    compsub = set()

    def extend(candidates, not_ = set()):
        while len(candidates) > 0 and not any(map(lambda e: set(candidates).issubset(connections[e]), not_)):
            v = candidates.pop()
            compsub.add(v)
            new_candidates = list(filter(lambda e: v in connections[e], candidates))
            new_not = set(filter(lambda e: v in connections[e], not_))
            if len(new_candidates) == 0 and len(new_not) == 0:
                res.append(compsub.copy())
            else:
                extend(new_candidates, new_not)
            compsub.remove(v)
            not_.add(v)

    extend(list(connections.keys()))
    return res

max_clique = sorted(get_cliques(connections), key=lambda e: len(e))[-1]
submit(','.join(sorted(max_clique)), part='b')
