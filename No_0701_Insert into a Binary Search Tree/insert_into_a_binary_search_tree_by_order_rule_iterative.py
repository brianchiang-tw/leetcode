'''

Description:

Given the root node of a binary search tree (BST) and a value to be inserted into the tree, insert the value into the BST. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Note that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

For example, 

Given the tree:
        4
       / \
      2   7
     / \
    1   3
And the value to insert: 5
You can return this binary search tree:

         4
       /   \
      2     7
     / \   /
    1   3 5
This tree is also valid:

         5
       /   \
      2     7
     / \   
    1   3
         \
          4

'''



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        
        if not root:
            root = TreeNode( val )
            return root
        
        cur = root
        while cur:
            
            if val > cur.val:
                
                if not cur.right:
                    cur.right = TreeNode( val )
                    break
                else:
                    cur = cur.right
            else:
                if not cur.left:
                    cur.left = TreeNode( val )
                    break
                else:
                    cur = cur.left
                
        return root



# n : number of nodes in binary tree

## Time Complexity: O( n )
#
# The overhead in time is the cost of insertion position finding, which is of O( n )

## Space Complexity: O( 1) 
#
# The overhead in space is the storage for looping variable, which is of O( 1 ).



def inorder_print( node:TreeNode):

    if node:

        inorder_print( node.left )
        print( f'{node.val} ', end = ' ')
        inorder_print( node.right )


def test_bench():

    root = TreeNode(4)
    
    root.left = TreeNode(2)
    root.right = TreeNode(7)

    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    

    # expected output:
    '''
    1  2  3  4  5  7
    1  2  3  4  5  6  7
    1  2  3  4  5  6  7  8
    1  2  3  4  5  6  7  8  9    
    '''


    test_data = [ 5, 6, 8, 9]
    worker = Solution()

    for new_node_value in test_data:
        worker.insertIntoBST( root, new_node_value )
        inorder_print( root )
        print()

    return



if __name__ == '__main__':

    test_bench()