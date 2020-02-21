'''

Description:

Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.

Example:

Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
Example 2:

Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.

'''



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    
    def sumNumbers(self, root: TreeNode) -> int:

        # storage for tree numbers, generated from root node to leave nodes
        tree_numbers = []
        
        def num_maker(node: TreeNode, tree_num: int):

            if node:
                
                # update tree_num with current node
                tree_num = 10 * tree_num + node.val

                if not node.left and not node.right:
                    # leaf node is reached, append tree_num to list
                    tree_numbers.append( tree_num )

                else:
                    # DFS down to next level
                    num_maker( node.left, tree_num)
                    num_maker( node.right, tree_num)        
        
        # -------------------------------------------        
        num_maker(root, 0)
        return sum(tree_numbers)



# n : the number of nodes in binary tree

## Time Complexity: O( n )
#
# The overhead in time is the cost of DFS traversal in binary tree, which is of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the storage for recursion call stack, as well as the list tree_numbers, which are of O( n ).



def test_bench():

    ## test case_#1
    root_1 = TreeNode(1)
    root_1.left = TreeNode(2)
    root_1.right = TreeNode(3)

    # expected output:
    '''
    25
    '''

    print( Solution().sumNumbers( root = root_1) )


    ## test case_#2
    root_2 = TreeNode( 4 )
    root_2.left = TreeNode( 9 )
    root_2.right = TreeNode( 0 )

    root_2.left.left = TreeNode(5)
    root_2.left.right = TreeNode(1)

    # expected output:
    '''
    1026
    '''
    print( Solution().sumNumbers( root = root_2 ) )


if __name__ == '__main__':

    test_bench()