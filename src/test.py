'''
Function Testing
'''
from puzzle import Puzzle
import heuristics as h

test = "null"
def error():
    print(f"Failed on: {test}")

if __name__ == "__main__":
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
    if (h.misplaced_tile(3,p) != 7): error()
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
    [4,5,6],
    [7,0,8]]
    )
    if (h.manhattan_distance(3,p) != 4): 
        print(h.manhattan_distance(3,p))
        error()


    