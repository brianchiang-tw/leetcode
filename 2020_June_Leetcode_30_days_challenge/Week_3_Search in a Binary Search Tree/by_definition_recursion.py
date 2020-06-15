'''

Description:

Given the root node of a binary search tree (BST) and a value. You need to find the node in the BST that the node's value equals the given value. Return the subtree rooted with that node. If such node doesn't exist, you should return NULL.

For example, 

Given the tree:
        4
       / \
      2   7
     / \
    1   3

And the value to search: 2
You should return this subtree:

      2     
     / \   
    1   3
In the example above, if we want to search the value 5, since there is no node with value 5, we should return NULL.

Note that an empty tree is represented by NULL, therefore you would see the expected output (serialized tree format) as [], not null.

'''



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        
        if root is None:
            # miss
            return None
			
        else:
            if root.val == val: 
                # hit
                return root
				
            elif root.val > val: 
				# val is smaller than current node value, serach left sub-tree
                return self.searchBST(root.left, val)
				
            else:
				# val is larger than current node value, serach left sub-tree
                return self.searchBST(root.right, val)



# n : the number of nodes in binary search tree

## Time Complexity: O( n )
#
# The overhead in time is the cost of tree height, which is of O( n ), in the worst case of skewed tree.

## Space Complexity: O( n )
#
# The overhead in space is the storage for recursion call stack, which is of O( n ). 


import unittest

class Testing(unittest.TestCase):

    def test_case_1(self):

        root = TreeNode(4)
        
        root.left = TreeNode(2)
        root.right = TreeNode(7)

        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)

        result = Solution().searchBST( root, 2 )

        self.assertEqual( result.val, 2)
        self.assertEqual( result.left.val, 1)
        self.assertEqual( result.right.val, 3)


    def test_case_2(self):
    
        root = TreeNode(4)
        
        root.left = TreeNode(2)
        root.right = TreeNode(7)

        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)

        result = Solution().searchBST( root, 7 )

        self.assertEqual( result.val, 7)
        self.assertEqual( result.left, None)
        self.assertEqual( result.right, None)



if __name__ == '__main__':

    unittest.main()