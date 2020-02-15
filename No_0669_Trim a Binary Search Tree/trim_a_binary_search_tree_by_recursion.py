'''

Description:

Given a binary search tree and the lowest and highest boundaries as L and R, trim the tree so that all its elements lies in [L, R] (R >= L). You might need to change the root of the tree, so the result should return the new root of the trimmed binary search tree.



Example 1:
Input: 
    1
   / \
  0   2

  L = 1
  R = 2

Output: 
    1
      \
       2



Example 2:
Input: 
    3
   / \
  0   4
   \
    2
   /
  1

  L = 1
  R = 3

Output: 
      3
     / 
   2   
  /
 1

'''



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        
        if not root:
            # empty node or empty tree
            return None
        
        else:
            
            if root.val < L : 
                # root and left sub-tree is out of range
                # trim and keep right-subtree
                return self.trimBST(root.right, L, R)
            
            elif root.val > R :
                # root and right sub-tree is out of range
                # trim and keep left-subtree
                return self.trimBST(root.left, L, R)
                
            else:
                # root is in range
                # trim both left and right sub-tree
                root.left = self.trimBST( root.left, L, R)
                root.right = self.trimBST( root.right, L, R)

                return root



# n : the number of nodes in binary tree

## Time Complexity: O(n)
#
# The overhead in time is the cost of DFS traversal, which is of O( n ).

## Space Complexity: O(n)
#
# The overhead in space is the storage for recursion call stack, which is of O( n ).


def inorder_print( node: TreeNode):

    if node:

        inorder_print( node.left )
        print(f'{node.val} ', end = '')
        inorder_print( node.right )



def test_bench():

    ## Testcase_#1
    root_1 = TreeNode(1)
    root_1.left = TreeNode(0)
    root_1.right = TreeNode(2)

    # before:
    # 0 1 2
    print('\n')
    inorder_print( root_1 )

    root_1 = Solution().trimBST( root_1, L = 1, R = 2 )
    print('\n')
    # after:
    # 1 2
    inorder_print( root_1 )



    ## Testcase_#2
    root_2 = TreeNode(3)
    root_2.left = TreeNode(0)
    root_2.right = TreeNode(4)

    root_2.left.right = TreeNode(2)
    root_2.left.right.left = TreeNode(1)

    # before:
    # 0 1 2 3 4
    print('\n')
    inorder_print( root_2 )

    root_2 = Solution().trimBST( root_2, L = 1, R = 3 )
    print('\n')
    # after:
    # 1 2 3
    inorder_print( root_2 )

    return



if __name__ == '__main__':

    test_bench()