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

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        traversal_path = []
        cur_level_path, prev_level = [], 0
        bfs_queue = [(root, 0)]
        
        while len(bfs_queue) != 0:
            
            visit_node, node_level = bfs_queue.pop(0)
            
            if visit_node is None:
                # empty node, just skip and continue next iteration
                continue
            
            
            if node_level > prev_level:
                # down to a new level
                # append cur_level_path to traversal_path
                traversal_path.append( cur_level_path[:] )
                cur_level_path.clear()
                
                # update prev_level
                prev_level = node_level
            
            
            cur_level_path.append( visit_node.val )
            bfs_queue.append( (visit_node.left, node_level+1) )
            bfs_queue.append( (visit_node.right, node_level+1) )
        
        if root is not None:
            # append final level, is root is non-empty
            traversal_path.append( cur_level_path[:] )    
        
        return traversal_path


# N : number of nodes in binary tree

## Time Complexity: O( N )
#
# The overhead in time is the while loop with bfs_queue.
# The number of iteration is with the number of nodes on order O( N )

## Space Complexity: O( N )
#
# The overhead in space is the bfs_queue as well as traversal_path
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