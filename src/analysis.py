'''
Analysis of various herustics for the sliding puzzle problem. Gets metrics for each run and saves it as data
'''
import numpy as np
import time
import json
import heuristics as h
import matplotlib as plt
from itertools import islice
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
count = 0

def generate_data():
    with open("src\\data\\puzzles.jsonl") as f:
        for line in islice(f, 100):
            indata = json.loads(line)
            goal, puzzle = indata["depth"], indata["grid"]

        #for goal, puzzle in cases.items(): ALTERNATE LINE FOR CASES
            start_state = Node(Puzzle(3,puzzle))
            for name, heuristic in heuristics.items():
                print(f"Running {count} on {name}")
                start_time = time.perf_counter()
                result = general_search(start_state,queueing_function,heuristic)
                end_time = time.perf_counter()
                data["Runtime"][name][0].append(goal)
                data["Runtime"][name][1].append(end_time - start_time)
                data["Max Queue Size"][name][0].append(goal)
                data["Max Queue Size"][name][1].append(result[1])
                data["Nodes Expanded"][name][0].append(goal)
                data["Nodes Expanded"][name][1].append(result[2])
            count += 1

    # Calculate Averages
    for metric in data:
        for heuristic, hdata in data[metric].items(): 
            hdata[2] = sum(hdata[1])/len(hdata[0])

    # Saving the data
    with open("src\\data\\data.json", "w") as f:
        json.dump(data, f, indent=4) 

def plot_data(data):
    # Plotting the Data
    import numpy as np
    from scipy.optimize import curve_fit

    for metric in data:
        plt.figure()
        for heuristic, hdata in data[metric].items():
            x, y = np.array(hdata[0]), np.array(hdata[1])
            plt.plot(x, y, 'o', label=f'{heuristic} (data)', alpha=0.5)
            
            # Fit a polynomial (adjust degree as needed)
            coeffs = np.polyfit(x, y, deg=2)
            poly = np.poly1d(coeffs)
            
            # Generate smooth curve
            x_smooth = np.linspace(x.min(), x.max(), 100)
            y_smooth = np.maximum(poly(x_smooth), 0)  # Clip to 0
            
            plt.plot(x_smooth, y_smooth, '-', label=f'{heuristic} (fit)')
        
        plt.legend()
        plt.xlabel("Solution Depth")
        plt.ylabel(f"{metric}{' (s)' if metric == 'Runtime' else ''}")
        plt.title(f"{metric} vs Solution Depth")

if __name__ == "__main__":
    #generate_data()

    with open("src\\data\\data.json", "r") as f:
        data = json.load(f)

    plot_data(data)








