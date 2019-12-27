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
    
    def path_tracker(self, node, path, bag_of_path ):
    
        if node is None:
            return None
        
        else:
            cur_path = path + str(node.val) 
            left = self.path_tracker( node.left, cur_path[::], bag_of_path )
            right = self.path_tracker( node.right, cur_path[::], bag_of_path )
            
            if left is None and right is None:
                bag_of_path.append( cur_path )
            
            return bag_of_path
    
    
    def sumRootToLeaf(self, root: TreeNode) -> int:
        
        bag_of_path = self.path_tracker( root, str(), [] )
        
        if bag_of_path is None:
            return 0
        
        else:
            
            path_sum = sum( [ int(p, 2)for p in bag_of_path ] )
            return path_sum



# n : the number of nodes in given input binary tree

## Time Complexity: O( n )
#
# The overhead in time is to traverse each node in DFS, which is of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is to maintain path and bag-of-path to track root-to-leaf path.
# In addition, the the number of root-to-leaf paths is of O( n )


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