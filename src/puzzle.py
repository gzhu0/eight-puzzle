'''
Puzzle class to represent a n x n sliding puzzle
'''
class Puzzle:
    def __init__(self, n, grid = None, zero_pos = None):
        '''
        n x n sliding Puzzle

        grid: n x n grid input
        zero_pos: coordinates for the 0 tile 
        '''
        if grid == None:
            self.grid = [[0 for _ in range(n)] for _ in range(n)]
        else: 
            self.grid = grid
        if zero_pos is None:
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if grid[i][j] == 0: 
                        self.zero_pos = (i,j)
        else: 
            self.zero_pos = zero_pos
        self.n = n

    def move(self): 
        '''
        Returns a list of Puzzles for all possible moves
        '''
        ret = []
        x,y = self.zero_pos
        if x > 0: # up
            p = self.swap(x-1,y)
            ret.append(p)  
        if y > 0: # left
            p = self.swap(x,y-1)
            ret.append(p)  
        if x < self.n-1: # down
            p = self.swap(x+1,y)
            ret.append(p)  
        if y < self.n-1: # right
            p = self.swap(x,y+1)
            ret.append(p)  
        return ret

    def swap(self, a,b):
        '''
        Swaps the zero_pos with designated node and returns a Puzzle
        '''
        x,y = self.zero_pos
        new = [r[:] for r in self.grid]
        new[a][b], new[x][y] = new[x][y], new[a][b]
        return Puzzle(self.n, new, (a,b))

    def unroll(self): 
        '''
        Unrolls the puzzle grid into a 1D list, row by row 
        '''
        return [i for x in self.grid for i in x]
    
    def __str__(self):
        return f"{self.grid}"
    
    def check(self):
        '''
        Returns true if puzzle is in a goal state
        '''
        g = self.unroll()
        for i in range(len(g)-1):
            if i + 1 != g[i]:
                return False
        return True
    
    def __hash__(self):
        return hash(tuple(self.unroll()))








