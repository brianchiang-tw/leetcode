'''

Description:

Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true



Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false



Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false

'''



#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        if p and q:
            # both p and q exist
            return (p.val == q.val) and self.isSameTree( p.left, q.left) and self.isSameTree( p.right, q.right )
        
        elif not p and not q:
			# both p and q are empty node ( i.e., None )
            return True
        
        else:
			# either p or q is empty, the other is non-empty.
            return False


# n : the number of nodes in binary tree

## Time Complexity: O( n )
#
# The overhead in time is the cost of DFS traversal, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the cost of recursion stack, which is of O( n )



import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):
        
        root_1 = TreeNode( 1 )
        root_1.left = TreeNode( 2 )
        root_1.right = TreeNode( 3 )

        root_2 = TreeNode( 1 )
        root_2.left = TreeNode( 2 )
        root_2.right = TreeNode( 3 )

        result = Solution().isSameTree(root_1, root_2)
        self.assertEqual(result, True)




    def test_case_2( self ):
        
        root_1 = TreeNode( 1 )
        root_1.left = TreeNode( 2 )


        root_2 = TreeNode( 1 )
        root_2.right = TreeNode( 2 )

        result = Solution().isSameTree(root_1, root_2)
        self.assertEqual(result, False)



    def test_case_3( self ):
        
        root_1 = TreeNode( 1 )
        root_1.left = TreeNode( 2 )
        root_1.right = TreeNode( 1 )

        root_2 = TreeNode( 1 )
        root_2.left = TreeNode( 1 )
        root_2.right = TreeNode( 2 )

        result = Solution().isSameTree(root_1, root_2)
        self.assertEqual(result, False)


if __name__ == '__main__':

    unittest.main()

    