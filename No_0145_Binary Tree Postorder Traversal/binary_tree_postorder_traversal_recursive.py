'''

Description:

Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?

'''

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        
        traversal_path = []
        if not root:
            # empty node or empty tree
            return []

        else:
            # DFS with postorder 
            # right child, left child, current node
            traversal_path.extend( self.postorderTraversal( root.left ) )
            traversal_path.extend( self.postorderTraversal( root.right ) )
            
            traversal_path.append( root.val )
            
        return traversal_path



# N : number of nodes in binary tree

## Time Complexity: O( N )
#
# The overhead in time is the recursion call, iterating every node with postorder.
# Each single visit on one node takes O( 1 ), total n nodes takes O( N ).

## Space Complexity: O( N )
#
# The overhead in space is to maintain call stack for recursion.
# The worst case is O( N ) of left-skew tree or right-skew tree.



def test_bench():

    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    path_of_postorder = Solution().postorderTraversal( root )

    # expected output:
    '''
    [3, 2, 1]
    '''

    print( path_of_postorder )

    return 



if __name__ == '__main__':

    test_bench()