# Definition for a binary tree node.
import sys

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    
    def validate_bst(self, root: TreeNode, min_bound:int, max_bound:int)-> bool:
        
        if root is None:
            return True
        
        else:
            
            
            if root.val > max_bound or root.val < min_bound:
                # check node value is of BST property, within valid range from min_bound to max_bound
                return False
            
                # check left subtree
            is_left_valid = self.validate_bst( root.left, min_bound, root.val-1 )
            
                # check right subtree
            is_right_valid = self.validate_bst( root.right, root.val+1, max_bound )
    
            return ( is_left_valid and is_right_valid )
    
    
    
    def isValidBST(self, root: TreeNode) -> bool:
        
        if root is None:
            return True
        
        return self.validate_bst( root, -sys.maxsize, sys.maxsize-1 )


# N : number of nodes in binary tree

## Time Complexity: O( N )
#
# Use divide and conquer to traversal each node exactly once, total N node, thus O( N )
#
# T( N ) = 2T( N / 2) + 1


## Space Complexity: O( N )
#
# O( 1 ) constant size variable in each run. And check every node by visiting once, thus O( N )



def test_bench():

    root_of_tree = TreeNode(5)

    root_of_tree.left = TreeNode(1)
    root_of_tree.right = TreeNode(4)
    root_of_tree.right.left = TreeNode(3)
    root_of_tree.right.right = TreeNode(6)

    is_bst = Solution().isValidBST( root_of_tree )

    # expected output:
    # False
    print( is_bst )

    root_of_tree = TreeNode(2)

    root_of_tree.left = TreeNode(1)
    root_of_tree.right = TreeNode(3)

    is_bst = Solution().isValidBST( root_of_tree )

    # expected output:
    # True
    print( is_bst )

    return


if __name__ == '__main__':

    test_bench()