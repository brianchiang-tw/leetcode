'''

Description:

Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
Note: Time complexity should be O(height of tree).

Example:

root = [5,3,6,2,4,null,7]
key = 3
'''

#    5
#   / \
#  3   6
# / \   \
#2   4   7

'''
Given key to delete is 3. So we find the node with value 3 and delete it.

One valid answer is [5,4,6,2,null,null,7], shown in the following BST.
'''
#    5
#   / \
#  4   6
# /     \
#2       7

'''
Another valid answer is [5,2,6,null,4,null,7].
'''
#    5
#   / \
#  2   6
#   \   \
#    4   7





# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        
        if not root:
            return None
            
        if root.val > key:
            root.left = self.deleteNode( root.left, key )

        elif root.val < key:
            root.right = self.deleteNode( root.right, key )

        else:

            if (not root.left) or (not root.right):
                # At least one child is empty
                # Target node is replaced by either non-empty child or None
                root = root.left if root.left else root.right

            else:
                # Both two childs exist
                # Target node is replaced by smallest element of right subtree
                cur = root.right

                while cur.left:
                    cur = cur.left

                root.val = cur.val
                root.right = self.deleteNode( root.right, cur.val )
                    
        return root



# h : the height of binary search tree

## Time Complexity: O( h )
#
# The overhead in time is the cost of target searching and node replacement, which is of O( h ).

## Space Complexity: O( h )
#
# The overhead in space is the storage for recursion call stack, which is of O( h ).


def in_order( node: TreeNode):

    if node:

        in_order( node.left )
        print( node.val, end = ' ')
        in_order( node.right )



def test_bench():

    root_1 = TreeNode( 5 )
    
    root_1.left = TreeNode( 3 )
    root_1.right = TreeNode( 6 )

    root_1.left.left = TreeNode( 2 )
    root_1.left.right = TreeNode( 4 )
    root_1.right.right = TreeNode( 7 )

    root_1_after_deletion =  Solution().deleteNode(root_1, 3)

    # expected output:
    '''
    2 4 5 6 7
    '''

    in_order( root_1_after_deletion )



if __name__ == '__main__':

    test_bench()    