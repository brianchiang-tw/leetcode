'''

Description:

Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1



Trivia:
This problem was inspired by this original tweet by Max Howell:

Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.

'''



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque    
    
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:        
        
        traversal_queue = deque([root]) if root else None
        
		# lanuch BFS, aka level-order-traversal to carry out invertion
        while traversal_queue:
            
            cur_node = traversal_queue.popleft()
            
			# Invert child node of current node
            cur_node.left, cur_node.right = cur_node.right, cur_node.left
            
			# push left child into queue to invert left subtree
            if cur_node.left:
                traversal_queue.append( cur_node.left )
            
			# push right child into queue to invert right subtree
            if cur_node.right:
                traversal_queue.append( cur_node.right )                
        
        return root


# n : the number of nodes in binary tree

## Time Complexity: O( n )
#
# The overhead in time is the cost of BFS, which is of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the storage for traversal queue, which is of O( n ).


from collections import deque

def print_level_order( node ):

    traversal_queue = [node] if node else None

    while traversal_queue:

        next_level = []

        for cur_node in traversal_queue:

            print(f'{cur_node.val}', end = ' ')

            if cur_node.left:
                next_level.append( cur_node.left )

            if cur_node.right:
                next_level.append( cur_node.right )
        
        print('')

        traversal_queue = next_level
    return


def test_bench():

    root = TreeNode( 4 )

    root.left = TreeNode( 2 )
    root.right = TreeNode( 7 )

    root.left.left = TreeNode( 1 )
    root.left.right = TreeNode( 3 )
    root.right.left = TreeNode( 6 )
    root.right.right = TreeNode( 9 )

    print('before \n')
    # expected output:
    '''
    4
    2 7
    1 3 6 9
    '''
    print_level_order( root )

    root = Solution().invertTree( root )

    print('\nafter \n')

    # expected output:
    '''
    4
    7 2
    9 6 3 1    
    '''
    print_level_order( root )

    return




if __name__ == '__main__':

    test_bench()