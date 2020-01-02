'''

Description:

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        if root is None:
            # empty node or empty tree
            return 0
        
        if root is not None and root.left is None and root.right is None:
            # leaf node
            return 1
        
        else:
            # non-leaf node
            return max( self.maxDepth(root.left), self.maxDepth(root.right) ) + 1



# N : number of nodes in tree with given root

## Time Complexity: O( N )
#
# Use in-order like traversal to visit each node recursively, each node is visited once.
# Overall time cost is of O( N )

## Space Complexity: O( N )
#
# The major overhead is to maintain stack variable to recurvisely traverse each node, which takes O( N ) for whole tree.


def test_bench():


    '''

    Example:

    Given binary tree [3,9,20,null,null,15,7],

        3
    / \
    9  20
        /  \
    15   7
    return its depth = 3.

    '''
    root = TreeNode(3)

    root.left = TreeNode(9)
    root.right = TreeNode(20)

    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    # expected output:
    '''
    3
    '''

    print( Solution().maxDepth(root) )

    return



if __name__ == '__main__':

    test_bench()
