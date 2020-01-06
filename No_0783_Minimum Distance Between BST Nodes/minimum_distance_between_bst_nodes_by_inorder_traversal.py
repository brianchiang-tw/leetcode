'''

Description:

Given a Binary Search Tree (BST) with the root node root, return the minimum difference between the values of any two different nodes in the tree.

Example :

Input: root = [4,2,6,1,3,null,null]
Output: 1
Explanation:
Note that root is a TreeNode object, not an array.

The given tree [4,2,6,1,3,null,null] is represented by the following diagram:

          4
        /   \
      2      6
     / \    
    1   3  

while the minimum difference in this tree is 1, it occurs between node 1 and node 2, also between node 3 and node 2.
Note:

The size of the BST will be between 2 and 100.
The BST is always valid, each node's value is an integer, and each node's value is different.

'''



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List
class Solution:
    
    
    def helper(self, node: TreeNode, arr:List[int])->int :
        # in-order traversal
        
        if node:
            
            self.helper( node.left, arr )
            
            arr.append( node.val )
            
            self.helper( node.right, arr )
            
    
    
    def minDiffInBST(self, root: TreeNode) -> int:
        
        arr = []
        
        # in-order traversal, convert BST to sorted array
        self.helper(root, arr)
        
        
        min_diff = 2 **31
        
        for i in range(1, len(arr)):            
            min_diff = min( min_diff, arr[i]-arr[i-1] )
            
        return min_diff
                
# n : the number of nodes in binary search tree

## Time Complexity : O( n )
#
# The overhead in time is the in-order-traversal of binary search tree, which is of O( n ).

## Space Complexity : O( m )
#
# The overhead in space is the call stack for recursion and array, arr, which are both of O( n ).




def test_bench():

    root = TreeNode( 4 )
    root.left = TreeNode( 2 )
    root.left.left = TreeNode( 1 )
    root.left.right = TreeNode( 3 )
    root.right = TreeNode( 6 )


    print( Solution().minDiffInBST(root ) )

    return 



if __name__ == '__main__':

    test_bench()
