#Has Path?

def has_path_bfs(graph, source, destination):
    q=[source]
    visited=set()
    while len(q)>0:
        curr=q.pop(0)
        if curr in visited:
            continue
        if curr==destination:
            return True
        visited.add(curr)
        for n in graph[curr]:
            q.append(n)
    return False

def has_path_dfs(graph, source, destination):
    stk=[source]
    visited=set()
    while len(stk)>0:
        curr=stk.pop()
        if curr in visited:
            continue
        if curr==destination:
            return True
        visited.add(curr)
        for n in graph[curr]:
            stk.append(n)
    return False

def has_path_dfs_recursive(graph, source, destination):
    visited=set()
    def dfs(graph, source, destination, visited):
        if source==destination:
            return True
        for n in graph[source]:
            if n not in visited:
                dfs(graph, n, destination, visited)
        return False


graph = {
    1: [2, 3],
    2: [4],
    3: [5, 6],
    4: [],
    5: [],
    6: [],
    7: [8, 9, 10],
    8: [],
    9: [6],
    10: [],
}
res=has_path_bfs(graph, source = 7, destination = 6)
assert res==True

res=has_path_bfs(graph, source = 7, destination = 4)
assert res==False

res=has_path_dfs(graph, source = 7, destination = 6)
assert res==True

res=has_path_dfs(graph, source = 7, destination = 4)
assert res==False

res=has_path_dfs(graph, source = 7, destination = 6)
assert res==True

res=has_path_dfs(graph, source = 7, destination = 4)
assert res==False
