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
        
        traversal_stack = [ root ] if root else []
        in_order_path = []
        
        while traversal_stack:
            
            cur_node = traversal_stack.pop()
            
            
            in_order_path.append( cur_node.val )
            
            if cur_node.right:
                traversal_stack.append( cur_node.right )
            
            if cur_node.left:
                traversal_stack.append( cur_node.left )

        return in_order_path



# n : the number of nodes in binary tree

## Time Complexity: O( n )
#
# The overhead in time is the cost of DFS traversal, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for stack and path tracker list, in_order_path, which are of O( n )



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