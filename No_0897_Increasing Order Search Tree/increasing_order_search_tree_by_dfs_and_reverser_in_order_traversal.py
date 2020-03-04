'''

Description:

Given a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only 1 right child.

Example 1:
Input: [5,3,6,2,4,null,8,1,null,null,null,7,9]

       5
      / \
    3    6
   / \    \
  2   4    8
 /        / \ 
1        7   9

Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

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
            \
             7
              \
               8
                \
                 9  
Note:

The number of nodes in the given tree will be between 1 and 100.
Each node will have a unique integer value from 0 to 1000.

'''



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        prev_node = None
        
        def helper( node: TreeNode):
                           
            if node.right:
                helper( node.right )

            # prev_novde always points to next larger element for current node
            nonlocal prev_node

            # update right link points to next larger element
            node.right = prev_node

            # break the left link of next lrager element
            if prev_node:
                prev_node.left = None

            # update previous node as current node
            prev_node = node

            if node.left:
                helper( node.left)
                
        # ---------------------------------------
        helper( root )
        
        return prev_node



# n : the number of nodes in binary tree

## Time Complexity: O( n )
#
# The overhead in time is the cost of DFS traversal, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the cost of recursion call stack, which is of O( n ).



def print_right_skew_tree( node ):

    if node:

        print(f'{node.val} ', end = '')

        print_right_skew_tree( node.right )

def test_bench():

    root = TreeNode(5)

    root.left = TreeNode(3)
    root.right = TreeNode(6)

    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(8)

    root.left.left.left = TreeNode(1)
    root.right.right.left = TreeNode(7)
    root.right.right.right = TreeNode(9)

    root = Solution().increasingBST( root )

    print_right_skew_tree( root )

    return



if __name__ == '__main__':

    test_bench()
