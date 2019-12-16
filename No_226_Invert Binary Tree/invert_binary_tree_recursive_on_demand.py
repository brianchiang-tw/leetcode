'''

Description:

Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1

Trivia:
This problem was inspired by this original tweet by Max Howell:

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        if root is None:
            # empty node
            return root
        
        else:
            # non empty node
            
            # swap left child, right child
            root.left, root.right = root.right, root.left
            
            if root.left:
                # invert left subtree on demand
                self.invertTree( root.left )
            
            if root.right:
                # invert right subtree on demand
                self.invertTree( root.right )
            
            return root


# N : number of nodes in binary treee

## Time Complexity : O( N )
#
# The overhead in time is to iterate each non-leaf node with invert function
# The number of of non-leaf node is of O( N )

## Space Complexity : O( N )
#
# The overhead in space is to maintain call stack for recrusion.
# The numbeer of recursion is up to number of non-leaf node with order O( N )




def _print_tree( node:TreeNode):

    if( node ):

        _print_tree( node.left )
        print( node.val, end = ' ')
        _print_tree( node.right )

    return



def test_bench():

    '''
    Example:

    Input:

         4
       /   \
      2     7
     / \   / \
    1   3 6   9
    '''



    # expected output:
    '''
     before tree invertion:
    9 7 6 4 3 2 1
     after tree invertion:
    1 2 3 4 6 7 9
    '''


    root = TreeNode( 4 )
    
    root.left = TreeNode( 7 )
    root.left.left = TreeNode( 9 )
    root.left.right = TreeNode( 6 )

    root.right = TreeNode( 2 )
    root.right.left = TreeNode( 3 )
    root.right.right = TreeNode( 1 )

    print("\n before tree invertion: ")
    _print_tree( root )

    Solution().invertTree( root )

    print("\n after tree invertion: ")
    _print_tree( root )


    return


if __name__ == '__main__':

    test_bench()