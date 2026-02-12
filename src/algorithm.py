'''
General A* Algorithm to solve an n-puzzle
'''

import heapq
from node import Node
from puzzle import Puzzle


from collections import defaultdict

depth_counts = defaultdict() #frequency for the depth of each node

def empty(list : list):
    return len(list) == 0

def remove_front(list : list):
    return heapq.heappop(list)

def queueing_function(nodes, new_nodes, visited_nodes, queued_nodes):
    '''
    Queueing function to put 
    '''
    for n in new_nodes:
        #if n.hash() not in visited_nodes and n.hash() not in queued_nodes:
        if n.hash() not in queued_nodes:
            if n.cost not in depth_counts:
                depth_counts[n.cost] = 0
            depth_counts[n.cost] += 1
            heapq.heappush(nodes, n)
            queued_nodes.add(n.hash())
    return nodes


def general_search(puzzle: Node, queueing_function,heuristic):
    '''
    Queueing function
    '''
    nodes = [puzzle] # Making the queue
    # Creating set of visited nodes and set of queued nodes
    visited_nodes = set() 
    queued_nodes = set() 
    queued_nodes.add(puzzle.hash())

    while True:
        if empty(nodes): 
            return -1
        node = remove_front(nodes)
        # Adding node to set of visited nodes
        #visited_nodes.add(node.hash())
        #queued_nodes.remove(node.hash())

        if node.goal_test():
            return node.cost, len(nodes), len(visited_nodes)
        nodes = queueing_function(nodes,node.expand(heuristic), visited_nodes, queued_nodes)
        
        

        