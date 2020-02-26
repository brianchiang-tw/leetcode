'''

Description:

Given a binary tree, return the tilt of the whole tree.

The tilt of a tree node is defined as the absolute difference between the sum of all left subtree node values and the sum of all right subtree node values. Null node has tilt 0.

The tilt of the whole tree is defined as the sum of all nodes' tilt.



Example:

Input: 
         1
       /   \
      2     3

Output: 1

Explanation: 

Tilt of node 2 : 0
Tilt of node 3 : 0
Tilt of node 1 : |2-3| = 1
Tilt of binary tree : 0 + 0 + 1 = 1



Note:

The sum of node values in any subtree won't exceed the range of 32-bit integer.
All the tilt values won't exceed the range of 32-bit integer.

'''



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        
        tilt_sum = 0
        
        def helper( node: TreeNode):
            
            if not node:
                return 0
            
            else:
                
                left_sum = helper(node.left)
                right_sum = helper(node.right)
                
                nonlocal tilt_sum
                tilt_sum += abs(left_sum - right_sum)
                return left_sum + node.val + right_sum
        
        # ---------------------------------------------
        
        helper( root )
        return tilt_sum



# n : the number of nodes in binary tree

## Time Complexity: O( n )
#
# The overhead in time is the cost of post-order traversal, which is of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the storage for recursion call stack, which is of O( n ).


def test_bench():

    ## Test case_#1
    root_1 = TreeNode(1)
    root_1.left = TreeNode(2)
    root_1.right = TreeNode(3)

    # expected output:
    '''
    1
    '''
    print( Solution().findTilt(root_1))


    ## Test case_#2
    root_2 = TreeNode(1)
    root_2.left = TreeNode(2)
    root_2.right = TreeNode(3)

    root_2.left.left = TreeNode(4)
    root_2.left.right = TreeNode(5)

    # expected output:
    '''
    9
    '''
    print( Solution().findTilt(root_2))



if __name__ == '__main__':

    test_bench()