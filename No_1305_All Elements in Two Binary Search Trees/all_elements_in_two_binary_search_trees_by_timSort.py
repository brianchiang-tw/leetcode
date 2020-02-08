'''

Description:

Given two binary search trees root1 and root2.

Return a list containing all the integers from both trees sorted in ascending order.


Example 1:


Input: root1 = [2,1,4], root2 = [1,0,3]
Output: [0,1,1,2,3,4]



Example 2:

Input: root1 = [0,-10,10], root2 = [5,1,7,0,2]
Output: [-10,0,0,1,2,5,7,10]



Example 3:

Input: root1 = [], root2 = [5,1,7,0,2]
Output: [0,1,2,5,7]



Example 4:

Input: root1 = [0,-10,10], root2 = []
Output: [-10,0,10]



Example 5:


Input: root1 = [1,null,8], root2 = [8,1]
Output: [1,1,8,8]
 

Constraints:

Each tree has at most 5000 nodes.
Each node's value is between [-10^5, 10^5].

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import List
class Solution:
    
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
    
        # Step_#1:
        # Collect all elements into one list
    
        array_bst = []
    
        def inorder( node:TreeNode, array ):
            
            if node:
                
                inorder(node.left, array)
                
                array.append( node.val )
                
                inorder(node.right, array)
        
            return
        
    
        inorder(root1, array_bst)
        inorder(root2, array_bst)
        
        
        # Step_#2:
        # Sort arrat_bst
        
        output_array = sorted( array_bst )
        
        return output_array






# m : the number of nodes in binary search tree with root1
# n : the number of nodes in binary search tree with root2

## Time Complexity: O( m + n )
# Step_#1:
# The overhead in time is the cost of inorder traversal of these two BST, which is of O( m ) + O( n ) = O( m + n )
#
# Step_#2:
# The overhead in time is the cost of sorting of two sorted array by Timsort in Python, which is of O( m + n ).
#
# It takes O( m + n ) in total.

## Space Complexity: O( m + n )
#
# The overhead in space is the storage of output_array, which is of O( m + n ).



def test_bench():
    
    ## Test case_#1:
    # First binary search tree
    root_1 = TreeNode(2)
    root_1.left = TreeNode(1)
    root_1.right = TreeNode(4)

    # Second binary search tree
    root_2 = TreeNode(1)
    root_2.left = TreeNode(0)
    root_2.right = TreeNode(3)

    # expected output:
    '''
    [0, 1, 1, 2, 3, 4]
    '''
    print( Solution().getAllElements(root1 = root_1, root2= root_2) )



    ## Test case_#2:
    # First binary search tree
    root_1 = TreeNode(0)
    root_1.left = TreeNode(-10)
    root_1.right = TreeNode(10)

    # Second binary search tree
    root_2 = TreeNode(5)
    root_2.left = TreeNode(1)
    root_2.right = TreeNode(7)

    root_2.left.left = TreeNode(0)
    root_2.left.right = TreeNode(2)

    # expected output:
    '''
    [-10, 0, 0, 1, 2, 5, 7, 10]
    '''
    print( Solution().getAllElements(root1 = root_1, root2= root_2) )    

    return 



if __name__ == '__main__':

    test_bench()

