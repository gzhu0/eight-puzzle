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
x = general_search(p1, queueing_function, h.uniform_cost_search)
print(x)





