'''
Tests for various helper functions and algorithm test cases
'''
from puzzle import Puzzle
from node import Node
import heuristics as h
from algorithm import general_search, queueing_function
import time


test = "null"
def error():
    print(f"Failed on: {test}")

if __name__ == "__main__":

    # Testing Searches
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
    heuristics = (h.uniform_cost_search, h.misplaced_tile, h.manhattan_distance)

    for ans, puzzle in cases.items():
        initial_state = Node(Puzzle(3,puzzle))
        for func in heuristics:
            print(f"Testing {ans} on {func.__name__}")
            start_time = time.perf_counter()
            result = general_search(initial_state, queueing_function, func)
            end_time = time.perf_counter()
            if result[0] != ans:
                print(f"Test {ans} failed on {func}: Got {result[0]} but expected {ans}")
                
            else:
                print("Test Passed")
            print("Time: ", end_time - start_time)

    # Testing Check Function
    n = Node( Puzzle(3,
    [[1,2,3],
    [4,5,6],
    [7,8,0]]
    ) )
    if not n.goal_test(): print("Goal test failed!")

    # Testing Puzzle Equals Override
    a = Puzzle(3,
    [[1,3,2],
    [4,8,7],
    [5,0,6]]
    )
    b = Puzzle(3,
    [[1,3,2],
    [4,8,7],
    [5,0,6]]
    )
    if (a != b): print("Equals not working")

     # Testing Puzzle In
    a = [Puzzle(3,
    [[1,3,2],
    [4,8,7],
    [5,0,6]]
    )]
    b = Puzzle(3,
    [[1,3,2],
    [4,8,7],
    [5,0,6]]
    )
    if not b in a: print("Hash not working")

    # Testing Node Class
    p = Puzzle(3,
    [[1,2,3],
    [4,5,6],
    [7,8,0]]
    )
    node = Node(p)
    # nodes = node.expand(h.misplaced_tile)
    # for i in nodes:
    #     print(i)
    # print()

    p = Puzzle(3,
    [[1,4,2],
    [3,0,6],
    [8,7,5]]
    )
    # node = Node(p)
    # nodes = node.expand(h.manhattan_distance)
    # for i in nodes:
    #     print(i)


    # Testing Misplaced Tile
    test = "Misplaced Tile"
    p = Puzzle(3,
    [[1,2,3],
    [4,5,6],
    [7,8,0]]
    )
    if (h.misplaced_tile(p) != 0): error()
    p = Puzzle(3,
    [[2,1,3],
    [6,0,7],
    [4,8,5]]
    )
    if (h.misplaced_tile(p) != 6): error()
    p = Puzzle(3,
    [[1,3,2],
    [4,9,7],
    [8,5,0]]
    )
    if (h.misplaced_tile(p) != 6): error()

    # Testing Manhattan Distance
    # Using example from Lecture 3 Slide 29
    test = "Manhattan Distance"
    p = Puzzle(3,
    [[1,2,3],
    [4,5,6],
    [7,8,0]]
    )
    if (h.manhattan_distance(p) != 0): 
        print(h.manhattan_distance(p))
        error()
    p = Puzzle(3,
    [[3,2,8],
    [4,5,6],
    [7,1,0]]
    )
    if (h.manhattan_distance(p) != 8): 
        print(h.manhattan_distance(p))
        error()

    p = Puzzle(3,
    [[7,8,1],
    [6,0,2],
    [5,4,3]]
    )
    if (h.manhattan_distance(p) != 16): 
        print(h.manhattan_distance(p))
        error()


    