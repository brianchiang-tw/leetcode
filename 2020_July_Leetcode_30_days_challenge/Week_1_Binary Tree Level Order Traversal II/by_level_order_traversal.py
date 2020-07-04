'''

Description:

Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
   
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]

'''



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List
from collections import deque
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        
        result = deque()
        traversal_queue = [ root ] if root else []
        
        # launch level-order traversal
        while traversal_queue:
            
            cur_level = []
            next_level_queue = []
            
            for node in traversal_queue:
                
                cur_level.append( node.val )
                
                if node.left:
                    next_level_queue.append( node.left )
                    
                if node.right:
                    next_level_queue.append( node.right )
            
            # push current level traversal to result on the head ( for reverse level order )
            result.appendleft( cur_level )
            
            traversal_queue = next_level_queue
            
        return [*result]



# n : the number of nodes in binary tree

## Time Complexity: O( n )
#
# The overhead in time is the cost of level-order traversal, which is of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the storage for list, result, which is of O( n ).


import unittest
class Testing( unittest.TestCase ):

    def test_case_1(self):

        root = TreeNode( 3 )

        root.left = TreeNode( 9 )
        root.right = TreeNode( 20 )

        root.right.left = TreeNode( 15 )
        root.right.right = TreeNode( 7 )



if __name__ == '__main__':

    unittest.main()