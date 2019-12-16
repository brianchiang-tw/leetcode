'''

Description:

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

 

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution:
    
    def check_balance_factor(self, node: TreeNode ) -> (int, bool):
        
        if node is None:
            return 0, True
        
        else:
            
            left_h, left_flag = self.check_balance_factor(node.left)
            right_h, right_flag = self.check_balance_factor(node.right)
            
            if left_flag and right_flag and abs(left_h-right_h) < 2:
                return max(left_h,right_h) + 1, True
            else:
                # already un-balanced, early return
                return -1, False
        
    
    
    def isBalanced(self, root: TreeNode) -> bool:
        
        tree_height, balance_flag = self.check_balance_factor(root) 
        
        return balance_flag



# N : number of nodes in binary tree

## Time Complexity:
#
# The overhead in time is to check balance factor on each node
# The node number is of O( N )

## Space Complexity:
#
# The overhead in space is to maintain call stack for recursion
# The time of recursion if of O( N )



def test_bench():

    '''
    Example:

        3
       / \
      9  20
         /  \
        15   7

    '''

    # expected output
    '''
    True
    '''


    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)

    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)


    is_balanced = Solution().isBalanced( root )

    print( is_balanced )

    return


if __name__ == '__main__':

    test_bench()