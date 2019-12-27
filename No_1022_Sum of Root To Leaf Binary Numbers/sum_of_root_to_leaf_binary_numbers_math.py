'''

Description:

Given a binary tree, each node has value 0 or 1.  Each root-to-leaf path represents a binary number starting with the most significant bit.  For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.

For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.

Return the sum of these numbers.

Example 1:

          1
       /    \
      0      1
     / \    / \
    0   1  0   1
Input: [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
 

Note:

The number of nodes in the tree is between 1 and 1000.
node.val is 0 or 1.
The answer will not exceed 2^31 - 1.

'''



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    
    def sumRootToLeaf(self, root, path_sum = 0):

        if root is None:
            # empty tree or empty node
            return 0

        # each node represents a binary bit
        path_sum = ( path_sum << 1 ) | root.val

        if root.left is None and root.right is None:
            # reach one root-to-leaf path, return path_sum
            return path_sum

        else:
            # divide and conquer
            return self.sumRootToLeaf(root.left, path_sum) + self.sumRootToLeaf(root.right, path_sum)


# n : the number of nodes in given input binary tree

## Time Complexity: O( n )
#
# The overhead in time is to traverse each node in DFS, which is of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is to maintain stack for traverse dfs all node in binary tree of O( n ).


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