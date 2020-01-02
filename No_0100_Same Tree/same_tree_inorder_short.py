'''

Description:

Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


        
class Solution:
    def isSameTree(self, p, q):
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        else:
            return p is q



# N : number of nodes in tree

## Time Compleixty : O( N )
#
# Visit each node and check equality with DFS, each node is visited once.
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
    root_1 = TreeNode(5)

    root_1.left = TreeNode(5)
    root_1.right = TreeNode(5)

    root_2 = TreeNode(5)

    root_2.left = TreeNode(5)
    root_2.right = TreeNode(5)


    print( Solution().isSameTree( root_1, root_2 ) )


    # test case_#2:
    root_1 = TreeNode(5)

    root_1.left = TreeNode(5)
    root_1.right = TreeNode(5)

    root_2 = TreeNode(5)

    root_2.left = TreeNode(4)
    root_2.right = TreeNode(6)

    print( Solution().isSameTree( root_1, root_2 ) )



    # test case_#3:
    # with root node only
    root_1 = TreeNode(5)
    root_2 = TreeNode(5)
    print( Solution().isSameTree( root_1, root_2 ) )



    # test case_#4:
    # empty tree
    root_1 = None
    root_2 = None
    print( Solution().isSameTree( root_1, root_2 ) )



if __name__ == '__main__':

    test_bench()        