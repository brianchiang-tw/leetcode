'''

Description:

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]

'''



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        
        traversal_queue = [ root ] if root else []
        
        path = []
        
        while traversal_queue:
            
            cur_level_path, next_level_queue = [], []
            
            for node in traversal_queue:
                
                # update current level traversal path
                cur_level_path.append( node.val )
                
                if node.left:
                    next_level_queue.append( node.left )
                
                if node.right:
                    next_level_queue.append( node.right )
            
            # add current level path into path collection
            path.append( cur_level_path )
            
            # update next_level_queue as traversal_queu
            traversal_queue = next_level_queue
            
        return path



# n : number of nodes in binary tree

## Time Complexity: O( n )
#
# The overhead in time is the cost of BFS, which is if O( n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for traversal_queue and path, which are of O( n )




def test_bench():

    '''

        3
       / \
      9  20
        /  \
       15   7

    '''

    # expected output:
    '''
    [[3], [9, 20], [15, 7]]
    '''

    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode( 7 )

    level_order_traversal = Solution().levelOrder( root )

    print( level_order_traversal )

    return



if __name__ == '__main__':

    test_bench()        