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



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        if p and q:
            # General case:
            # Compare whole tree in DFS traversal

            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        elif not p and not q:
            # Base case:
            # Both p and q are empty

            return True
        
        else:

            # Base case:
            # Either p or q is empty, the other is non-empty.
            return False



# n : the number of nodes in binary tree

## Time Complexity: O( n )
#
# The overhead in time is the cost of DFS traversal, which is of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the storage for recursion call stack, which is of O( n ).



def test_bench():

    root_p = TreeNode( 1 )
    root_p.left = TreeNode( 2 )
    root_p.right = TreeNode( 3 )

    root_q = TreeNode( 1 )
    root_q.left = TreeNode( 2 )
    root_q.right = TreeNode( 3 )

    # expected output:
    '''
    True
    '''
    print( Solution().isSameTree( p = root_p, q= root_q ) )

    # ------------------------------------------------------

    root_p = TreeNode( 1 )
    root_p.left = TreeNode( 2 )

    root_q = TreeNode( 1 )
    root_q.right = TreeNode( 2 )

    # expected output:
    '''
    False
    '''
    print( Solution().isSameTree( p = root_p, q= root_q ) )



if __name__ == '__main__':

    test_bench()
