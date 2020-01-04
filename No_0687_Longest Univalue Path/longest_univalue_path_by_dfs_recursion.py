'''

Description:

Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

The length of path between two nodes is represented by the number of edges between them.

 

Example 1:

Input:

              5
             / \
            4   5
           / \   \
          1   1   5
Output: 2

 

Example 2:

Input:

              1
             / \
            4   5
           / \   \
          4   4   5
Output: 2

 

Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.

''' 



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    def longestUnivaluePath(self, root: TreeNode) -> int:
        
        
        # keep track of longest univalue path
        self.longest_uni_path = 0
        
        
        def helper( node: TreeNode):
            if not node:
                return 0

            else:

                path_of_left = helper( node.left )
                path_of_right = helper( node.right )
                
                # if left child has the same value of current node, extend uni path
                left_uni = path_of_left+1 if node.left and node.left.val == node.val else 0
                
                # if right child has the same value of current node, extend uni path
                right_uni = path_of_right+1 if node.right and node.right.val == node.val else 0
                
                # use current node as bridge to make uni_path as long as possible
                self.longest_uni_path = max( self.longest_uni_path, left_uni + right_uni )

                return max(left_uni, right_uni)        
        


        # DFS traverse whole tree from root
        helper( root )
        
        return self.longest_uni_path
                


# n : the number of node in the binary tree

## Time Complexity: O( n )
# 
# The major overhead in time is the dfs traverse call of whole binary tree, which is of O( n ).

## Space Complexity: O( n )
#
# The major overhead in space is to maintain call stack for recursion call, which is of O( n ).



def test_bench():

    '''
    Input:

              5
             / \
            4   5
           / \   \
          1   1   5
    
    '''

    # expected output:
    '''
    2

    Hint: 5 - 5 - 5
    '''

    root = TreeNode( 5 )

    root.left = TreeNode( 4 )
    root.left.left = TreeNode( 1 )
    root.left.right = TreeNode( 1 )

    root.right = TreeNode( 5 )
    root.right.right = TreeNode( 5 )

    print( Solution().longestUnivaluePath(root) )

    return



if __name__ == '__main__':

    test_bench()