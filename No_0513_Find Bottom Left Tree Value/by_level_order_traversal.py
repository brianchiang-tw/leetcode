'''

Description:

Given a binary tree, find the leftmost value in the last row of the tree.

Example 1:
Input:

    2
   / \
  1   3

Output:
1



Example 2:
Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7
Note: You may assume the tree (i.e., the given root node) is not NULL.


'''




# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        
        traversal_queue = [ root ]
        
        bottom_left = root
        
        while traversal_queue:
            
            next_level = []
            
            for idx, node in enumerate(traversal_queue):
                    
                if not idx:
                    # update bottom left as the first node on current level
                    bottom_left = node

                # add child node to next level traversal queue if they exist                    
                    
                if node.left:
                    next_level.append( node.left ) 

                if node.right:
                    next_level.append( node.right ) 

            traversal_queue = next_level
            
        return bottom_left.val



# n : number of nodes in binary tree

## Time Complexity: O( n )
#
# The overhead in time is the cost for level-order traversal, which is of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the storage for traversal queue, which is of O( n ).



def test_bench():

    head_1 = TreeNode( 2 )
    head_1.left = TreeNode( 1 )
    head_1.right = TreeNode( 3 )

    head_2 = TreeNode( 1 )
    head_2.left = TreeNode( 2 )
    head_2.right = TreeNode( 3 )

    head_2.left.left = TreeNode( 4 )
    head_2.right.left = TreeNode( 5 )
    head_2.right.right = TreeNode( 6 )

    head_2.right.left.left = TreeNode( 7 )

    test_data = [ head_1, head_2 ]

    # expected output

    '''
    1
    7
    '''


    for t in test_data:

        print( Solution().findBottomLeftValue( root = t ) )

    return



if __name__ == '__main__':

    test_bench()    
