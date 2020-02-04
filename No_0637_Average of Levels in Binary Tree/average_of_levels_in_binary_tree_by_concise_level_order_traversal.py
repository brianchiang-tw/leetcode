'''

Description:

Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
Note:
The range of node's value is in the range of 32-bit signed integer.

'''



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque

from typing import List
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        
        
        if not root:
            # Quick response for empty tree
            return []
        
        queue = deque([root])
        
        average_of_level = []
        
        while queue:
            
            # valid nodes on current level
            size = len(queue)
            
            totalSum = 0
            
            for _ in range(size):
                
                # pop one node from traversal queue
                node = queue.popleft()
                
                # accumulate sum of current level
                totalSum += node.val
                
                # add left child if it exists
                if node.left:
                    queue.append(node.left)
                    
                # add right child if it exists
                if node.right:
                    queue.append(node.right)
            
            # add current level's average value to list
            average_of_level.append(totalSum/size)
        
        return average_of_level



# n : the number of nodes in binary tree
# h : the height of binary tree

## Time Complexity: O( n )
#
# The overhead in time is the level-order traversal, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the the storage for queue, which is of O( n ), and
# the storage for average_of_level, which is of O( h )
# It takes O( n + h ) = O( n ) in total.



def test_bench():

    root = TreeNode(3)

    root.left = TreeNode(9)
    root.right = TreeNode(20)

    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    # expected output:
    '''
    [3.0, 14.5, 11.0]
    '''
    print( Solution().averageOfLevels(root) )



if __name__ == '__main__':

    test_bench()