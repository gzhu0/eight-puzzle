from puzzle import Puzzle
from node import Node
import heuristics as h
from algorithm import general_search, queueing_function

'''
Main interface 
'''
p1 = Node( Puzzle(3,
[[5,6,4],
[1,2,0],
[3,8,7]]
) )

p2 = Node( Puzzle(3,
[[5,1,0],
[2,6,3],
[4,7,8]]
) )

p3 = Node( Puzzle(3,
[[0,7,2],
[4,6,1],
[3,5,8]]
) )

p4 = Node( Puzzle(3,
[[1,6,7],[5,0,3],[4,8,2]]
) )

x = general_search(p4, queueing_function, h.uniform_cost_search)
print("Search Completed:", x)
