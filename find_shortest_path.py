# shortest path between two nodes in unweighted undirected graph
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

#########################################################################
# shortest path between two nodes in weighted directed graph

import heapq

def shortestPath(g, source, destination) -> int:
        distances = {node: float('inf') for node in g}
        distances[source] = 0

        hq = [(0, source)]

        while hq:
            current_distance, current_node = heapq.heappop(hq)  #pop min distance

            if current_node == destination:   #found destination
                break

            if current_distance > distances[destination]: #longer distance so skip
                continue

            for neighbor, weight in g[current_node]:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(hq, (distance, neighbor))

        return distances[destination]
        
g={'A':[('B',10), ('C',3)],
   'B':[('D',2)],
   'C':[('B',4), ('D',8), ('E',2)],
   'D':[('E',5)],
   'E':[]
}

res=shortestPath(g, 'A', 'D')
assert res==9
