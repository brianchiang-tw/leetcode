# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:

        global_max = -2**31
        
        def helper(node: TreeNode):
            
            if not node:
                return 0
            
            nonlocal global_max
            left = max( helper( node.left ), 0 )
            right = max( helper( node.right), 0 )
            
            # use current node as bridge, update if sum of connection is bigger than global_max
            global_max = max( global_max, left + right + node.val )
            
            # update local max, either left node or right node.
            local_max = max( left, right ) + node.val
            return local_max
        
        helper( root )
        return global_max



# n : the number of nodes in binary tree

## Time Complexity: O( n )
#
# The overhead in time is the cost of post-order traversal, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for recursion call stack, which is of O( n )



def test_bench():

    root_1 = TreeNode( 1 )
    root_1.left = TreeNode( 2 )
    root_1.right = TreeNode( 3 )

    root_2 = TreeNode( -10 )

    root_2.left = TreeNode( 9 )
    root_2.right = TreeNode( 20 )

    root_2.right.left = TreeNode( 15 )
    root_2.right.right = TreeNode( 7 )

    test_data = [
                    root_1,
                    root_2
                ]

    # expected output:
    '''
    6
    42
    '''

    for t in test_data:

        print( Solution().maxPathSum( root = t ) )

    return



if __name__ == '__main__':

    test_bench()