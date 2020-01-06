'''

Description:

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import List
class Solution:
    def check_path_sum( self, node: TreeNode, sum, path: List[int], solution):
        
        if node is None:
            # empty tree
            return

        if node.val == sum and node.left is None and node.right is None:
            
            # get one solution meets summation requirement
            # add current node to path
            path += [ node.val ]
            
            # add current path to solution
            solution += [ path[:] ]
            
            return
        
        else:
            
            # update sum for next level
            sum -= node.val
            
            # add current node to path
            path += [ node.val ]
            
            # dfs with left child
            self.check_path_sum( node.left, sum, path[:], solution)
            
            # dfs with right child
            self.check_path_sum( node.right, sum, path[:], solution)
        
            return
        
        
    
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        
        solution = [] 
        
        self.check_path_sum( root, sum, [], solution )
        
        return solution
        


# n : the number of nodes in binary search tree

## Time Complexity: O( n )
#
# The overhead in time is the DFS traversal of whole binary tree, which is of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the storage for output list, which is of O( n ).



def test_bench():

    root = TreeNode( 5 )

    root.left = TreeNode( 4 )
    root.right = TreeNode( 8 )

    root.left.left = TreeNode( 11 )

    root.right.left = TreeNode( 13 )
    root.right.right = TreeNode( 4 )

    root.left.left.left = TreeNode( 7 )
    root.left.left.right = TreeNode( 2 )

    root.right.right.left = TreeNode( 5 )
    root.right.right.right = TreeNode( 1 )

    path_of_sum = Solution().pathSum( root, sum = 22 )

    # expected output:
    '''
    [[5, 4, 11, 2], [5, 8, 4, 5]]
    '''


    print( path_of_sum )

    return 



if __name__ == '__main__':

    test_bench()