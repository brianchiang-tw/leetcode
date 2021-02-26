'''

Description:

Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

Example 1:


Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]



Example 2:

Input: root = [1,null,3]
Output: [1,3]



Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import defaultdict
from typing import List

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        
        if not root:
			# Quick response for empty tree
            return []
        
        # key: depth
		# value: value of right-most node
        self.side_view_dict = defaultdict( int )
        self.max_depth = 0
        
        def helper( node: TreeNode, depth: int):
            
            if node:
                
                if self.side_view_dict.get(depth, None) == None:
                    self.side_view_dict[depth] = node.val
                
                self.max_depth = max( self.max_depth, depth)
                
                # Let right sub-tree go before left sub-tree in order to get right side view
                helper( node.right, depth+1 )
                helper( node.left, depth+1 )
        
        # ----------------------------------------
        helper( node = root, depth = 0 )
        return [ self.side_view_dict[depth] for depth in range(0, self.max_depth+1) ]


import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        root = TreeNode( 1 )

        root.left = TreeNode( 2 )
        root.right = TreeNode( 3 )

        root.left.right = TreeNode( 5 )
        root.right.right = TreeNode( 4 )

        result = Solution().rightSideView( root )
        self.assertEqual(result, [1, 3, 4])


    def test_case_2( self ):

        root = TreeNode( 1 )
        
        root.right = TreeNode( 3 )

        result = Solution().rightSideView( root )
        self.assertEqual( result, [1, 3] )


    def test_case_3( self ):

        root = None

        result = Solution().rightSideView( root )
        self.assertEqual( result, [] )


        


if __name__ == '__main__':

    unittest.main()