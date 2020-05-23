'''

Description:

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

'''



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
    
        if root is None:
            # Base case:
            # Empty Node
            return False
        
        else:
            
            if root.val == sum and root.left is None and root.right is None:
                # Base case:
                # Reach leaf node with target sum
                return True
            
            else:
                # General case:
                # Search a path with target sum in DFS
                return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)



# n : the number of node in binary tree

## Time Complexity: O( n )
#
# The overhead in time is the cost of DFS traversal, which is of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the cost of recursion call stack, which is of O( n ).


def test_bench():

    root = TreeNode( 5 )

    root.left = TreeNode( 4 )
    root.right = TreeNode( 8 )

    root.left.left = TreeNode( 11 )
    root.right.left = TreeNode( 13 )
    root.right.right = TreeNode( 4 )

    root.left.left.left = TreeNode( 7 )
    root.left.left.right = TreeNode( 2 )
    root.right.right.right = TreeNode( 1 )

    # expected output:
    '''
    True
    '''
    print( Solution().hasPathSum( root = root, sum = 22) )

    # expected output:
    '''
    False
    '''
    print( Solution().hasPathSum( root = root, sum = 21) )



if __name__ == '__main__':

    test_bench()
