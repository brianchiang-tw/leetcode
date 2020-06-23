'''

Description:

Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input: 
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:

        def get_tree_height( node: TreeNode) -> int:
            
            if not node:
                # base case
                return 0
            
            else:
                # general case
                return 1 + get_tree_height( node.left )
            
        # -----------------------------------------------
        
        def counting( node: TreeNode ) -> int:
            
            h = get_tree_height( node )
            
            if h == 0:
                # base case (with empty tree)
                return 0
            
            else:
                # general case
                if (h - 1) == get_tree_height( node.right ):
                    
                    # left subtree and right subtree are of the same height
                    # last node is on the right subtree
                    return 2 ** (h - 1) + counting( node.right )
                
                else:
                    # left subtree is higher than right subtree
                    # last node is on the left subtree
                    return 2 ** (h - 2) + counting( node.left )
        
        # -----------------------------------------------
        return counting(root)



# n : the number of nodes in binary tree

## Time Complexity: O( (log n )^2 )
#
# The overhead in time is the cost of height of complete binary tree * cost of binary search on bottom level
# It takes O( h ) * O( log n) = O( log n ) * O( log n ) = O( (log n )^2 ) in total.

## Space Complexity: O( (log n )^2 )
#
# The overhead in space is the storage for recursion call stack, which are of O( (log n )^2 )


def test_bench():

    root = TreeNode(1)
    
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    root.right.left = TreeNode(6)

    # expected output:
    '''
    6
    '''

    print( Solution().countNodes(root = root) )

    return



if __name__ == '__main__':

    test_bench()