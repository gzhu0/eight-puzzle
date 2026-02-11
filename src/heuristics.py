'''
Heuristic functions for sliding puzzle.
'''

def uniform_cost_search():
    return 0

def misplaced_tile(n, puzzle):
    '''
    Returns the number of misplaced tiles for a n x n puzzle (excluding blank tile)
    '''
    g = puzzle.unroll()
    count = 0
    for i in range(len(g)):
        if g[i] != i+1 and g[i] != 0:
            count += 1
    return count

def manhattan_distance(n,puzzle):
    '''
    Returns the sum of the distance each tile is away from the correct position for an n x n puzzle (excluding blank tile)
    '''
    total = 0
    curr = 0
    g = puzzle.grid
    for i in range(len(g)):
        for j in range(len(g[i])):
            curr = g[i][j]
            if curr == 0: continue
            # Calculate the tile it is supposed to be on
            curr_i = (curr-1)//n
            curr_j = (curr-1)%n
            # Find the distance of current tile to ideal distance
            dist = abs(i-curr_i) + abs(j-curr_j)
            total += dist 
    return total

