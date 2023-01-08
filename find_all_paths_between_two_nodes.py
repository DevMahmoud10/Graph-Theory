
def get_all_paths(graph , source, destination):
    def dfs(graph , source, destination , visited , path, result):
        if source in visited:
            return
        visited.add(source)
        path.append(source)
        if source == destination:
            result.append(path[:])
        for n in graph[source]:
            if dfs(graph, n, destination, visited, path, result):
                result.append(path)
        path.pop()
        visited.remove(source)
    result=[]
    visited=set()
    dfs(graph , source , destination , visited, [], result)
    return result

graph = {}
graph[1] = [2, 5]
graph[2] = [1, 3, 5]
graph[3] = [2, 4]
graph[4] = [3, 5, 6]
graph[5] = [1, 2, 4]
graph[6] = [4]

res=get_all_paths(graph, 1, 6)
print(res)
#[[1, 2, 3, 4, 6], [1, 2, 5, 4, 6], [1, 5, 2, 3, 4, 6], [1, 5, 4, 6]]
