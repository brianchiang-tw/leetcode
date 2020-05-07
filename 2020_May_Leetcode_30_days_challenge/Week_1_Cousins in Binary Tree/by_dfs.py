'''

Description:

In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.


Example 1:


Input: root = [1,2,3,4], x = 4, y = 3
Output: false



Example 2:

Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true



Example 3:

Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false
 

Note:

The number of nodes in the tree will be between 2 and 100.
Each node has a unique integer value from 1 to 100.

'''



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:

        def dfs( root: TreeNode, value: int, depth: int, parent: int ):

            if not root:
                return

            if root.val == value:
                
                # find the node with target value
                global depth_res, parent_res

                depth_res = depth
                parent_res = parent

                return

            else:
                
                # search the node with target value in left sub-tree
                dfs( root.left, value, depth+1, root.val )

                # search the node with target value in right sub-tree
                dfs( root.right, value, depth+1, root.val )

        # ---------------------------------------------------------------

        dfs( root = root, value = x, depth = 0, parent = 0 )
        x_depth, x_parent = depth_res, parent_res

        dfs( root = root, value = y, depth = 0, parent = 0 )
        y_depth, y_parent = depth_res, parent_res

        return x_parent != y_parent and x_depth == y_depth



# n : the number of nodes in binary search tree

## Time Complexity: O( n )
#
# The overhead in time is the cost of pre-order DFS traversal, which is of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the storage for recursion stack, which is of O( n ).


def test_bench():

    root_1 = TreeNode( 1 )
    root_1.left = TreeNode( 2 )
    root_1.right = TreeNode( 3 )
    root_1.left.left = TreeNode( 4 )

    x1, y1 = 4, 3

    # ------------------------------------------

    root_2 = TreeNode( 1 )
    root_2.left = TreeNode( 2 )
    root_2.right = TreeNode( 3 )
    root_2.left.right = TreeNode( 4 )
    root_2.right.right = TreeNode( 5 )

    x2, y2 = 5, 4

    # ------------------------------------------

    root_3 = TreeNode( 1 )
    root_3.left = TreeNode( 2 )
    root_3.right = TreeNode( 3 )
    root_3.left.right = TreeNode( 4 )

    x3, y3 = 2, 3

    # ------------------------------------------

    test_data = [
                    ( root_1, x1, y1 ),
                    ( root_2, x2, y2 ),
                    ( root_3, x3, y3 ),
                ]

    # expected output:
    '''
    False
    True
    False
    '''

    for t in test_data:

        print( Solution().isCousins( *t) )
    
    return



if __name__ == '__main__':

    test_bench()