def find_shortest_path(graph, source, destination):
    visited=set()
    q=[(source, 0)]
    while len(q)>0:
        node, distance=q.pop(0)
        if node==destination:
            return distance
        if node in visited:
            continue
        visited.add(node)
        for n in graph[node]:
            q.append((n, distance+1))
    return -1

graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1, 5, 6],
    4: [2, 5],
    5: [3, 4, 6],
    6: [3, 5],
}

res=find_shortest_path(graph, 1, 6)
assert res==2
