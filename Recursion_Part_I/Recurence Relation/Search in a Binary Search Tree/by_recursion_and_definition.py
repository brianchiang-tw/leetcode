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
        
        if root is not None:
            
            if val > root.val:
                return self.searchBST( root.right, val )

            elif val < root.val:
                return self.searchBST( root.left, val )

            else:
                return root
            
        else:
            return None



# n : the number of nodes in binary search tree

## Time Complexity: O( n )
#
# The overhead in time is the cost of binary search, which is of O( h ) = O( n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for recursion call stack, which is of O( h ) = O( n )


def print_bst( node: TreeNode):

    if node:

        print_bst( node.left )
        print(f'{node.val} -> ', end = '')
        print_bst( node.right )



def test_bench():

    root = TreeNode(4)

    root.left = TreeNode(2)
    root.right = TreeNode(7)

    root.left.left = TreeNode(1)
    root.left.right= TreeNode(3)

    search_result = Solution().searchBST( root, 2 )

    # expected output:
    '''
    1 -> 2 -> 3 ->
    '''

    print_bst( search_result )



if __name__ == '__main__':

    test_bench()