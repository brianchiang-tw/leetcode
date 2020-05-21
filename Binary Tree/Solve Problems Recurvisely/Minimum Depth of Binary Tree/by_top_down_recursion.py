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

        self.min_depth = 2**31

        def helper( node: TreeNode, cur_depth: int):

            if not node:
                return
            
            if not node.left and not node.right:

                self.min_depth = min( self.min_depth, cur_depth )
                return

            helper( node.left, cur_depth+ 1 )
            helper( node.right, cur_depth+ 1 )

        # -----------------------------------

        helper( node = root, cur_depth = 1 )
        return self.min_depth if self.min_depth != 2**31 else 0






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