'''

Description:

Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        
        # ---------------------------
        def dfs(node, attr):
            
            if not node:
            
                # base case:
                # empty node or empty tree
                return 0
            
             
            if not node.left and not node.right:

                # base case:
                # current node is leaf node

                return node.val if attr == 'left' else 0

           
            # general case:
            return dfs(node.left, 'left') + dfs(node.right, 'right')
        
        # ---------------------------
        return dfs(node=root, attr='root')


# n : the number of nodes in binary tree

## Time Complexity: O( n )
#
# The overhead in time is the cost of DFS, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for recursion call stack, which is of O( n )


import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):
        
        root = TreeNode( 3 )

        root.left = TreeNode( 9 )
        root.right = TreeNode( 20 )

        root.right.left = TreeNode( 15 )
        root.right.right = TreeNode( 7 )

        result = Solution().sumOfLeftLeaves( root=root )
        self.assertEqual( result, 24 )



if __name__ == '__main__':

    unittest.main()