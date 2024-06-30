#minimum-spanning-tree using Prim's algorithm
import heapq

def get_mst_by_prims(g):
    min_heap = []
    for neighbor, weight in g['A']:
        heapq.heappush(min_heap, [weight, 'A', neighbor])

    mst = []
    visited = set()
    cost=0
    while min_heap:
        weight, n1, n2 = heapq.heappop(min_heap)
        if n1 in visited:
            continue
        mst.append([n1, n2])
        visited.add(n1)
        cost+=weight
        for neighbor, weight in g[n2]:
            if neighbor not in visited:
                heapq.heappush(min_heap, [weight, n2, neighbor])
    return cost,mst


g={'A':[('B',10),('C',3)],
   'B':[('A',10),('C',4),('D',1)],
   'C':[('A',3),('B',4),('D',4),('E',4)],
   'D':[('B',1),('C',4),('E',2)],
   'E':[('C',4),('D',2)]
}
    
    
print(get_mst_by_prims(g)) #(10, [['A', 'C'], ['C', 'B'], ['B', 'D'], ['D', 'E']])
