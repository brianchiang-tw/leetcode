'''

Description:

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        
        if root is None:
            return False
        
        else:
            if root.val == sum and root.left is None and root.right is None:
                return True

            else:

                has_left_path = self.hasPathSum( root.left, sum-root.val)
                has_right_path = self.hasPathSum( root.right, sum-root.val)
                
                return has_left_path or has_right_path

# N : the number of nodes in tree

## Time Complexity: O( N )
#
# Use tree travesal to visit each node with O(1) computaion and assignemnt till leaf node is reached.
# Cost at each function call is O(1), and each node is visit once, total cost is of O( N ).

## Space Complexity: O( N )
#
# The overhead at each function call is flag variable of O(1)
# And the cost of stack in recursion at each function call is O(1), and each node is visit once, total cost is O( N )