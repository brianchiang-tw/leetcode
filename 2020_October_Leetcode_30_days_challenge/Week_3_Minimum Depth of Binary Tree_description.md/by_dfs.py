'''

Description:

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        
        if root is None:
            # empty node or empty tree
            #print("leaf node reutrn 0" )
            return 0
        
        if root.left is None and root.right is None:
            # leaf node
            #print("Node{} reutrn 1".format(root.val) )
            return 1
        
        else:
            # non-leaf node
            
            if root.left is not None and root.right is not None:
                # both left and right sub-tree are non-empty
                return min( self.minDepth(root.left), self.minDepth(root.right) ) + 1
            
            elif root.left is None:
                # with right sub-tree only 
                return self.minDepth(root.right) + 1
            
            else:
                #with left sub-tree only
                return self.minDepth(root.left) + 1
            

# N : the number of nodes in binary tree with given root

## Time Complexity: O( N )
#
# Use in-order like traversal to visit each node recursively, each node is visited once.
# Overall time cost is of O( N )

## Space Complexity: O( N )
#
# The major overhead is to maintain stack variable to recurvisely traverse each node, which takes O( N ) for whole tree.


def test_bench():

    # 1st test-case
    '''
    
    Example:

    Given binary tree [3,9,20,null,null,15,7],

        3
       / \
      9  20
        /  \
       15   7
    return its minimum depth = 2.
    
    '''

    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)

    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    # expected output:
    '''
    2   
    '''
    print( Solution().minDepth(root) )



    # 2nd test-case
    # empty tree
    root = None

    # expected output:
    '''
    0   
    '''
    print( Solution().minDepth(root) )



    # 3rd test-case
    # right-skew tree
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)

    # expected output:
    '''
    3   
    '''
    print( Solution().minDepth(root) )



if __name__ == '__main__':

    test_bench()