'''

Description:


Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]


 

Example 1:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
 

Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the BST.

'''



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        cur_value = root.val
        
        if p.val > cur_value and q.val > cur_value:
            return self.lowestCommonAncestor( root.right, p, q)
        
        elif p.val < cur_value and q.val < cur_value:
            return self.lowestCommonAncestor( root.left, p, q)
        
        else:
            return root



# n : the number of nodes in binary search tree

## Time Complexity: O( n )
#
# The overhead in time is the depth of seatch, which is of O( n ) when BST degraded to linked list.

## Space Complexity: O( n )
#
# The overhead in space is the storage for recusrion call stack, which is of O( n ).


def test_bench():

    ## Test case_#1

    # expected output:
    '''
    6
    '''

    node_0 = TreeNode( 0 ) 
    node_2 = TreeNode( 2 )
    node_3 = TreeNode( 3 )
    node_4 = TreeNode( 4 )
    node_5 = TreeNode( 5 )
    node_6 = TreeNode( 6 )
    node_7 = TreeNode( 7 )
    node_8 = TreeNode( 8 )
    node_9 = TreeNode( 9 )

    root_1 = node_6

    node_4.left = node_3
    node_4.right = node_5

    node_2.left = node_0
    node_2.right = node_4

    node_8.left = node_7
    node_8.right = node_9

    node_6.left = node_2
    node_6.right = node_8

    print( Solution().lowestCommonAncestor( root = root_1, p = node_2, q = node_8 ).val )

    return



if __name__ == '__main__':

    test_bench()