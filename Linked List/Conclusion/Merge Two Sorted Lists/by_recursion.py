'''

Description:

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

'''



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        if not l1:

            # Base case:
            return l2
        
        if not l2: 

            # Base case:
            return l1

        if l1.val < l2.val:

            # General case:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1

        else:

            # General case:
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2        



# n : total number of element in input lists

# Time complexity
# O( n )       
# Each min value pick-up takes 1 comparison inside min() function
# Procedure of merge k sorted lists needs O( n ) times of min value pick-up

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