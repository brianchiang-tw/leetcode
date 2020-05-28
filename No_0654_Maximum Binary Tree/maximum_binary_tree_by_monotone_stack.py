'''

Description:

Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

The root is the maximum number in the array.
The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
Construct the maximum tree by the given array and output the root node of this tree.



Example 1:
Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    / 
     2  0   
       \
        1
Note:
The size of the given array will be in the range [1,1000].

'''



# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution(object):
    def constructMaximumBinaryTree(self, nums):

        if not nums:
            # Quick respnse for empty list
            return None

        monotone_stack = []

        for number in nums:

            cur_node = TreeNode( number )
            last_pop = None

            while monotone_stack and monotone_stack[-1].val < number:

                last_pop = monotone_stack.pop()
            
            # maximum element of monotone stack is left child of current node
            cur_node.left = last_pop

            if monotone_stack:
                # minimum element of monotone stack's right child is currnet node
                monotone_stack[-1].right = cur_node
            
            monotone_stack.append( cur_node )

        # root of maximum binary tree
        return monotone_stack[0]



# n : the length of input list nums

## Time Complexity: O( n )
#
# The overhead in time is the cost of linear scan with monotone stack, which is of O( n )

## Sapace Complexity: O( n )
#
# The overhead in space is the cost of tree building and monotone stack, which is of O( n )



def print_in_order( node ):

    if node:

        print_in_order( node.left )
        print( f'{node.val} -> ', end = ' ')
        print_in_order( node.right )



def test_bench():

    test_data = [3,2,1,6,0,5]

    # expected output:
    '''
    3 ->  2 ->  1 ->  6 ->  0 ->  5 ->  
    '''
    root = Solution().constructMaximumBinaryTree( test_data )

    print_in_order( root )



if __name__ == '__main__':

    test_bench()