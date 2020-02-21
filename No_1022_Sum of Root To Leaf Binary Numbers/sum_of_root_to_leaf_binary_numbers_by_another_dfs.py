class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution:
    def sumRootToLeaf(self, root, tree_num=0):
        
        if not root: 
			# empty node or empty tree
            return 0
        
        else:
            
			# update tree_num in binary form
            tree_num = tree_num << 1 | root.val
        
            if root.left == root.right: 
				# leaf node
                return tree_num
            else:
				# non-left node
				# DFS down to next level
                return self.sumRootToLeaf(root.left, tree_num) + self.sumRootToLeaf(root.right, tree_num)



# n : the number of node in binary tree

## Time Complexity: O( n )
#
# The overhead in time is the cost of DFS traversal, which is of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the storage for recursion call stack, which is of O( n ).




def test_bench():

    '''
    Example 1:

             1
          /    \
         0      1
        / \    / \
       0   1  0   1
    Input: [1,0,1,0,1,0,1]
    Output: 22
    Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22

    '''

    root = TreeNode( 1 )
    root.left = TreeNode( 0 )
    root.right = TreeNode( 1 )

    root.left.left = TreeNode( 0 )
    root.left.right = TreeNode( 1 )

    root.right.left = TreeNode( 0 )
    root.right.right = TreeNode( 1 )

    # expected output:
    '''
    22
    '''
    print( Solution().sumRootToLeaf( root ) )



if __name__ == '__main__':

    test_bench()