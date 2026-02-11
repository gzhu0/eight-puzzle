class Puzzle:
    def __init__(self, n, grid = None, center = None):
        '''
        n x n sliding Puzzle

        grid: n x n grid input
        center: coordinates for the 0 tile 
        '''
        if grid == None:
            self.grid = [[0 for _ in range(n)] for _ in range(n)]
        else: 
            self.grid = grid
        if center is None:
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if grid[i][j] == 0: 
                        self.center = (i,j)
        else: 
            self.center = center
        self.n = n

    def move(self): 
        '''
        Returns a list of Puzzles for all possible moves
        '''
        ret = []
        x,y = self.center
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
        Swaps the center with designated node and returns a Puzzle
        '''
        x,y = self.center
        new = [r[:] for r in self.grid]
        new[a][b], new[x][y] = new[x][y], new[a][b]
        return Puzzle(self.n, new, (a,b))

    def unroll(self): 
        '''
        Helper function for misplaced tile heuristic
        '''
        return [i for x in self.grid for i in x]

    
    def __eq__(self,other):
        '''
        Comparison function for use in the visited set
        '''
        g = self.unroll()
        g_other = other.unroll()
        for i in range(len(g)):
            if g[i] != g_other[i]:
                return False
        return True
    
    def __str__(self):
        '''
        For debugginig
        '''
        return f"{self.grid}"






