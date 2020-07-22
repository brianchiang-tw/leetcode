'''

Description:

Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).



For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:

[
  [3],
  [20,9],
  [15,7]
]

'''



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        
        traversal_queue = [ root ] if root else []
        
        path = []
        right_to_left = False
        
        while traversal_queue:
            
            cur_level_path, next_level_queue = [], []
            
            for node in traversal_queue:
                
                cur_level_path.append( node.val )
                
                if node.left:
                    next_level_queue.append( node.left )

                if node.right:
                    next_level_queue.append( node.right )

                    
            # update path of level-order traversal        
            if right_to_left:
                path.append( cur_level_path[::-1] )
            else:
                path.append( cur_level_path )
            
            # update traversal queue as next level queue
            traversal_queue = next_level_queue
            
            # switch direction for next level
            right_to_left = right_to_left ^ True
        
        return path



# n : the number of nodes in binary tree

## Time Complexity: O( n )
#
# The overhead in time is the cost of level-order traversal, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for path, which is of O( n )


import unittest


class Testing( unittest.TestCase ):

    def test_case_1( self ):

        root = TreeNode( 3 )

        root.left = TreeNode( 9 )
        root.right = TreeNode( 20 )

        root.right.left = TreeNode( 15 )
        root.right.right = TreeNode( 7 )

        result = Solution().zigzagLevelOrder( root )

        answer = [
                    [3],
                    [20,9],
                    [15,7]
                ]

        self.assertEqual(result, answer)


if __name__ == '__main__':

    unittest.main()