'''

Description:

Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6



Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42

'''



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        
        self.max_path_sum = float('-inf')
        
        def helper( node: TreeNode ) -> int:
            
            if not node:
                return 0
            
            else:
                
                # discard negative path
                left = max( helper( node.left ), 0 )
                right = max( helper( node.right ), 0 )
                
                self.max_path_sum = max( self.max_path_sum, left + right + node.val )
                
                # choose the optimal path in subtree
                return max( left, right) + node.val
        
        # ------------------------------------------------
        helper( root )
        return self.max_path_sum






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