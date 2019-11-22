'''

Description:

Merge two sorted linked lists and return it as a new list. 
The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        # dummy head node
        head_node = ListNode(0)
        
        # maintain a insert position for incoming new node with minimal value
        insert_position = head_node
        
        while l1 is not None and l2 is not None:
            
            if l1.val < l2.val:
                
                insert_position.next= ListNode( l1.val )
                
                # update insert position
                insert_position = insert_position.next
                
                # l1 move to next element
                l1 = l1.next
                
            else:
                
                insert_position.next = ListNode( l2.val )
                
                # update insert position
                insert_position = insert_position.next
                
                # l2 move to next element
                l2 = l2.next
            
        
        # if l2 is empty, dump l1
        while l1 is not None:
            
            insert_position.next = ListNode( l1.val )
            
            insert_position = insert_position.next
            l1 = l1.next
            
        while l2 is not None:
            
            insert_position.next = ListNode( l2.val )
            
            insert_position = insert_position.next
            l2 = l2.next
    
        real_head_node = head_node.next
        return real_head_node



# N : total number of element in input lists

# Time complexity
# O( N )       
# Each min value pick-up takes 1 comparison inside min() function
# Procedure of merge k sorted lists needs O(N) times of min value pick-up

# Space complexity
# O( N ) for saving all elements in the form of linked list



def test_bench():

    list_1 = ListNode(1)
    list_1.next = ListNode(2)
    list_1.next.next = ListNode(4)

    list_2 = ListNode(1)
    list_2.next = ListNode(3)
    list_2.next.next = ListNode(4)

    head_of_solution = Solution().mergeTwoLists( list_1, list_2 )

    # print out solution linked list
    current = head_of_solution

    while current is not None:

        print( current.val )

        current = current.next

    # expected output
    '''
    1
    1
    2
    3
    4
    4
    '''




if __name__ == "__main__":

    test_bench()