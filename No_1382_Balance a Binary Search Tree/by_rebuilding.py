'''

Description:

Given a binary search tree, return a balanced binary search tree with the same node values.

A binary search tree is balanced if and only if the depth of the two subtrees of every node never differ by more than 1.

If there is more than one answer, return any of them.

 

Example 1:



Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2,null,null] is also correct.
 

Constraints:

The number of nodes in the tree is between 1 and 10^4.
The tree nodes will have distinct values between 1 and 10^5.

'''




# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        nums = []
        
        def inorder( node,nums):
            
            #Convert BST to ascending sequence
             
            if node:
                
                inorder( node.left, nums )
                nums.append( node.val )
                inorder( node.right, nums )
                
        # ----------------------------------------
        
        def sequence_to_balanced_BST( left, right, nums):
            
            #Convert ascending sequence to balanced BST
            
            if left > right:
                # Base case:
                return None
            
            else:
                # General case:

                mid = left + ( right - left ) // 2

                root = TreeNode( nums[mid] )

                root.left = sequence_to_balanced_BST( left, mid-1, nums)
                root.right = sequence_to_balanced_BST( mid+1, right, nums)

                return root
        
        # ----------------------------------------
        
        inorder( root, nums )
        
        return sequence_to_balanced_BST( left = 0, right = len(nums)-1, nums = nums)



# n : the number of node in binary serach tree.

## Time Complexity: O( n )
#
# The overhead in time is the cost of flattening and the cost of rebuilding, which are of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the storage for flattening list, nums, and the recursion call stack of rebuilding, which are of O( n ).

def post_order_traversal( node ):

    if node:

        post_order_traversal( node.left )
        post_order_traversal( node.right )
        print( node.val, end = ' ')



def test_bench():

    root = TreeNode( 1 )
    root.right = TreeNode( 2 )
    root.right.right = TreeNode( 3 )
    root.right.right.right = TreeNode( 4 )

    # expected output:
    '''
    Before balance operation

    4 3 2 1

    After balance operation

    1 4 3 2
    '''



    print('Before balance operation\n')
    post_order_traversal( root )

    print('\n')
    root_of_balanced_bst = ( Solution().balanceBST( root = root ) )

    print('After balance operation\n')
    post_order_traversal( root_of_balanced_bst )



if __name__ == '__main__':

    test_bench()