'''

Description:

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

 '''

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        

        def helper( left, right):

            if left > right:
                # Base case: ( also known as stop condtion )
                return None
            
            else:
                # General case:
                # Solve by divide-and-conquer
                
                # conquer
                mid = left + (right-left)//2
                root = TreeNode(  nums[ mid ] )

                # divide
                root.left = helper( left, mid-1 )
                root.right = helper( mid+1, right )

                return root

        # ----------------------
        return helper( 0, len(nums)-1 )


# N : the number of elements in input

## Time Complexity:
#
# The overhead in time is T(n) = 2 * T(n/2) + O(1) 
# T( n ) = O( n )

## Space Complexity:
#
# The overhead in space is copying of sub-list with recursion S(n) = S * S(n/2) + O(1)
# S( n ) = O( n )


def in_order_print( root:TreeNode )->None:

    if root is None:
        print("None", end = ' ')

    else:

        in_order_print( root.left )
    
        print( root.val, end = ' ')

        in_order_print( root.right )

    return


def test_bench():

    test_data = [ -10,-3,0,5,9 ]

    root_of_bst = Solution().sortedArrayToBST( test_data )


    # expected output:
    '''
    None -10 None -3 None 0 None 5 None 9 None 
    '''
    in_order_print( root_of_bst )

    return



if __name__ == '__main__':

    test_bench()