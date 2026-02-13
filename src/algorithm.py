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
    Queueing function to put 
    '''
    for n in new_nodes:
        if n.hash() not in visited_nodes:
            if n.cost not in depth_counts:
                depth_counts[n.cost] = 0
            depth_counts[n.cost] += 1
            heapq.heappush(nodes, n)
    return nodes


def general_search(puzzle: Node, queueing_function,heuristic):
    '''
    Queueing function
    '''
    nodes = [puzzle] # Making the queue
    # Creating set of all queued nodes
    visited_nodes = set() 

    while True:
        if empty(nodes): 
            return -1
        node = remove_front(nodes)
        visited_nodes.add(node.hash())
        #print(f"Node {node.cost} {node.val} {node.hash()}")

        if node.goal_test():
            return node
        nodes = queueing_function(nodes,node.expand(heuristic), visited_nodes)
        
        

        