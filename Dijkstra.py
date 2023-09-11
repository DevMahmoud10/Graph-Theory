import heapq

def dijkstra(g):
    visited={}
    min_heap=[(0,'A')]
    while min_heap:
        s_weight,s_node=heapq.heappop(min_heap)
        if s_node in visited:
            continue
        visited[s_node]=s_weight
        for d_node,d_weight in g[s_node]:
            if d_node not in visited:
                heapq.heappush(min_heap, (s_weight+d_weight,d_node))
    return visited
        
g={'A':[('B',10), ('C',3)],
   'B':[('D',2)],
   'C':[('B',4), ('D',8), ('E',2)],
   'D':[('E',5)],
   'E':[]
}

print(dijkstra(g))      #{'A': 0, 'B': 7, 'C': 3, 'D': 9, 'E': 5}
