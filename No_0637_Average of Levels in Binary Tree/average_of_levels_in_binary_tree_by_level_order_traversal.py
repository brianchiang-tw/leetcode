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
        
        # level order traversal queue
        traversal_queue = deque( [ (root, 0) ] )
        
        # output list for average of levels
        average_of_levels = []
        
        # a list to record values on current level
        cur_level_value = []
        
        # initialization to upmost level 0
        prev_level = 0
        
        # level oreder traversal
        while traversal_queue:
            
            
            cur_node, cur_level = traversal_queue.popleft()
            
            
            if not cur_node:
                continue
                
            else:
                
                # handle for going down to next level
                if cur_level != prev_level:
                    
                    # update previous level's average, save it to list
                    average_of_levels.append( sum(cur_level_value) / len(cur_level_value) )
                    
                    # clear old data
                    cur_level_value.clear()
                    
                
                # add value of current node to the list, cur_level_value 
                cur_level_value.append( cur_node.val )
                
                # add left child to traversal queue
                traversal_queue.append( (cur_node.left, cur_level+1) )
                
                # add right child to traversal queue
                traversal_queue.append( (cur_node.right, cur_level+1) )
                
                # update prev_level as current level
                prev_level = cur_level
        
        
        # corner case handle for last level
        average_of_levels.append( sum(cur_level_value) / len(cur_level_value) )
                    
        cur_level_value.clear()
        
        return average_of_levels



# n : the number of nodes in binary tree
# h : the height of binary tree

## Time Complexity: O( n )
#
# The overhead in time is the level-order traversal, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the the storage for traversal_queue, which is of O( n ), and
# the storage for average_of_levels, which is of O( h )
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