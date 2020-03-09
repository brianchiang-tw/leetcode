'''

Description:

Given a binary tree root, the task is to return the maximum sum of all keys of any sub-tree which is also a Binary Search Tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 


Example 1:

Input: root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]
Output: 20
Explanation: Maximum sum in a valid Binary search tree is obtained in root node with key equal to 3.



Example 2:

Input: root = [4,3,null,1,2]
Output: 2
Explanation: Maximum sum in a valid Binary search tree is obtained in a single root node with key equal to 2.



Example 3:

Input: root = [-4,-2,-5]
Output: 0
Explanation: All values are negatives. Return an empty BST.



Example 4:

Input: root = [2,1,3]
Output: 6



Example 5:

Input: root = [5,4,8,3,null,6,3]
Output: 7
 

Constraints:

Each tree has at most 40000 nodes..
Each node's value is between [-4 * 10^4 , 4 * 10^4].

 '''



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxSumBST(self, root: TreeNode) -> int:
        
        maximum_sum = 0
        
        def sumBST( node: TreeNode ):
            
            if not node:
                return True, 0
            
            else:
                
                is_left_bst, l_sum = sumBST( node.left )
                is_right_bst, r_sum = sumBST( node.right )
 
                nonlocal maximum_sum
                cur_sum = l_sum + node.val + r_sum
        
                # If current subtree is BST, then compare and update maximum_sum
                # Otherwise, return 0 to parent level
            
                if (not node.left or node.left.val < node.val) and \
                   (not node.right or node.right.val > node.val) and \
                    is_left_bst and is_right_bst :

                    maximum_sum = max(maximum_sum, cur_sum )
                    return True, cur_sum
                
                
                return False, 0
                    
        # ----------------------------------------
        sumBST( root )
        return maximum_sum



# n : the number of node in Binary search tree.

## Time Complexity: O( n )
#
# The overhead in time is the cost of post-order DFS traversal, which is of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the storage for recursion call stack, which is of O( n ).



def test_bench():

    ## Test_case_#1
    root_1 = TreeNode( 1 )

    root_1.left = TreeNode(4)
    root_1.right = TreeNode(3)

    root_1.left.left = TreeNode(2)
    root_1.left.right = TreeNode(4)
    root_1.right.left = TreeNode(2)
    root_1.right.right = TreeNode(5)

    root_1.right.right.left = TreeNode(4)
    root_1.right.right.right = TreeNode(6)



    ## Test_case_#2
    root_2 = TreeNode(4)

    root_2.left = TreeNode(3)

    root_2.left.left = TreeNode(1)
    root_2.left.right = TreeNode(2)



    ## Test_case_#3
    root_3 = TreeNode( -4 )
    
    root_3.left = TreeNode( -2 )
    root_3.right = TreeNode( -5 )



    ## Test_case_#4
    root_4 = TreeNode( 2 )
    root_4.left = TreeNode( 1 )
    root_4.right = TreeNode( 3 )

    test_data = [ root_1, root_2, root_3, root_4 ]

    # expected output:
    '''
    20
    2
    0
    6
    '''

    for t in test_data:
        print( Solution().maxSumBST( root = t ) )

    return 

if __name__ == '__main__':

    test_bench()