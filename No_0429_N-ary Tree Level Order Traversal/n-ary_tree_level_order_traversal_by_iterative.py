'''

Description:

Given an n-ary tree, return the level order traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).


Constraints:

The height of the n-ary tree is less than or equal to 1000
The total number of nodes is between [0, 10^4]

'''




# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children



from typing import List
from collections import deque
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        # base case:
        if not root:
            return []
        
        # base_case:
        traversal_queue = deque( [(root, 0)] )
        
        path = []
        cur_level_path, prev_level = [], 0
        
        # general case:
        while traversal_queue:
        
            # pop one node from traversal queue
            current, cur_level = traversal_queue.popleft()
            
            if current:
                
                if cur_level != prev_level:
                    # prev level is completed, append prev level path
                    path.append( cur_level_path[::] )
                    
                    # reset current level path
                    cur_level_path.clear()
                    
                    # update prev level 
                    prev_level = cur_level
                    
                
                
                cur_level_path.append( current.val )
                
                
                # adding children into traversal queue
                for child in current.children:
                    traversal_queue.append( (child, cur_level+1) )
                    
        
        # append last level's traversal path
        path.append( cur_level_path[::])

        return path



# n : the number of nodes in n-ary tree

## Time Complexity: O( n )
#
# The overhead in time is the BFS traversal of a n-ary tree, which is of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the storage for BFS traversal path, which is of O( n ).