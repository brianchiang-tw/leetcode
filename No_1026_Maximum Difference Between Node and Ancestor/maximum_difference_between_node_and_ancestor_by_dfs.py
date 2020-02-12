'''

Description:

Given the root of a binary tree, find the maximum value V for which there exists different nodes A and B where V = |A.val - B.val| and A is an ancestor of B.

(A node A is an ancestor of B if either: any child of A is equal to B, or any child of A is an ancestor of B.)

 

Example 1:



Input: [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation: 
We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.
 

Note:

The number of nodes in the tree is between 2 and 5000.
Each node will have value between 0 and 100000.

'''



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        
        self.max_diff = 0
        
        def helper( node: TreeNode, min_val: int, max_val: int ):
            
            if not node:
                # empty node or empty tree
                return
            
            # update maximal difference by max value and min value of ancestors
            self.max_diff = max( self.max_diff, abs(node.val-min_val), abs(node.val-max_val) )
            
            # update min value of ancestors
            min_val = min( min_val, node.val )
            
            # update max value of ancestors
            max_val = max( max_val, node.val )
            
            # DFS on left sub-tree
            helper( node.left, min_val, max_val )
            
            # DFS on right sub-tree
            helper( node.right, min_val, max_val )
        
            return
        #----------------------------------------------
        
        # DFS on root node
        helper( root, root.val, root.val )
        
        return self.max_diff



# n : the number of nodes in binary tree

## Time Complexity: O( n )
#
# The overhead in time is the cost of pre-order DFS traversal, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for recursion call stack, which is of O( n )



def test_bench():

    root = TreeNode( 8 )
    root.left = TreeNode( 3 )
    root.right = TreeNode( 10 )

    root.left.left = TreeNode( 1 )
    root.left.right = TreeNode( 6 )
    root.right.right = TreeNode( 14 )

    root.left.right.left = TreeNode( 4 )
    root.left.right.right = TreeNode( 7 )
    root.right.right.left = TreeNode( 13 )

    print( Solution().maxAncestorDiff(root ) )

    return 



if __name__ == '__main__':

    test_bench()