'''
General A* Algorithm to solve an n-puzzle
'''

import heapq
from node import Node
from puzzle import Puzzle


from collections import defaultdict

depth_counts = defaultdict(int) #frequency for the depth of each node

def empty(list : list):
    return len(list) == 0

def remove_front(list : list):
    return heapq.heappop(list)

def queueing_function(nodes, new_nodes, visited_nodes):
    '''
    Queueing function for the general search
    '''
    for n in new_nodes:
        if n.hash() not in visited_nodes:
            if n.cost not in depth_counts:
                depth_counts[n.cost] = 0
            depth_counts[n.cost] += 1
            heapq.heappush(nodes, n)
    return nodes


def general_search(start_node: Node, queueing_function, heuristic, trace = False):
    '''
    General Search Function 
    Returns goal node, max queue size, nodes expanded
    '''
    nodes = [start_node] # Making the queue
    visited_nodes = set() # Initializing visited set
    nodes_expanded = 0 # Keeping track of the amount of nodes expanded
    max_queue_size = 1 # Keeping track of the max queue size

    while True:
        if empty(nodes): 
            return -1, max_queue_size, nodes_expanded
        node = remove_front(nodes)
        visited_nodes.add(node.hash())

        if trace: print(f"Popping {node}")
        nodes_expanded += 1

        if node.goal_test():
            return node.cost, max_queue_size, nodes_expanded
        nodes = queueing_function(nodes,node.expand(heuristic), visited_nodes)
        max_queue_size = max(max_queue_size, len(nodes))
        
        
        

        