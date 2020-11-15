'''

Description:

Given the root of a binary tree, find the maximum value V for which there exist different nodes A and B where V = |A.val - B.val| and A is an ancestor of B.

A node A is an ancestor of B if either: any child of A is equal to B, or any child of A is an ancestor of B.

 

Example 1:


Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation: We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.



Example 2:


Input: root = [1,null,2,null,0,3]
Output: 3
 

Constraints:

The number of nodes in the tree is in the range [2, 5000].
0 <= Node.val <= 105

Hint #1  
For each subtree, find the minimum value and maximum value of its descendants.

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        
        def dfs( node, anc_max, anc_min ):
            
            if not node:
                
                ## base case aka stop condition
                # empty node or empty subtree
                return
            
            
            ## general case
            
            # update maximum difference between current node and ancestor
            dfs.max_diff = max(dfs.max_diff, abs(anc_max-node.val), abs(anc_min-node.val))
            
            # update maximum of ancestor
            anc_max = max(anc_max, node.val)
            
            # update minimum of ancestor
            anc_min = min(anc_min, node.val)
            
            # DFS down to next level
            dfs(node.left, anc_max, anc_min)
            dfs(node.right, anc_max, anc_min)
            
        # -------------------------------------
        
        # initialization
        dfs.max_diff = 0
        dfs(node=root, anc_max=root.val, anc_min=root.val)
        return dfs.max_diff


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
        
        root = TreeNode( 8 )
        root.left = TreeNode( 3 )
        root.right = TreeNode( 10 )
        root.left.left = TreeNode( 1 )
        root.left.right = TreeNode( 6 )
        root.left.right.left = TreeNode( 4 )
        root.left.right.right = TreeNode( 7 )
        root.right.right = TreeNode( 14 )
        root.right.right.left = TreeNode( 13 )
        
        result = Solution().maxAncestorDiff( root )
        self.assertEqual(result, 7)


    def test_case_2( self ):

        root = TreeNode( 1 )
        root.right = TreeNode( 2 )
        root.right.right = TreeNode( 0 )
        root.right.right.left = TreeNode( 3 )


if __name__ == '__main__':

    unittest.main()        
