'''

Description:

Find the sum of all left leaves in a given binary tree.

Example:

     3
    / \
   9  20
     /  \
    15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.

'''



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        
        def helper( node: TreeNode):
            
            if node:

                if node.left and not node.left.left and not node.left.right:
                    # Catch one left leaf node
                    yield node.left.val
                
                if node.left:
                    yield from helper( node.left )                                    
                
                if node.right:
                    yield from helper( node.right )
                    
                        
            else:
                return

        # --------------------------------------------------
        
        return sum( helper( root ) )



# n : the number of node in binary tree

## Time Complexity: O( n )
#
# The overhead in time is the cost of DFS traversal, which is of O( n ).

## Sapce Complexity: O( n )
#
# The overhead in space is the cost of recursion call stack, which is of O( n ).



def test_bench():

    root = TreeNode( 3 )
    
    root.left = TreeNode( 9 )
    root.right = TreeNode( 20 )

    root.right.left = TreeNode( 15 )
    root.right.right = TreeNode( 7 )

    # expected output:
    '''
    24
    '''

    print( Solution().sumOfLeftLeaves( root = root ) )



if __name__ == '__main__':

    test_bench()