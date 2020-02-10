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
        
        def helper( node):
        
            if node:

                # DFS travesal to next level
                helper( node.right )
                helper( node.left )

                # flattern binary tree to right skewed linked list
                node.right = self.previous_traversal
                node.left = None
                self.previous_traversal = node
                
        # ---------------------
        
        # record of node of previous traversal
        self.previous_traversal = None
        helper(root)



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