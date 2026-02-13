from puzzle import Puzzle
from node import Node
import heuristics as h
from algorithm import general_search, queueing_function


heuristics = {0: h.uniform_cost_search, 
              1: h.misplaced_tile, 
              2: h.manhattan_distance
            }

def run_puzzle(trace: bool, start_node: Node):
    print("Please choose your heuristic: ")
    print('''
        0 - Uniform Cost Search
        1 - Misplaced Tiles
        2 - Manhattan Distance
          ''')
    user_input = int(input())
    if user_input in heuristics:
        h = heuristics[user_input]
        soln_depth, max_queue_size, nodes_expanded = general_search(start_node, queueing_function, h, trace)
        if soln_depth == -1:
            print("No Solution Found")
        else: print(f"Solution found at depth {soln_depth}")
        print(f"Max Queue Size: {max_queue_size}")
        print(f"Nodes Expanded: {nodes_expanded}")
        
    else: 
        print("Invalid Input")
        return

if __name__ == "__main__":

    trace = False

    print("***8-Puzzle Solver***")
    while True:
        print(f'''
        0 - Default Puzzle
        1 - Input Puzzle
        2 - Toggle Trace (Currently: {"On" if trace else "Off"})
        3 - Exit Program
              ''')
        user_input = int(input())
        if user_input == 0:
            start_node = Node(Puzzle(3, [[1,6,7],[5,0,3],[4,8,2]]))
            run_puzzle(trace, start_node)
        elif user_input == 1:
            print("Input the puzzle. Seperate every item in a row with only a space")
            row1 = [int(x) for x in input().split()]
            row2 = [int(x) for x in input().split()]
            row3 = [int(x) for x in input().split()]
            start_node = Node(Puzzle(3,[row1, row2, row3]))
            run_puzzle(trace, start_node)
        elif user_input == 2: 
            trace = not trace
        elif user_input == 3:
            break   
        else:
            print("Invalid Input")
