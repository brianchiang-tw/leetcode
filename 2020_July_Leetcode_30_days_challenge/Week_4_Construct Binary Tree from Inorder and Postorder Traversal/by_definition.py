'''

Description:

Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import List
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        
        val_index_dict = { val: idx for idx, val in enumerate(inorder) }
        
        def helper( left, right ):
            
            if left > right:
                # Base case
                return None
            
            else:
                
                root = TreeNode(postorder.pop())
                
                mid = val_index_dict[root.val]
                
                root.right =  helper(mid+1, right)
                root.left = helper(left, mid-1)
                
                return root
            
        #------------------------------------------------------------------------
        
        return helper(left=0, right=len(inorder)-1)



# n : the number of nodes in binary tree

## Time Complexity: O( n )
#
# The overhead in time is the cost of T(n) = 2T(n/2) + O( 1 ) = O( n )

## Space Complexity: O( n )
#
# The overhead in space is the storage of recursion call stack, which is of O( n )


def inorder_traversal(node):

    if node:
        yield from inorder_traversal(node.left)
        yield node.val
        yield from inorder_traversal(node.right)


def postorder_traversal(node):
    
    if node:
        yield from postorder_traversal(node.left)
        yield from postorder_traversal(node.right)
        yield node.val



import unittest
class Testing(unittest.TestCase):

    def test_case_1(self):

        root = Solution().buildTree(inorder = [9,3,15,20,7],postorder = [9,15,7,20,3])
        inorder_visit = [*inorder_traversal(root)]
        self.assertEqual(inorder_visit,  [9,3,15,20,7])

        postorder_visit = [*postorder_traversal(root)]
        self.assertEqual(postorder_visit, [9,15,7,20,3])


if __name__ == '__main__':

    unittest.main()