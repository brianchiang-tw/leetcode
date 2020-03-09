'''

Description:

958. Check Completeness of a Binary Tree
Medium

557

10

Add to List

Share
Given a binary tree, determine if it is a complete binary tree.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

 

Example 1:

Input: [1,2,3,4,5,6]
Output: true
Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.



Example 2:

Input: [1,2,3,4,5,null,7]
Output: false
Explanation: The node with value 7 isn't as far left as possible.
 
Note:

The tree will have between 1 and 100 nodes.

'''



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        
        
        traversal_queue = deque( [ root ] )
        prev_node = root
        
        
        # Launch Level-order traversal
        
        while traversal_queue:
            
            cur_node = traversal_queue.popleft()
            
            if cur_node:
                
                if not prev_node:
                    # Empty node in the middle means this is not a complete binary tree ( not left-compact)
                    return False
                
                traversal_queue.append( cur_node.left )
                traversal_queue.append( cur_node.right )
            
            # update previous node
            prev_node = cur_node
            
        return True



# n : the number of nodes in binary tree

## Time Complexity: O( n )
#
# The overhead in time is the cost of level-order traversal, which is of ( n ).

## Space Complexity: O( n )
#
# The overhead in space is the storage of traversal_queue, which is of O( n ).


def test_bench():

    ## Test_case_#1

    root_1 = TreeNode(1)
    
    root_1.left = TreeNode(2)
    root_1.right = TreeNode(3)

    root_1.left.left = TreeNode(4)
    root_1.left.right = TreeNode(5)
    root_1.right.left = TreeNode(6)

    ## Test_case_#2
    root_2 = TreeNode(1)
    
    root_2.left = TreeNode(2)
    root_2.right = TreeNode(3)

    root_2.left.left = TreeNode(4)
    root_2.left.right = TreeNode(5)
    root_2.right.right = TreeNode(7)

    test_data = [
                    root_1,
                    root_2,
                ]

    # expected output:
    '''
    True
    False
    '''

    for t in test_data:
        print( Solution().isCompleteTree( root = t ) )

    return



if __name__ == '__main__':

    test_bench()
