'''

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
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        if not root:
            # Empty tree or empty leaf node
            return 0
        
        else:
            
            # Choose the local longest path in DFS
            left = self.maxDepth( root.left )
            right = self.maxDepth( root.right )
            
            return max(left, right)+1



# n : the number of nodes in binary tree

## Time Complexity: O( n )
#
# The overhead in time is the cost of DFS traversal, which is of O( n )


## Space Complexity: O( n )
#
# The overhead in space is the storage for recursion call stack, which is of O( n )



def test_bench():

    root = TreeNode( 3 )

    root.left = TreeNode( 9 )
    root.right = TreeNode( 20 )

    root.right.left = TreeNode( 15 )
    root.right.right = TreeNode( 7 )

    # expected output:
    '''
    3
    '''

    print( Solution().maxDepth( root ) )




if __name__ == '__main__':

    test_bench()
