'''

Description:

Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.

'''



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        diameter = 0
        
        def discover_path(node):
            
            if not node:
                return 0
            
            else:
                
                # Discover whole tree in DFS
                left = discover_path( node.left ) 
                right = discover_path( node.right ) 
                
                local_longest = max( left, right )
                
                # update diameter with longest path on current level
                
                nonlocal diameter
                diameter = max( diameter, left + right)
                
                # return local longest path to parent node
                return local_longest+1
            
        # ---------------------------------------------------
        discover_path( root )
        return diameter
        


# n : the number of node in binary tree

## Time Complexity: O( n )
#
# The overhead in time is the cost of post-order DFS traversal, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for recursion call stack, which is of O( n )


def test_bench():

    root = TreeNode(1)

    root.left = TreeNode(2)
    root.right = TreeNode(3)

    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    # expected output:
    '''
    3
    '''

    print( Solution().diameterOfBinaryTree( root = root ) )

    return



if __name__ == '__main__':

    test_bench()