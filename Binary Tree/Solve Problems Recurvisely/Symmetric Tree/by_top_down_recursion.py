'''

Description:

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
 

'''



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    
    def chk_symm(self, p: TreeNode, q:TreeNode) ->bool:
            
            
                       
            if p and q:
                return (p.val == q.val) and self.chk_symm( p.left, q.right) and self.chk_symm( p.right, q.left)
                    
            elif not p and not q:
                # Base case:
                # Both p and q are empty node
                return True
            
            else:
                # Base case:
                # One is empty, the other is non-empty.
                return False
                
    
    def isSymmetric(self, root: TreeNode) -> bool:
        
        if root:
            return self.chk_symm( p = root.left, q = root.right)
        
        else:
            return True



# n : the number of nodes in binary tree

## Time Complexity: O( n )
#
# The overhead in time is the cost of DFS traversal, which is of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the storage for recursion call stack, which is of O( n ).

def test_bench():

    root = TreeNode( 1 )

    root.left = TreeNode( 2 )
    root.right = TreeNode( 2 )

    root.left.left = TreeNode( 3 )
    root.left.right = TreeNode( 4 )
    root.right.left = TreeNode( 4 )
    root.right.right = TreeNode( 3 )            

    # expected output:
    '''
    True
    '''
    print( Solution().isSymmetric( root ) )

    # ---------------------------------------------

    root = TreeNode( 1 )
    
    root.left = TreeNode( 2 )
    root.right = TreeNode( 2 )

    root.left.right = TreeNode( 3 )
    root.right.right= TreeNode( 3 )

    # expected output:
    '''
    False
    '''
    print( Solution().isSymmetric( root ) )

    # ---------------------------------------------

if __name__ == '__main__':

    test_bench()    