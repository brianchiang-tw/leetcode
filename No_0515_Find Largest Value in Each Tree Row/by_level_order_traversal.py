
'''

Description:

You need to find the largest value in each row of a binary tree.

Example:
Input: 

          1
         / \
        3   2
       / \   \  
      5   3   9 

Output: [1, 3, 9]

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
    def largestValues(self, root: TreeNode) -> List[int]:
        
        
        if not root:
            return []
        
        traversal_queue =  deque([root])
        
        max_list = []
        
        # Launch level-order traversal
        while traversal_queue:
        
            next_queue = deque([])
            max_val = float('-inf')
            
            for cur in traversal_queue:
                
                # update max node value of current level
                max_val = max( max_val, cur.val )
            
                if cur.left:
                    next_queue.append( cur.left )
                    
                if cur.right:
                    next_queue.append( cur.right )
            
            max_list.append( max_val )
            
            traversal_queue = next_queue
        
        return max_list



# n : the numberof nodes

## Time Complexity : O( n )
#
# The overhead in time is the cost of level-order traversal, which is of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the storage for traversal queue, which is of O( n ).



def test_bench():

    root_1 = TreeNode( 1 )
    
    root_1.left = TreeNode( 3 )
    root_1.right = TreeNode( 2 )

    root_1.left.left = TreeNode( 5 )
    root_1.left.right = TreeNode( 3 )
    root_1.right.right = TreeNode( 9 )

    # expected output:
    '''
    [1, 3, 9]
    '''

    print( Solution().largestValues( root = root_1 ) )



if __name__ == '__main__':

    test_bench()