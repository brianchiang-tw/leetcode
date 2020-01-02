# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import List

class Solution:
    
    def __init__(self):
        self.inorder = []
    
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        if root :
            
            self.inorderTraversal( root.left )
            self.inorder.append( root.val )
            self.inorderTraversal( root.right) 
            
            return self.inorder
        
        else:
            return []


# N : number of node in binary tree with given root

## Time Complexity:
#
# Inorder traversal visits each node once, every single visit costs O(1).
# There are n nodes in binary tree, thus totally it takes O( n ).

## Space Complexity:
#
# The overhead in time is to maintain call stack for inorder traversal,
# the call depth is O( n ) at most.

def test_bench():

    root = TreeNode(1)

    root.right = TreeNode(2)

    root.right.left = TreeNode(3)

    in_order_traversal = Solution().inorderTraversal(root)

    # expected output:
    '''
    [1, 3, 2]
    '''
    print( in_order_traversal )


    return



if __name__ == '__main__':

    test_bench()