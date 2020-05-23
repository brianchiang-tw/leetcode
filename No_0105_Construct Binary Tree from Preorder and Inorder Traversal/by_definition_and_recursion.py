'''

Description:

Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        val_index_dict = { num:idx for idx, num in enumerate(inorder) }
        
        self.root_index = 0
        
        def helper( left, right):
            
            if left > right:
                # Base case:
                # return empty node as leaf node's child
                return None
            
            else:
                
                # Recall:
                # definition of preorder traversal: Center, Left, Right
                # rebuild with direction of definition
                root = TreeNode( preorder[self.root_index] )
                
                # update root index
                self.root_index += 1
                
                mid = val_index_dict[ root.val ]
                
                root.left = helper( left, mid-1 )
                root.right = helper( mid+1, right)
                
                return root
        # ----------------------------------------------------
        return helper( left = 0 , right = len(inorder)-1 )






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



def print_pre_order( node ):
    
    if node:

        print(f'{node.val} -> ', end = '')
        print_pre_order( node.left )
        print_pre_order( node.right )
        
        



def test_bench():

    preorder = [3,9,20,15,7]   
    inorder = [9,3,15,20,7]
        

    root = Solution().buildTree( preorder, inorder )


    # expected output:
    '''
    3 -> 9 -> 20 -> 15 -> 7 ->
    '''
    print_pre_order( root )

    print()

    # expected output:
    '''
    9 -> 3 -> 15 -> 20 -> 7 ->
    '''
    print_in_order( root )

    





if __name__ == '__main__':

    test_bench()    