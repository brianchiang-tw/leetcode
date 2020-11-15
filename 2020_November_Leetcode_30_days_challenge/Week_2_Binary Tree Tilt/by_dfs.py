'''

Description:

Given the root of a binary tree, return the sum of every tree node's tilt.

The tilt of a tree node is the absolute difference between the sum of all left subtree node values and all right subtree node values. If a node does not have a left child, then the sum of the left subtree node values is treated as 0. The rule is similar if there the node does not have a right child.

 

Example 1:


Input: root = [1,2,3]
Output: 1
Explanation: 
Tilt of node 2 : |0-0| = 0 (no children)
Tilt of node 3 : |0-0| = 0 (no children)
Tile of node 1 : |2-3| = 1 (left subtree is just left child, so sum is 2; right subtree is just right child, so sum is 3)
Sum of every tilt : 0 + 0 + 1 = 1



Example 2:


Input: root = [4,2,9,3,5,null,7]
Output: 15
Explanation: 
Tilt of node 3 : |0-0| = 0 (no children)
Tilt of node 5 : |0-0| = 0 (no children)
Tilt of node 7 : |0-0| = 0 (no children)
Tilt of node 2 : |3-5| = 2 (left subtree is just left child, so sum is 3; right subtree is just right child, so sum is 5)
Tilt of node 9 : |0-7| = 7 (no left child, so sum is 0; right subtree is just right child, so sum is 7)
Tilt of node 4 : |(3+5+2)-(9+7)| = |10-16| = 6 (left subtree values are 3, 5, and 2, which sums to 10; right subtree values are 9 and 7, which sums to 16)
Sum of every tilt : 0 + 0 + 0 + 2 + 7 + 6 = 15



Example 3:


Input: root = [21,7,14,1,1,2,2,3,3]
Output: 9
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-1000 <= Node.val <= 1000

Hint #1  
Don't think too much, this is an easy problem. Take some small tree as an example.

Hint #2  
Can a parent node use the values of its child nodes? How will you implement it?

Hint #3  
May be recursion and tree traversal can help you in implementing.

Hint #4  
What about postorder traversal, using values of left and right childs?

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def findTilt(self, root: TreeNode) -> int:
        
        
        def helper( node: TreeNode)-> tuple:
            
            if not node:
                return 0, 0
            
            else:
                
                left_sum, left_tilt = helper(node.left)
                right_sum, right_tilt = helper(node.right)
                             
                current_tilt = abs(left_sum - right_sum)
                return ( (left_sum + node.val + right_sum), (left_tilt + current_tilt + right_tilt) )
        
        # ---------------------------------------------
        # first return item is the sum of current subtree
        # second return item is the tile of current subtree
        return helper(root)[1]


# n : the number of nodes in binary tree

## Time Complexity: O( n )
#
# The overhead in time is the cost of DFS, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for recursion stack, which is of O( n )




import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        root = TreeNode( 1 )
        root.left = TreeNode( 2 )
        root.right = TreeNode( 3 )

        result = Solution().findTilt(root)
        self.assertEqual(result, 1)


    def test_case_2( self ):

        root = TreeNode( 4 )
        root.left = TreeNode( 2 )
        root.right = TreeNode( 9 )
        root.left.left = TreeNode( 3 )
        root.left.right = TreeNode( 5 )
        root.right.right = TreeNode( 7 )

        result = Solution().findTilt( root )
        self.assertEqual(result, 15)


    def test_case_3( self ):

        root = TreeNode( 21 )
        root.left = TreeNode( 7 )
        root.right = TreeNode( 14 )
        root.left.left = TreeNode( 1 )
        root.left.right = TreeNode( 1 )
        root.right.left = TreeNode( 2 )
        root.right.right = TreeNode( 2 )
        root.left.left.left = TreeNode( 3 )
        root.left.left.right = TreeNode( 3 )

        result = Solution().findTilt( root )
        self.assertEqual(result, 9)


if __name__ == '__main__':

    unittest.main()        
