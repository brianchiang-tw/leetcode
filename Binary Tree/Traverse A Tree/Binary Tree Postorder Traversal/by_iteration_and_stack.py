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



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



from typing import List

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:

        
        path = []
        
        traversal_stack = [ (root, 'init') ]
        
        while traversal_stack:
            
            cur_node, cur_label = traversal_stack.pop()
            
                
            if cur_node:
                
                if cur_label == 'c':
                    path.append( cur_node.val )
                    
                else:    
                    traversal_stack.append( (cur_node, 'c') )
                    traversal_stack.append( (cur_node.right, 'r') )
                    traversal_stack.append( (cur_node.left, 'l') )
                
        return path



# n : the number of nodes in binary tree

## Time Compliexty: O( n )
#
# The overhead in time is the cost of DFS traversal, which is of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the storage for recursion call stack and the storage for output list, path, of order O( n ).



def test_bench():

    root = TreeNode( 1 )
    root.right = TreeNode( 2 )
    root.right.left = TreeNode( 3 )

    # expected output:
    '''
    [3, 2, 1]
    '''
    print( Solution().postorderTraversal( root ) )



if __name__ == '__main__':

    test_bench()