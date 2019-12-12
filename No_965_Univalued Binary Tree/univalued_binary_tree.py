'''

Description:

A binary tree is univalued if every node in the tree has the same value.

Return true if and only if the given tree is univalued.

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution:
    
    def is_the_same(self, root, val):
        
        if not root:
            return True
        
        else:       
            # check whether root, left-subtree, right-subtree have the same value or not.
            return all( [root.val == val, self.is_the_same(root.left, val), self.is_the_same(root.right, val) ] )
                       
        
        
    def isUnivalTree(self, root: TreeNode) -> bool:
        
        if not root:
            return True
        else:
            # all other nodes compare with the value of root
            return self.is_the_same(root, root.val)
            

# N : number of nodes in tree

## Time Compleixty : O( N )
#
# Visit each node with DFS, each node is visited once.
# It takes O( N ) for a tree traversal

## Space Compleixty : O( N )
#
# The overhead in space is to maintain stack for recursive function call, up to O( N ) times.

            
def test_bench():


    # expected output:
    '''
    True
    False
    True
    True
    '''


    # test case_#1:
    root = TreeNode(5)

    root.left = TreeNode(5)
    root.right = TreeNode(5)

    print( Solution().isUnivalTree( root ) )


    # test case_#2:
    root = TreeNode(5)

    root.left = TreeNode(4)
    root.right = TreeNode(6)

    print( Solution().isUnivalTree( root ) )



    # test case_#3:
    # with root node only
    root = TreeNode(5)
    print( Solution().isUnivalTree( root ) )



    # test case_#4:
    # empty tree
    root = None
    print( Solution().isUnivalTree( root ) )



if __name__ == '__main__':

    test_bench()