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
        
        cur_node = root
        
        while cur_node:
            
            
            if cur_node.left:
                
                # locate the rightmost anchor node of left sub-tree
                rihgtmost_of_left_subtree = cur_node.left
                while rihgtmost_of_left_subtree.right:
                    rihgtmost_of_left_subtree = rihgtmost_of_left_subtree.right
                
                # flatten the right sub-tree to linked lsit and append to anchor node
                rihgtmost_of_left_subtree.right = cur_node.right
                
                # flatten the left sub-tree to right-skewed linked list
                cur_node.right = cur_node.left
                
                cur_node.left = None

            cur_node = cur_node.right



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