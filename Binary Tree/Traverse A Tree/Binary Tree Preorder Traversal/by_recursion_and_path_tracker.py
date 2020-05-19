'''

Description:

Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]

Follow up: Recursive solution is trivial, could you do it iteratively?

'''



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



from typing import List

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        
        def dfs( node: TreeNode, path: List):
            
            if node:
                
                path.append( node.val )
                
                dfs( node.left, path )
                
                dfs( node.right, path )
                
        # ----------------------------------------
        
        in_order_path = []
        dfs( root, in_order_path )
        return in_order_path



# n : the number of nodes in binary tree

## Time Complexity: O( n )
#
# The overhead in time is the cost of DFS traversal, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for recursion stack, which is of O( n )



def test_bench():

    root = TreeNode( 1 )
    root.right = TreeNode( 2 )
    root.right.left = TreeNode( 3 )

    # expected output:
    '''
    [1, 2, 3]
    '''
    print( Solution().preorderTraversal( root ) )
    # --------------------------------------

    # expected output:
    '''
    []
    '''
    root = None
    print( Solution().preorderTraversal( root ) )

    return



if __name__ == '__main__':

    test_bench()    