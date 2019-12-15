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
 

Note:
Bonus points if you could solve it both recursively and iteratively.

'''



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    def check_symm(self, p:TreeNode, q:TreeNode)->bool:
        
        if p and q:
            
            # both p and q exist, check symmetry on both child nodes
            return p.val == q.val and self.check_symm( p.left, q.right) and self.check_symm( p.right, q.left)
        
        elif not p and not q:
            # both p and q not exist, still of symmetry
            return True
        
        else:
            # one of either p or q not exist, against symmetry
            return False
            
        
    
    def isSymmetric(self, root: TreeNode) -> bool:
        
        if root is None:
            # empty tree
            return True
        else:
            # check symmetry by function check_symm
            return self.check_symm( root.left, root.right)
                

# N : number of elements in binary tree

## Time Complexity: O( N )
#
# The overhead in time is the recusion to check each level.
# Visit each single node takes O(1).
# There are n nodes in total, thus take O(N) for whole tree.

## Space Complexity: O( N )
#
# The overhead is space is to maintain call stack for recursion.
# Visit each single node takes O(1).
# There are n nodes in total, thus take O(N) for whole tree.



def test_bench():

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)

    is_symmetric = Solution().isSymmetric( root )
    
    # expected output:
    '''
    True
    '''
    print( is_symmetric )

    root.left.right = TreeNode(3)
    root.right.right = TreeNode(3)

    is_symmetric = Solution().isSymmetric( root )

    # expected output:
    '''
    False
    '''
    print( is_symmetric )

    return



if __name__ == '__main__':

    test_bench()
