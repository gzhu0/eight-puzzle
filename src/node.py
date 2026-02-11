'''
Node class for searching through puzzles states
'''

class Node:
    def __init__(self, puzzle, cost = None, val = None):
        if cost == None:
            self.cost = 0
        else: 
            self.cost = cost
        if val == None: 
            self.val = 0
        else: 
            self.val = val
        self.puzzle = puzzle

    # Overload operators for use in queueing structure 
    def __lt__(self,other):
        return self.val < other.val
    
    def __gt__(self,other):
        return self.val > other.val
    
    def __str__(self):
        return f"Cost: {self.cost}. val: {self.val}, Puzzle: {self.puzzle}"
    
    def expand(self, heuristic):
        # Expands node by expanding the puzzle, updating cost, and applying heuristics
        puzzles = self.puzzle.move()
        nodes = []
        for p in puzzles:
            nodes.append(Node(p, self.cost+1, heuristic(p.n, p) + self.cost+1))
        return nodes
    
    def goal_test(self):
        '''
        Returns true if the node is in a goal state
        '''
        return self.puzzle.check()
            