def has_cycle(graph):
    def is_node_in_cycle(graph, node, visited, currently_in_stack):
        visited.add(node)
        currently_in_stack.add(node)
        for n in graph[node]:
            if n in currently_in_stack:
                return True
            if n in visited:
                continue
            if is_node_in_cycle(graph, n, visited, currently_in_stack):
                return True
        currently_in_stack.remove(node)
        return False

    visited=set()
    currently_in_stack=set()
    for node in graph:
        if node in visited:
            continue
        if is_node_in_cycle(graph, node, visited, currently_in_stack):
            return True
    return False
            
graph = {
    1: [2, 4],
    2: [3],
    3: [3],
    4: [5],
    5: [2]
}
res=has_cycle(graph)
assert res==True

graph = {
    1: [2, 4],
    2: [3],
    3: [],
    4: [5],
    5: [2]
}
res=has_cycle(graph)
assert res==False
