'''
Function Testing
'''
from puzzle import Puzzle
from node import Node
import heuristics as h
from algorithm import general_search, queueing_function


test = "null"
def error():
    print(f"Failed on: {test}")

if __name__ == "__main__":
    # Testing General Serach Function
    # test = "General Search"
    # head = Node( Puzzle(3,
    # [[5,6,4],
    # [1,2,0],
    # [3,8,7]]
    # ) )
    # x = general_search(head, queueing_function, h.uniform_cost_search)
    # if (x != 0):
    #     error()
    #     print(x)

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
    if (h.misplaced_tile(3,p) != 0): error()
    p = Puzzle(3,
    [[2,1,3],
    [6,0,7],
    [4,8,5]]
    )
    if (h.misplaced_tile(3,p) != 6): error()
    p = Puzzle(3,
    [[1,3,2],
    [4,9,7],
    [8,5,0]]
    )
    if (h.misplaced_tile(3,p) != 6): error()

    # Testing Manhattan Distance
    # Using example from Lecture 3 Slide 29
    test = "Manhattan Distance"
    p = Puzzle(3,
    [[1,2,3],
    [4,5,6],
    [7,8,0]]
    )
    if (h.manhattan_distance(3,p) != 0): 
        print(h.manhattan_distance(3,p))
        error()
    p = Puzzle(3,
    [[3,2,8],
    [4,5,6],
    [7,1,0]]
    )
    if (h.manhattan_distance(3,p) != 8): 
        print(h.manhattan_distance(3,p))
        error()
    p = Puzzle(3,
    [[1,3,2],
    [4,5,8],
    [7,0,6]]
    )
    if (h.manhattan_distance(3,p) != 5): 
        print(h.manhattan_distance(3,p))
        error()


    