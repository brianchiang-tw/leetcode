'''

Description:

You are given the root of a binary search tree (BST), where exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

Follow up: A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?

 

Example 1:


Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]
Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.



Example 2:


Input: root = [3,1,4,null,null,2]
Output: [2,1,4,null,null,3]
Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.
 

Constraints:

The number of nodes in the tree is in the range [2, 1000].
-231 <= Node.val <= 231 - 1

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right




class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        stack = [(root, 'init')] if root else []
        
        prev, first_error, second_error = None, None, None
        
        while stack:
            
            cur, state = stack.pop()
            
                
            if state == 'center':
                
                # catch error node during in-order traversal
                if not first_error and prev and prev.val > cur.val:
                    first_error = prev
                    
                if first_error and prev and prev.val > cur.val:
                    second_error = cur
                        
                prev = cur
                
            else:
                
                # in-order traversal with stack
                if cur.right: stack.append( (cur.right, 'right') )
                stack.append( (cur, 'center') )
                if cur.left: stack.append( (cur.left, 'left') )
            
        
        # recover binary search tree with correct value by swap
        first_error.val, second_error.val = second_error.val, first_error.val
        
        return



# n : the number of nodes in binary search tree

## Time Complexity: O( n )
#
# The overhead in time is the cost of inorder traversal, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for recursion call stack, which is of O( n )


def inorder( node ):

    if node:

        yield from inorder( node.left )
        yield node.val
        yield from inorder( node.right )


import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):
        
        root = TreeNode(1)
        root.left = TreeNode(3)
        root.left.right = TreeNode(2)
        
        Solution().recoverTree(root=root)
        result = [ *inorder(node=root) ]
        self.assertEqual(result, [1,2,3] )


    def test_case_2( self ):
        
        root = TreeNode(3)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        root.right.left = TreeNode(2)
        
        Solution().recoverTree(root=root)
        result = [ *inorder(node=root) ]
        self.assertEqual(result, [1,2,3,4] )



if __name__ == '__main__':

    unittest.main()        