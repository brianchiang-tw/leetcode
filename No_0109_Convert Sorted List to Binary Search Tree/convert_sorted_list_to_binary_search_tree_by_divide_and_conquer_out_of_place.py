'''

Description:

Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

'''



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import List
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        

        def linked_lsit_to_array( head: ListNode, sequence: List ):
            '''
            Input: head of of sorted linked list
            Output: a list with sorted value from linked list
            '''
            
            cur = head
            
            while cur:
                sequence.append( cur.val)
                cur = cur.next
                
        
        
        def array_to_BST( sequence: List ) -> TreeNode:
            '''
            Input: a list with sorted value
            Output: root node of balanced binary search tree
            '''
            
            if not sequence:
                return None
            
            else:
                
                mid = len(sequence) // 2
                
                root = TreeNode( sequence[mid] )
                
                root.left = array_to_BST( sequence[:mid])
                root.right = array_to_BST( sequence[mid+1:])
                
                return root
        
        # ----------------------------------------------
        sequence = []
        root_of_BST = None
        
        linked_lsit_to_array( head, sequence)
        root_of_BST = array_to_BST( sequence )
        return root_of_BST



# n : number of nodes in linked list

## Time Complexity: O( n log n )
#
# For linked_lsit_to_array(),
# it takes O( n ) to convert linked list to array.
#
# For array_to_BST(),
# it takes T( n ) = 2T( n / 2) + O( n ), T( n ) is of O( n log n ).

## Space Complexity: O( n )
#
# The overhead in space is the storage for temporary array, and binary search tree, which is of O( n ).



def link_list_factory( sequence: List[int] ):

    size = len(sequence)
    last_one = None

    # build linked list from tail to head
    for node_value in reversed(sequence):
        node = ListNode( node_value )

        if last_one is not None:
            node.next = last_one

        last_one = node

    head = last_one
    return head



def inorder_print( node: TreeNode):

    if node:
        inorder_print( node.left )
        print(f'{node.val} ', end = '')
        inorder_print( node.right )


def test_bench():

    test_data = [-10, -3, 0, 5, 9]

    # expected output:
    '''
    -10 -3 0 5 9 
    '''

    # head node of linked list
    head_node = link_list_factory( test_data )

    # Test the conversion of sorted linked list to binary search tree
    root_node = Solution().sortedListToBST(head_node)

    # print the inorder traversal of output BST
    inorder_print( root_node )

    return 



if __name__ == '__main__':

    test_bench()