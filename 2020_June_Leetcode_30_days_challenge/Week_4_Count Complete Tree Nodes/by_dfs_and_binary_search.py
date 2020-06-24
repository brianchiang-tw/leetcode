'''

Description:

Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3



Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99

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