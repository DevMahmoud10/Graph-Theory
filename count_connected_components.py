def get_connected_components_count_bfs(graph):
    visited=set()
    count=0
    for node in graph:
        q=[node]
        if node in visited:
            continue
        while len(q)>0:
            curr=q.pop(0)
            if curr in visited:
                continue
            visited.add(curr)
            for n in graph[curr]:
                q.append(n)
        count+=1
    return count

def get_connected_components_count_dfs(graph):
    visited=set()
    count=0
    for node in graph:
        if node in visited:
            continue
        stk=[node]
        while len(stk)>0:
            curr=stk.pop()
            if curr in visited:
                continue
            visited.add(curr)
            for n in graph[curr]:
                stk.append(n)
        count+=1
    return count
        
def get_connected_components_count_dfs_recursive(graph):
    def dfs(graph, node, visited):
        if node in visited:
            return False
        visited.add(node)
        for n in graph[node]:
            dfs(graph, n, visited)
        return True
    visited=set()
    count=0
    for node in graph:
        if dfs(graph, node, visited):
            count+=1
    return count


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
res=get_connected_components_count_bfs(graph)
assert res==3
res=get_connected_components_count_dfs(graph)
assert res==3
res=get_connected_components_count_dfs_recursive(graph)
assert res==3
