def topological_sort_bfs(graph):
    in_degree = {}  # holds number of edges inserted to every node
    for node in graph['nodes']:
        in_degree[node] = 0

    for node in graph['nodes']:
        for neighbor in graph['nodes'][node]:
            in_degree[neighbor] += 1

    q = []
    for node in graph['visited']:
        if in_degree[node] == 0:
            q.append(node)
    c = 0
    ordering = []  # output
    while len(q) > 0:
        current = q.pop(0)
        ordering.append(current)
        for neighbor in graph['nodes'][current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                q.append(neighbor)
        c += 1
    if c != graph['nodes_number']:
        print("Graph have cycle")
        return []
    else:
        return ordering[::-1]


def topological_sort_dfs(graph):
    def dfs(graph, node, ordering):
        graph['visited'][node] = True
        for neighbor in graph['nodes'][node]:
            if not graph['visited'][neighbor]:
                dfs(graph, neighbor, ordering)
        ordering.append(node)

    ordering = []
    for node in graph['nodes']:
        if not graph['visited'][node]:
            dfs(graph, node, ordering)
    return ordering


## #Expected_input
graph = {'nodes': {'A': ['D'],
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
                   'M': []},
         }
graph['nodes_number'] = len(graph['nodes'])
graph['visited'] = {node: False for node in graph['nodes']}

# #calling
print(topological_sort_dfs(graph))
# #Expected output
# ['L', 'I', 'G', 'M', 'J', 'H', 'D', 'A', 'B', 'C', 'K', 'F', 'E']

# #calling
print(topological_sort_bfs(graph))
# #Expected output
# ['M', 'L', 'J', 'I', 'H', 'G', 'K', 'D', 'F', 'A', 'B', 'E', 'C']
