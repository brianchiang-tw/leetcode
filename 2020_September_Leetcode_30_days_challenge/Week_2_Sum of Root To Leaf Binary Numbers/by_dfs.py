'''

Description:

You are given the root of a binary tree where each node has a value 0 or 1.  Each root-to-leaf path represents a binary number starting with the most significant bit.  For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.

For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.

Return the sum of these numbers. The answer is guaranteed to fit in a 32-bits integer.

 

Example 1:


Input: root = [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22



Example 2:

Input: root = [0]
Output: 0



Example 3:

Input: root = [1]
Output: 1



Example 4:

Input: root = [1,1]
Output: 3
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
Node.val is 0 or 1.

'''



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        
        
        # -------------------------
        
        def dfs(node, cur_num):
            
            if node:
                
                cur_num = cur_num * 2 + node.val
                
                if not node.left and not node.right:
                    
                    # stop condition on leaf node
                    yield cur_num
                    return
                
                
                # geneal cases
                
                yield from dfs(node.left, cur_num)
                yield from dfs(node.right, cur_num)
        
        # --------------------------
        
        return sum( dfs(node=root, cur_num=0) )



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

        root = TreeNode(1)

        root.left = TreeNode( 0 )
        root.right = TreeNode( 1 )

        root.left.left = TreeNode( 0 )
        root.left.right = TreeNode( 1 )
        root.right.left = TreeNode( 0 )
        root.right.right = TreeNode( 1 )

        result = Solution().sumRootToLeaf( root )
        self.assertEqual(result, 22)


if __name__ == '__main__':

    unittest.main()        