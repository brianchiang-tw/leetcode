'''

Description:

Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]

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
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        
        bfs_queue = []
        traversal_path, cur_level_path = deque([]), []
        prev_level = 0
        bfs_queue.append( tuple((root, 0)) )
        
        while len(bfs_queue) != 0:
            
            visit_node, node_level = bfs_queue.pop(0)
            
            if visit_node is None:
                # current node is empty, skip and continue next iteration
                continue
                
            if node_level > prev_level:
                # insert previous level path to traversal path on head
                traversal_path.appendleft( cur_level_path[:] )
                cur_level_path.clear()
                prev_level = node_level
                
            cur_level_path.append( visit_node.val )
            
            bfs_queue.append( tuple((visit_node.left, node_level+1)) )
            bfs_queue.append( tuple((visit_node.right, node_level+1)) )
            
        if root is not None:
            # insert last level path to traversal path on head
            traversal_path.appendleft( cur_level_path[:] )
            
        return traversal_path
            
                

# N : number of nodes in binary tree

## Time Complexity: O( N )
#
# The overhead in time is the while loop with bfs_queue.
# The number of iteration is with the number of nodes on order O( N )

## Space Complexity: O( N )
#
# The overhead in time is the bfs_queue as well as traversal_path
# The size of them grow with the number of nodes on order O( N )




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
    [[15, 7], [9, 20], [3]]
    '''

    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode( 7 )

    level_order_traversal = list( Solution().levelOrderBottom( root ) )

    print( level_order_traversal )

    return



if __name__ == '__main__':

    test_bench()