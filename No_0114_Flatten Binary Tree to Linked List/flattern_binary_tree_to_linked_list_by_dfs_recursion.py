'''

Description:

Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6

'''



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    

            
        
    
    def flatten(self, root: TreeNode) -> None:
        """
        Input: root node of binary tree
        Output: convert binary tree to right-skewed linked list
        """
        
        if not root:
            # Base case:
            # empty node or empty tree
            return 
        
        if root.left: self.flatten(root.left)
        if root.right: self.flatten(root.right)
            
        original_right = root.right
        
        # flatten left sub-tree to right-skewed linked list
        root.right = root.left
        root.left = None
        
        # find the end node of right-skewed linked list
        while(root.right):
            root = root.right
        
        # flatten right sub-tree and append to end node
        root.right = original_right
        
        return
        
        
        
# n : the number of node in binary tree

## Time Compleity: O( n )
#
# The overhead in time is the cost of DFS traverdal, which is of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the dpeth of recursion call stack, which is of O( n ).


def print_right_skewed_linked_list( node:TreeNode ):

    if node:

        print( f'{node.val} ', end = '')

        print_right_skewed_linked_list( node.right )



def test_bench():

    root = TreeNode(1)

    root.left = TreeNode(2)
    root.right = TreeNode(5)

    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)

    root.right.right = TreeNode(6)

    Solution().flatten(root)

    # expected output:
    '''
    1 2 3 4 5 6 
    '''

    print_right_skewed_linked_list( root )

    return 



if __name__ == '__main__':

    test_bench()        