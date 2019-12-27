'''

Description:

Given the root node of a binary search tree (BST) and a value. You need to find the node in the BST that the node's value equals the given value. Return the subtree rooted with that node. If such node doesn't exist, you should return NULL.

For example, 

Given the tree:
        4
       / \
      2   7
     / \
    1   3

And the value to search: 2
You should return this subtree:

      2     
     / \   
    1   3
In the example above, if we want to search the value 5, since there is no node with value 5, we should return NULL.

Note that an empty tree is represented by NULL, therefore you would see the expected output (serialized tree format) as [], not null.

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        
        cur = root
        
        while cur is not None:
            
            if cur.val == val:
                return cur
            
            elif cur.val > val:
                cur = cur.left
                
            else:
                cur = cur.right
        
        return None



# n : the number of nodes in binary tree

## Time Complexity: O(h), worst case down to O( n )
#
# Average case is of order tree height = O( h ) = O ( log n )
# Worst case is of order tree length = O( n ) when tree is degraded to a linked list


## Space Complexity: O(1)
#
# The overhead in space is to maintain looping variable cur, which is of fixed size O( 1 )



def test_bench():

    root = TreeNode(4)

    root.left = TreeNode(2)
    root.right = TreeNode(7)

    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)

    target = 2

    # expected output:
    '''
    2
    '''
    print( Solution().searchBST(root, val = target ).val )

    return



if __name__ == '__main__':

    test_bench()