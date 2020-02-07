'''

Description:

Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level X such that the sum of all the values of nodes at level X is maximal.

 

Example 1:

Input: [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.
 

Note:

The number of nodes in the given tree is between 1 and 10^4.
-10^5 <= node.val <= 10^5

'''



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        
        traversal_queue = deque([ (root, 1) ])
        
        summation, max_sum = 0, -2**31
        cur_level, max_level = 0, 0
        
        # Level-order traversal
        while traversal_queue:
            
            size = len(traversal_queue)
            
            summation = 0
            
            # scan current level
            for _ in range(size):
                
                cur_node, cur_level = traversal_queue.popleft()
            
                # update summation of current level
                summation += cur_node.val
                
                # append child node for next level
                if cur_node.left:
                    traversal_queue.append( [cur_node.left, cur_level+1] )
                    
                if cur_node.right:
                    traversal_queue.append( [cur_node.right, cur_level+1] )
            
            # update maximum level summation
            if summation > max_sum:
                max_sum = summation
                max_level = cur_level
            
        return max_level



# n : the number of nodes in binary tree

## Time Complexity: O( n )
#
# The overhead in time is the cost of level-order traversal, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for traversal_queue, which is of O( n )


def test_bench():

    root = TreeNode(1)
    
    root.left = TreeNode(7)
    root.right = TreeNode(0)

    root.left.left = TreeNode(7)
    root.left.right = TreeNode(-8)

    print( Solution().maxLevelSum(root) )

    return 



if __name__ == '__main__':

    test_bench()