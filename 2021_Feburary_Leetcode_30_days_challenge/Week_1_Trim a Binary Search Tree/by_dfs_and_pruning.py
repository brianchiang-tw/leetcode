'''

Description:

Given the root of a binary search tree and the lowest and highest boundaries as low and high, trim the tree so that all its elements lies in [low, high]. Trimming the tree should not change the relative structure of the elements that will remain in the tree (i.e., any node's descendant should remain a descendant). It can be proven that there is a unique answer.

Return the root of the trimmed binary search tree. Note that the root may change depending on the given bounds.

 

Example 1:


Input: root = [1,0,2], low = 1, high = 2
Output: [1,null,2]



Example 2:


Input: root = [3,0,4,null,2,null,null,1], low = 1, high = 3
Output: [3,2,null,1]



Example 3:

Input: root = [1], low = 1, high = 2
Output: [1]



Example 4:

Input: root = [1,null,2], low = 1, high = 3
Output: [1,null,2]



Example 5:

Input: root = [1,null,2], low = 2, high = 4
Output: [2]
 

Constraints:

The number of nodes in the tree in the range [1, 104].
0 <= Node.val <= 104
The value of each node in the tree is unique.
root is guaranteed to be a valid binary search tree.
0 <= low <= high <= 104

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        
        if not root:
            # empty node or empty tree
            return None
        
        else:
            
            if root.val < L : 
                # root and left sub-tree is out of lower bound L
                # trim and keep right-subtree
                return self.trimBST(root.right, L, R)
            
            elif root.val > R :
                # root and right sub-tree is out of upper bound R
                # trim and keep left-subtree
                return self.trimBST(root.left, L, R)
                
            else:
                # root is in range
                # trim both left and right sub-tree
                root.left = self.trimBST( root.left, L, R)
                root.right = self.trimBST( root.right, L, R)

                return root


## Time Complexity: O( n )
#
# The overhead in time is the cost of DFS, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for recursion call stack, which is of O( n )

# ----------------------------------
def inorder( node ):

    if node:

        yield from inorder( node.left )
        yield node.val
        yield from inorder( node.right )

# ----------------------------------


import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        root = TreeNode( 1 )
        root.left = TreeNode( 0 )
        root.right = TreeNode( 2 )

        root_of_trim = Solution().trimBST( root=root, L=1, R=2 )

        result = [ *inorder( root_of_trim ) ]
        self.assertEqual( result, [1, 2])


    def test_case_2( self ):

        root = TreeNode( 3 )
        root.left = TreeNode( 0 )
        root.right = TreeNode( 4 )
        root.left.right = TreeNode( 2 )
        root.left.right.left = TreeNode( 1 )

        root_of_trim = Solution().trimBST( root=root, L=1, R=3 )

        result = [ *inorder( root_of_trim ) ]
        self.assertEqual( result, [1, 2, 3])


    def test_case_3( self ):

        root = TreeNode( 1 )
        
        root_of_trim = Solution().trimBST( root=root, L=1, R=2 )

        result = [ *inorder( root_of_trim ) ]
        self.assertEqual( result, [1] )


    def test_case_4( self ):

        root = TreeNode( 1 )
        root.right = TreeNode( 2 )
        
        root_of_trim = Solution().trimBST( root=root, L=1, R=3 )

        result = [ *inorder( root_of_trim ) ]
        self.assertEqual( result, [1, 2] )


    def test_case_5( self ):

        root = TreeNode( 1 )
        root.right = TreeNode( 2 )
        
        root_of_trim = Solution().trimBST( root=root, L=2, R=4 )

        result = [ *inorder( root_of_trim ) ]
        self.assertEqual( result, [2] )

if __name__ == '__main__':

    unittest.main()        
        