def topological_sort(graph):
    def dfs(graph, node, visited, ordering):
        if node not in visited:
            visited.add(node)
            for n in graph[node]:
                dfs(graph, n, visited, ordering)
            ordering.append(node)
            
    visited = set()
    ordering=[]
    for node in graph:
        dfs(graph, node, visited, ordering)
    return ordering


graph = {          'A': ['D'],
                   'B': ['D'],
                   'C': ['A', 'B'],
                   'D': ['G', 'H'],
                   'E': ['A', 'D', 'F'],
                   'F': ['K', 'J'],
                   'G': ['I'],
                   'H': ['I', 'J'],
                   'I': ['L'],
                   'J': ['L', 'M'],
                   'K': ['J'],
                   'L': [],
                   'M': []}
res=topological_sort(graph)
#output = ['L', 'I', 'G', 'M', 'J', 'H', 'D', 'A', 'B', 'C', 'K', 'F', 'E']
