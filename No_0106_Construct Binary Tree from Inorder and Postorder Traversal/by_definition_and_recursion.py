'''

Description:

Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7

'''



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        
        ## dictionary
        # key: number
        # value: index in inorder array
        val_index_dict = { num:idx for idx, num in enumerate(inorder) }
        
        def helper( left, right):
            
            if left > right:
                # Base case:
                # return empty node as leaf node's child
                return None
            
            else:
                
                # Recall:
                # definition of postorder traversal: Left, Right, Center
                # rebuild with reversed direction ( from right to left )
                root = TreeNode( postorder.pop() )
                
                mid = val_index_dict[ root.val ]
                
                root.right = helper( mid+1, right)
                root.left = helper( left, mid-1 )
                return root
        # ----------------------------------------------------
        
        ## Top-down rebuild binary tree with definition
        return helper( left = 0, right = len(inorder)-1 )



# n : the length of input list

## Time Complexity: O( n )
#
# The overhead in time is the cost of DFS, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for recursion stack, which is of O( n )


def print_in_order( node ):

    if node:

        print_in_order( node.left )
        print(f'{node.val} -> ', end = '')
        print_in_order( node.right )



def print_post_order( node ):
    
    if node:

        print_in_order( node.left )
        print_in_order( node.right )
        print(f'{node.val} -> ', end = '')
        



def test_bench():

    inorder = [9,3,15,20,7]
    postorder = [9,15,7,20,3]        

    root = Solution().buildTree( inorder, postorder )

    # expected output:
    '''
    9 -> 3 -> 15 -> 20 -> 7 ->
    '''
    print_in_order( root )

    print()

    # expected output:
    '''
    9 -> 15 -> 20 -> 7 -> 3 ->
    '''
    print_post_order( root )



if __name__ == '__main__':

    test_bench()    