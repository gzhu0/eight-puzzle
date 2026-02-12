'''
General A* Algorithm to solve an n-puzzle
'''

import heapq
from node import Node
from puzzle import Puzzle


from collections import defaultdict

counts = defaultdict()
counter = 0

def queueing_function(nodes, new_nodes, visited, in_pq):
    '''
    Queueing function to put 
    '''
    for n in new_nodes:
        if n.hash() not in visited and n.hash() not in in_pq:
            if n.cost not in counts:
                counts[n.cost] = 0
            counts[n.cost] += 1
            heapq.heappush(nodes, n)
            in_pq.add(n.hash())
    return nodes


def general_search(puzzle: Node, queueing_function,heuristic):
    global counter
    '''
    Queueing function
    '''
    nodes = [puzzle]
    print([str(n) for n in nodes])
    visited = set() 
    in_pq = set() # Nodes currently in the queue
    in_pq.add(puzzle.hash())
    while True:
        counter += 1
        if len(nodes) == 0: 
            return -1
        node = heapq.heappop(nodes)
        visited.add(node.hash())
        in_pq.remove(node.hash())
        if node.goal_test():
            return node.val, counter, len(nodes), len(visited)
        nodes = queueing_function(nodes,node.expand(heuristic), visited, in_pq)
        
        

        