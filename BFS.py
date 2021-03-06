class Graph():
    def __init__(self):
        self.n = 0
        self.g = {}
        self.visited = {}

    def addEdge(self, source, destination):
        if source in self.g:
            if destination in self.g:
                if destination not in self.g[source]:
                    self.g[source].append(destination)
                if source not in self.g[destination]:
                    self.g[destination].append(source)
            else:
                self.g[destination] = [source]
                self.visited[destination] = False
                self.n += 1
        else:
            self.g[source] = [destination]
            self.visited[source] = False
            self.n += 1

    def bfs(self, node):
        q = [node]
        while len(q) > 0:
            node = q.pop(0)
            self.visited[node] = True
            for neighbor in self.g[node]:
                if not self.visited[neighbor] and neighbor not in q:
                    q.append(neighbor)
            print(node)


g = Graph()
g.addEdge('A', 'B')
g.addEdge('B', 'A')
g.addEdge('A', 'C')
g.addEdge('C', 'A')
g.addEdge('C', 'E')
g.addEdge('E', 'C')
g.addEdge('B', 'D')
g.addEdge('D', 'B')
g.addEdge('B', 'E')
g.addEdge('E', 'B')
g.addEdge('D', 'E')
g.addEdge('E', 'D')
g.addEdge('D', 'F')
g.addEdge('F', 'D')
g.addEdge('E', 'F')
g.addEdge('F', 'E')

print("BFS :")
g.bfs('A')

# input:
# Graph Structure
#     A
#    / \
#   B   C
#  | \   |
#  |  \  |
#  |   \ |
#  |    \|
#  D ___ E
#  \     |
#   \   /
#     F

# output:
# BFS :
# A B C D E F
