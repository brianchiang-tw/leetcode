'''

Description:

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

'''



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
       
    def maxDepth(self, root: TreeNode) -> int:

        cur_queue = [ root ] if root else []
        cur_depth = 0

        while cur_queue:
            
            # update current depth
            cur_depth += 1

            next_queue = []

            # launch level-order traversal, add update next_qeueue from child nodes
            for node in cur_queue:
                
                if not node.left and not node.right:
                    return cur_depth


                if node.left:
                    next_queue.append( node.left )

                if node.right:
                    next_queue.append( node.right )

            cur_queue = next_queue
            

        # -------------------------------

        return cur_depth




# n : the number of nodes in binary trees

## Time Complexity: O( n )
#
# The overhead in time is the cost of BFS (i.e., level-order traversal), which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for traversal queue, which is of O( n )



def test_bench():

    root = TreeNode( 3 )

    root.left = TreeNode( 9 )
    root.right = TreeNode( 20 )

    root.right.left = TreeNode( 15 )
    root.right.right = TreeNode( 7 )

    # expected output:
    '''
    2
    '''
    print( Solution().maxDepth( root ) )

    # ----------------------------------------

    root = TreeNode( 2 )
    
    root.left = TreeNode( 1 )
    root.right = TreeNode( 3 )

    # expected output:
    '''
    2
    '''
    print( Solution().maxDepth( root ) )

    # ----------------------------------------

    root = TreeNode( 2 )

    # expected output:
    '''
    1
    '''
    print( Solution().maxDepth( root ) )

    # ----------------------------------------

    root = None

    # expected output ( test for empty tree ):
    '''
    0
    '''
    print( Solution().maxDepth( root ) )


if __name__ == '__main__':

    test_bench()