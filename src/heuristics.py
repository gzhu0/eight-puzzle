'''
Heuristic functions for sliding puzzle.
'''

def uniform_cost_search():
    return 0

def misplaced_tile(n, puzzle):
    '''
    Returns the number of misplaced tiles for a n x n puzzle
    '''
    g = puzzle.unroll()
    g = g[-1:] + g[:-1]
    count = 0
    for i in range(len(g)):
        if g[i] != i:
            count += 1
    return count



