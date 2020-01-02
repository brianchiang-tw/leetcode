'''

Description:

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: 

“The lowest common ancestor is defined between two nodes p and q as the lowest node in T 

that has both p and q as descendants (where we allow a node to be a descendant of itself).”

'''



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if root and ( root is p or root is q ):
            return root
        
        if root is None:
            return None
            
        else:
            left_ancestor = self.lowestCommonAncestor( root.left, p ,q)
            
            right_ancestor = self.lowestCommonAncestor( root.right, p ,q)
            
            
            if left_ancestor and right_ancestor:
                return root
            
            elif left_ancestor:
                return left_ancestor
            
            elif right_ancestor:
                return right_ancestor
            
            else:
                return None

# N : number of nodes in binary tree

## Time Complexity : O( N )
#
# The overhead in time is how long can we reach the end case of meeting p and q.
# The average and worst vase is of O(N) becuase p and q could be on the opposite subtree, 
# which means one in on the left subtree, the other is on the right subtree.

## Space Complexity : O( N )
#
# The overhead in space is to maintain call stack for recursion.
# The worst case is either the left-skew or right-skew tree, which takes O( N ) to reach stop condition.





def test_bench():

    root = TreeNode(5)

    root.left = TreeNode(3)

    node_2 = TreeNode(2)
    node_4 = TreeNode(4)

    root.left.left = node_2
    root.left.right = node_4


    root.right = TreeNode(7)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(8)

    # expected output:
    '''
    3
    '''

    print( Solution().lowestCommonAncestor(root, p = node_2, q = node_4).val )



if __name__ == '__main__':

    test_bench()