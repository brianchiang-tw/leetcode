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
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:

        if not root :
            # Base case:
            # Empty node
            return 0

        left = self.minDepth( root.left )
        right = self.minDepth( root.right )

        if left and right:
            return min(left, right)+1
        elif left:
            return left+1
        elif right:
            return right+1
        else:
            return 1



# n : the number of nodes in binary trees

## Time Complexity: O( n )
#
# The overhead in time is the cost of DFS, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for call stack, which is of O( n )



def test_bench():

    root = TreeNode( 3 )

    root.left = TreeNode( 9 )
    root.right = TreeNode( 20 )

    root.right.left = TreeNode( 15 )
    root.right.right = TreeNode( 7 )

    # expected output:
    '''
    2
    '''
    print( Solution().minDepth( root ) )

    # ----------------------------------------

    root = TreeNode( 2 )
    
    root.left = TreeNode( 1 )
    root.right = TreeNode( 3 )

    # expected output:
    '''
    2
    '''
    print( Solution().minDepth( root ) )

    # ----------------------------------------

    root = TreeNode( 2 )

    # expected output:
    '''
    1
    '''
    print( Solution().minDepth( root ) )

    # ----------------------------------------

    root = None

    # expected output ( test for empty tree ):
    '''
    0
    '''
    print( Solution().minDepth( root ) )


if __name__ == '__main__':

    test_bench()