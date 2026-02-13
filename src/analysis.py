'''
Analysis of various herustics for the sliding puzzle problem
'''
import matplotlib.pyplot as plt
import numpy as np
import time
import heuristics as h
from node import Node
from puzzle import Puzzle
from algorithm import general_search, queueing_function

cases = {
    0: [[1,2,3],[4,5,6],[7,8,9]],
    2 :[[1,2,3],[4,5,6],[0,7,8]],
    4: [[1,2,3],[5,0,6],[4,7,8]],
    8 :[[1,3,6],[5,0,2],[4,7,8]],
    12 :[[1,3,6],[5,0,7],[4,8,2]],
    16 :[[1,6,7],[5,0,3],[4,8,2]],
    20 :[[7,1,2],[4,8,5],[6,3,0]],
    24 :[[0,7,2],[4,6,1],[3,5,8]],
}


data = {
    "Runtime" : {
        "Uniform Cost Search" : [[],[],-1],
        "Misplaced Tiles" : [[],[],-1],
        "Manhattan Distance" : [[],[],-1]
    },
    "Max Queue Size" : {
        "Uniform Cost Search" : [[],[],-1],
        "Misplaced Tiles" : [[],[],-1],
        "Manhattan Distance" : [[],[],-1]
    },
    "Nodes Expanded" :{
        "Uniform Cost Search" : [[],[],-1],
        "Misplaced Tiles" : [[],[],-1],
        "Manhattan Distance" : [[],[],-1]
    },
}

heuristics = {
    "Uniform Cost Search" : h.uniform_cost_search,
    "Misplaced Tiles" : h.misplaced_tile,
    "Manhattan Distance" : h.manhattan_distance
}

for goal, puzzle in cases.items():
    start_state = Node(Puzzle(3,puzzle))
    for name, heuristic in heuristics.items():
        start_time = time.perf_counter()
        result = general_search(start_state,queueing_function,heuristic)
        end_time = time.perf_counter()
        data["Runtime"][name][0].append(goal)
        data["Runtime"][name][1].append(end_time - start_time)
        data["Max Queue Size"][name][0].append(goal)
        data["Max Queue Size"][name][1].append(result[1])
        data["Nodes Expanded"][name][0].append(goal)
        data["Nodes Expanded"][name][1].append(result[2])

# Calculate Averages
for metric in data:
    for heuristic, hdata in data[metric].items(): 
         hdata[2] = sum(hdata[1])/len(hdata[0])


for metric in data:
    plt.figure()
    for heuristic, hdata in data[metric].items():  
        plt.plot(hdata[0],hdata[1],label = heuristic)
    plt.legend()
    plt.xlabel("Solution Depth")
    plt.ylabel(f"{metric}{' (s)' if metric == 'Runtime' else ''}")
    plt.title(f"{metric} vs Solution Depth")

plt.show()






