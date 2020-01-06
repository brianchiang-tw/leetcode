'''

Description:

Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.

 

Example 1:

Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32
Example 2:

Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23
 

Note:

The number of nodes in the tree is at most 10000.
The final answer is guaranteed to be less than 2^31.

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    def helper(self, node, L, R, arr):
        
        
        if node:
            
            
            if node.val > L:
                self.helper( node.left, L, R, arr )
            
            if R >= node.val >= L:
                arr.append( node.val )
            
            if node.val < R:
                self.helper( node.right, L, R, arr )
    
    
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        
        arr = []
        
        self.helper(root, L, R, arr)
        
        return sum( arr )



# n : the number of node in given binary search tree

## Time Complexity: O( n )
#
# The overhead in time is to traversal the binary search tree within range, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the call stack for recursion and array, arr, which are both of O( n )



def test_bench():
    
    root = TreeNode( 10 )

    root.left = TreeNode( 5 )
    root.right = TreeNode( 15 )

    root.left.left = TreeNode( 3 )
    root.left.right = TreeNode( 7 )

    root.right.left = None 
    root.right.right = TreeNode( 18 )

    L, R = 7, 15 

    print( Solution().rangeSumBST(root, L, R) )

    return 



if __name__ == '__main__':

    test_bench()