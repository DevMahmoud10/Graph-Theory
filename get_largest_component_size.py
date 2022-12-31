def get_largests_component_bfs(graph):
    visited=set()
    max_component_size=0
    for node in graph:
        q=[node]
        if node in visited:
            continue
        component_size=0
        while len(q)>0:
            curr=q.pop(0)
            if curr in visited:
                continue
            component_size+=1
            visited.add(curr)
            for n in graph[curr]:
                q.append(n)
        max_component_size=max(max_component_size, component_size)
    return max_component_size

def get_largests_component_dfs(graph):
    visited=set()
    max_component_size=0
    for node in graph:
        if node in visited:
            continue
        stk=[node]
        component_size=0
        while len(stk)>0:
            curr=stk.pop()
            if curr in visited:
                continue
            visited.add(curr)
            component_size+=1
            for n in graph[curr]:
                stk.append(n)
        max_component_size=max(max_component_size, component_size)
    return max_component_size
        
def get_largests_component_dfs_recursive(graph):
    def dfs(graph, node, visited, component_size):
        if node in visited:
            return component_size
        visited.add(node)
        component_size+=1
        for n in graph[node]:
            extended_component_size=dfs(graph, n, visited, component_size)
            component_size=max(component_size, extended_component_size)
        return component_size
    visited=set()
    max_component_size=0
    for node in graph:
        component_size=dfs(graph, node, visited, 0)
        max_component_size=max(max_component_size, component_size)
    return max_component_size


graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1, 5, 6],
    4: [2],
    5: [3],
    6: [3],
    7: [8, 9, 10],
    8: [7],
    9: [7],
    10: [7],
    11: [12],
    12: [11]
}
res=get_largests_component_bfs(graph)
assert res==6
res=get_largests_component_dfs(graph)
assert res==6
res=get_largests_component_dfs_recursive(graph)
assert res==6
