'''
General A* Algorithm to solve an n-puzzle
'''

import heapq
from node import Node
from puzzle import Puzzle

def queueing_function(nodes, new_nodes, visited):
    '''
    Queueing function to put 
    '''
    for n in new_nodes:
        if not n.puzzle in visited:
            heapq.heappush(nodes, n)


def general_search(puzzle, queueing_function):
    nodes = [Node(0,puzzle)]
    visited = set()
    while True:
        if len(nodes) == 0: return -1
        node = heapq.heappop(nodes)
        visited.add(node.puzzle)
        if node.goal_test():
            return node.val
        nodes = queueing_function(nodes,node.expand(), visited)
        