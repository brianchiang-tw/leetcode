'''

Description:

Given a binary tree root and a linked list with head as the first node. 

Return True if all the elements in the linked list starting from the head correspond to some downward path connected in the binary tree otherwise return False.

In this context downward path means a path that starts at some node and goes downwards.

 

Example 1:



Input: head = [4,2,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: true
Explanation: Nodes in blue form a subpath in the binary Tree.  



Example 2:



Input: head = [1,4,2,6], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: true



Example 3:

Input: head = [1,4,2,6,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: false
Explanation: There is no path in the binary tree that contains all the elements of the linked list from head.
 

Constraints:

1 <= node.val <= 100 for each node in the linked list and binary tree.
The given linked list will contain between 1 and 100 nodes.
The given binary tree will contain between 1 and 2500 nodes.

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

class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        
        def string_of_linked_list( head: ListNode ):
            
            linked_list_string = ''
            cur = head
            
            while cur:
                linked_list_string += str( cur.val ) + ','
                cur = cur.next
                
            return linked_list_string
                
        # ----------------------------------------------------
        
        # Get the path string of linked list
        linked_list_string = string_of_linked_list( head )
        
        # ----------------------------------------------------
            
        def dfs( node: TreeNode, path_string: str) -> bool:
            
            if not node:
                
                # If path string of binary tree includes path string of linked list, 
                # then Accept and return True
                if path_string.find(linked_list_string) != -1:
                    return True
                else:
                    return False
                
                
            else:

                # Update path string of binary tree, and DFS down to next level

                path_string += str( node.val) + ','
                return dfs( node.left, path_string ) or dfs( node.right, path_string )
        
        # -----------------------------------------------------
        
        return dfs( root, '')



# m : the length of input linked list
# n : the number of nodes of binary tree

## Time Complexity: O( n^2 * m )
# The overhead in time is the cost of DFS and the cost of substring matching.
# The cost of DFS is O( n ), and the cost of substring matching is O( m*n )

## Space Complexity: O( m + n )
#
# The overhead in space is the storage for path strins for linked list and binary tree, which are of O( m + n ).



def test_bench():

    ## Test_case_#1
    root_1 = TreeNode(1)
    root_1.left = TreeNode(4)
    root_1.right = TreeNode(4)

    root_1.left.right = TreeNode(2)
    root_1.right.left = TreeNode(2)

    root_1.left.right.left = TreeNode(1)
    root_1.right.left.left = TreeNode(6)
    root_1.right.left.right = TreeNode(8)

    root_1.right.left.right.left = TreeNode(1)
    root_1.right.left.right.right = TreeNode(3)

    head_1 = ListNode(4)
    head_1.next = ListNode(2)
    head_1.next.next = ListNode(8)
    # expected output:
    '''
    True
    '''

    print( Solution().isSubPath(head = head_1, root = root_1) )



    ## Test_case_#2
    root_2 = TreeNode(1)
    root_2.left = TreeNode(4)
    root_2.right = TreeNode(4)

    root_2.left.right = TreeNode(2)
    root_2.right.left = TreeNode(2)

    root_2.left.right.left = TreeNode(1)
    root_2.right.left.left = TreeNode(6)
    root_2.right.left.right = TreeNode(8)

    root_2.right.left.right.left = TreeNode(1)
    root_2.right.left.right.right = TreeNode(3)

    head_2 = ListNode(1)
    head_2.next = ListNode(4)
    head_2.next.next = ListNode(2)
    head_2.next.next.next = ListNode(6)
    head_2.next.next.next.next = ListNode(8)
    # expected output:
    '''
    False
    '''

    print( Solution().isSubPath(head = head_2, root = root_2) )


    return



if __name__ == '__main__':

    test_bench()