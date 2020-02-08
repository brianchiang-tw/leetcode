'''

Description:

Given a binary tree root and an integer target, delete all the leaf nodes with value target.

Note that once you delete a leaf node with value target, if it's parent node becomes a leaf node and has the value target, it should also be deleted (you need to continue doing that until you can't).

 

Example 1:



Input: root = [1,2,3,2,null,2,4], target = 2
Output: [1,null,3,null,4]
Explanation: Leaf nodes in green with value (target = 2) are removed (Picture in left). 
After removing, new nodes become leaf nodes with value (target = 2) (Picture in center).



Example 2:



Input: root = [1,3,3,3,2], target = 3
Output: [1,3,null,null,2]



Example 3:



Input: root = [1,2,null,2,null,2], target = 2
Output: [1]
Explanation: Leaf nodes in green with value (target = 2) are removed at each step.



Example 4:

Input: root = [1,1,1], target = 1
Output: []



Example 5:

Input: root = [1,2,3], target = 1
Output: [1,2,3]
 

Constraints:

1 <= target <= 1000
Each tree has at most 3000 nodes.
Each node's value is between [1, 1000].

'''




# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        
        def helper( node: TreeNode, target:int) -> bool:
            
            if not node:
                # base case:
                # empty node
                return True
            
            
            # DFS traversal on left sub-tree
            left_removal    = helper( node.left, target)
            
            # DFS traversal on right sub-tree
            right_removal   = helper( node.right, target)
            
            
            if left_removal and right_removal and node.val == target:
                # current node is leaf node, and with target value.
                # take current node as dummy node (like empty node)
                return True
            
            
            if left_removal:
                # remove leaf node with target value on the left
                node.left = None
            
            
            if right_removal:
                # remove left node with target value on the right
                node.right = None
            
            
            # current node is neither non-leaf node, nor leaf node without target value.
            return False
        
        
        #-------------------------------------------------------------
        
        
        if helper(root, target):
            # root is empty node naturally, or removed finally.
            return None
        else:
            # root still exists eventually
            return root



# n : the number of node in binary tree
# h : the height of binary tree

## Time Complexity: O( n )
#
# The overhead in time is the cost of post-oreder DFS traversal, which is of O( n ).

## Space Complexity: O( h )
#
# The overhead in space is the storage for recursion call stack, which is of O( h ).



def test_bench():

    def in_order_traversal( node ):

        if node:

            in_order_traversal( node.left )
            print(f'{node.val} ', end = '' )
            in_order_traversal( node.right )

    # --------------------------------------

    root = TreeNode(1)
    target = 2
    
    root.left = TreeNode(2)
    root.left.left = TreeNode(2)

    root.right = TreeNode(3)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(4)

    # expected output:
    '''
    1 3 4 
    '''
    Solution().removeLeafNodes( root, target )
    in_order_traversal( root )
    


if __name__ == '__main__':

    test_bench()