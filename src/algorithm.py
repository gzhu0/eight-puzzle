'''
General A* Algorithm to solve an n-puzzle
'''

import heapq
from node import Node
from puzzle import Puzzle


from collections import defaultdict

counts = defaultdict()
counter = 0

def queueing_function(nodes, new_nodes, visited):
    '''
    Queueing function to put 
    '''
    for n in new_nodes:
        if not n.puzzle in visited:
            if n.cost not in counts:
                counts[n.cost] = 0
            counts[n.cost] += 1
            heapq.heappush(nodes, n)
    return nodes


def general_search(puzzle: Node, queueing_function,heuristic):
    global counter
    '''
    Queueing function
    '''
    nodes = [puzzle]
    print([str(n) for n in nodes])
    visited = set()
    while True:
        counter += 1
        #print(counts)
        if len(nodes) == 0: 
            return -1
        node = heapq.heappop(nodes)
        visited.add(node.puzzle)
        if node.goal_test():
            return node.val, counter, len(nodes), len(visited)
        nodes = queueing_function(nodes,node.expand(heuristic), visited)
        
        

        