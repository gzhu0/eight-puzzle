'''
Randomly generates puzzles and tests their viability, then puts all valid puzzles into a list.
'''

import random
import json
from puzzle import Puzzle
from node import Node
import heuristics as h
from algorithm import general_search, queueing_function



def random_puzzle():

    nums = list(range(9))
    random.shuffle(nums)

    grid = [nums[i*3:(i+1)*3] for i in range(3)]
    return grid

# Code from GeeksForGeeks
def getInvCount(arr):
    inv_count = 0
    empty_value = 0
    for i in range(0, 9):
        for j in range(i + 1, 9):
            if arr[j] != empty_value and arr[i] != empty_value and arr[i] > arr[j]:
                inv_count += 1
    return inv_count

# Code from GeeksForGeeks
def isSolvable(puzzle) :
    # Count inversions in given 8 puzzle
    inv_count = getInvCount([j for sub in puzzle for j in sub])
    # return true if inversion count is even.
    return (inv_count % 2 == 0)    

data = []
i = 0
num_puzzles = 100
while i <= num_puzzles:
    grid = random_puzzle()
    if not isSolvable(grid):
        continue
    start_node = Node(Puzzle(3,grid))
    result = general_search(start_node, queueing_function, h.manhattan_distance)
    print(f"Finished Puzzle {i}: {result[0]}")
    if result[0] != -1:
        data.append((result[0],grid))
        i += 1

with open("src\data\puzzles.jsonl", "w") as f:
    for depth, grid in data:
        json.dump({"depth": depth, "grid": grid}, f)
        f.write("\n")