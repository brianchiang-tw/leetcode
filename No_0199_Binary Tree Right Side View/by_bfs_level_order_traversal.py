'''

Description:

Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

'''



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List
from collections import deque

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        
        if not root:
            # Quick response for empty tree
            return []
        
        traversal_queue = deque( [root ] )
        
        right_side_view = []
        
        while traversal_queue:
            
            for _ in range( len(traversal_queue) ):
                
                cur_node = traversal_queue.popleft()
                
                if cur_node.left:
                    traversal_queue.append( cur_node.left )
                    
                if cur_node.right:
                    traversal_queue.append( cur_node.right )
                    
            right_side_view.append( cur_node.val )
        
        return right_side_view



# n : the number of nodes in binary tree

## Time Complexity: O( n )
#
# The overhead in time is the cost of level-order traversal, which is of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the stroage for travrersal queue, which is of O( n ).


def test_bench():

    root = TreeNode( 1 )

    root.left = TreeNode( 2 )
    root.right = TreeNode( 3 )

    root.left.right = TreeNode( 5 )
    root.right.right = TreeNode( 4 )

    # expected output:
    '''
    [1, 3, 4]
    '''

    print( Solution().rightSideView( root ) )



if __name__ == '__main__':

    test_bench()