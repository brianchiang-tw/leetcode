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
        
        dummy_head = ListNode(-1)
        cur = dummy_head
        
        # Both l1 and l2 still have elements
        while l1 and l2:
            
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            
            cur = cur.next
            
            
            
        # if l1 is empty, directly merge l2    
        while l2:
            
            cur.next = l2
            l2, cur = l2.next, cur.next
        
        
        # if l2 is empty, directly merge l1
        while l1:
            
            cur.next = l1
            l1, cur = l1.next, cur.next
        
        
        # return the head of merged sorted linked list
        return dummy_head.next



# n : total number of element in input lists

# Time complexity
# O( n )       
# Each min value pick-up takes 1 comparison inside min() function
# Procedure of merge k sorted lists needs O(N) times of min value pick-up

# Space complexity
# O( n ) for saving all elements in the form of linked list



def linked_list_factory( elements ):
    
    last_node = None
    for element in reversed( elements ):
        cur_node = ListNode( element )
        cur_node.next = last_node
        last_node = cur_node

    return last_node



def linked_list_print( head: ListNode ):

    cur = head
    
    while cur:

        print( cur.val, end = '->' )
    
        cur = cur.next

    
    print('None\n')



def test_bench():

    head_1 = linked_list_factory( [1,2,4] )
    head_2 = linked_list_factory( [1,3,4] )

    # expected output
    '''
    1->1->2->3->4->4->None
    '''

    head_of_solution = Solution().mergeTwoLists( head_1, head_2 )

    # print out solution linked list
    linked_list_print( head_of_solution )



if __name__ == "__main__":

    test_bench()