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

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        
        traversal_path = []
        
        stack_preorder = [ root ]
        
        while stack_preorder:
            
            current = stack_preorder.pop()
            
            if current:
                
                # DFS with preorder:
                # current, current.left, current.right   
            
                traversal_path.append( current.val )
                
                # left is of higher priority than right, 
                # thus push right before left
                stack_preorder.append( current.right ) 
                stack_preorder.append( current.left ) 
                        
        return traversal_path



# N : the number of elements in binary tree

## Time Complexity: O( N )
#
# The overhead in time is to visit each node once, each visit take O( 1 ), total n nodes.
# Totally it takes O( N ) to complete a preorder traversal from root.

## Space Complexity: O( N )
#
# The overhead in time is to maintain a stack for DFS pre-order traversal.
# It takes O( N ) at most on worst case of left-skew tree or right-skew tree. 


def test_bench():

    '''
    Example:

    Input: [1,null,2,3]
        1
          \
           2
          /
         3

    '''

    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    traversal_path = Solution().preorderTraversal( root )


    # expected output:
    '''
    [1, 2, 3]
    '''

    print( traversal_path )

    return



if __name__ == '__main__':

    test_bench()