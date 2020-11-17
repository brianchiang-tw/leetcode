'''

Description:

Given the root node of a binary search tree, return the sum of values of all nodes with a value in the range [low, high].

 

Example 1:


Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32



Example 2:


Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
 

Constraints:

The number of nodes in the tree is in the range [1, 2 * 104].
1 <= Node.val <= 105
1 <= low <= high <= 105
All Node.val are unique.

'''



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
            
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        
        if root is None:
            # empty node or empty tree
            return 0
        
        
        # Divide and conquer with pruning redundant cases
        if root.val < L:
            # root is smaller than lower bound L, only consider and traverse right sub-tree
            return self.rangeSumBST( root.right, L, R )
        
        elif root.val > R:
            # root is larger than upper bound R, only consider and traverse left sub-tree
            return self.rangeSumBST( root.left, L, R )

        else:
            # root is in range, traverse both left and right sub-trees
            return root.val + self.rangeSumBST( root.right, L, R ) + self.rangeSumBST( root.left, L, R )


# n : the number of nodes in binary tree

## Time Complexity: O( n )
#
# The overhead in time is the cost of DFS, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the storagr for recursion call stack, which is of O( n )


import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        root = TreeNode( 10 )
        
        root.left = TreeNode( 5 )
        root.right = TreeNode( 15 )

        root.left.left = TreeNode( 3 )
        root.left.right = TreeNode( 7 )
        root.right.right = TreeNode( 18 )

        result = Solution().rangeSumBST(root=root, L=7, R=15)
        self.assertEqual(result, 32)


    def test_case_2( self ):

        root = TreeNode( 10 )
        
        root.left = TreeNode( 5 )
        root.right = TreeNode( 15 )

        root.left.left = TreeNode( 3 )
        root.left.right = TreeNode( 7 )
        root.right.left = TreeNode( 13 )
        root.right.right = TreeNode( 18 )

        root.left.left.left = TreeNode( 1 )
        root.left.right.left = TreeNode( 6 )

        result = Solution().rangeSumBST(root=root, L=6, R=10)
        self.assertEqual(result, 23)



if __name__ == '__main__':

    unittest.main()