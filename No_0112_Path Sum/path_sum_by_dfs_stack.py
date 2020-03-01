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
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution:
    
    def hasPathSum(self, root, sum):
        
        traversal_stack = [(root, sum)]
        
        # DFS with stack
        while traversal_stack:
            
            node, value = traversal_stack.pop()
            
            if node:
                if not node.left and not node.right and node.val == value:
                    # leaf node
                    return True
                
                else:
                    # non-leaf node
                    traversal_stack.append((node.right, value-node.val))
                    traversal_stack.append((node.left, value-node.val))

            else:
                # empty node
                continue
                
        return False

# N : the number of nodes in tree

## Time Complexity: O( N )
#
# Use tree travesal to visit each node with O(1) computaion and assignemnt till leaf node is reached.
# Cost at each function call is O(1), and each node is visit once, total cost is of O( N ).

## Space Complexity: O( N )
#
# The overhead at each function call is flag variable of O(1)
# And the cost of stack in recursion at each function call is O(1), and each node is visit once, total cost is O( N )





def test_bench():


#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \      \
# 7    2      1
#
# sum = 22
#
# path sum = 5 + 4 + 11 + 2 = 22
    node_7 = TreeNode(7)
    node_2 = TreeNode(2)
    node_11 = TreeNode(11)
    node_11.left = node_7
    node_11.right = node_2

    node_13 = TreeNode(13)

    node_1 = TreeNode(1)
    node_4 = TreeNode(4)
    node_4.right = node_1

    node_8 = TreeNode(8)
    node_8.left = node_13
    node_8.right = node_4

    node_4 = TreeNode(4)
    node_4.left = node_11

    root = TreeNode(5)
    root.left = node_4
    root.right = node_8

    target_sum = 22

    # expected output:
    '''
    True
    '''
    print( Solution().hasPathSum(root, target_sum) )


if __name__ == '__main__':

    test_bench()