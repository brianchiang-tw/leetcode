'''

Description:

Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?

'''



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution:
    def reverseList(self, head: ListNode) -> ListNode:        
        
        prev, cur = None, head
        
        while cur:
            
            # backup next hopping node
            next_hop = cur.next
            
            # reverse linkage direction
            cur.next = prev

            # go to next hopping node
            prev, cur = cur, next_hop
        
        # return the new head of reversed linked list
        return prev



# n : the length of linked list

## Time Complexity: O( n )
#
# The overhead in time is the while loop iterating on cur, which is of O( n )

## Space Complexity: O( 1 )
#
# The revese operation is in-place, no extra space allocation is needed.
# The overhead in space is the storage for node operation, which is of O( 1 )



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

    '''
    1->2->3->4->5->None
    '''

    head = linked_list_factory( [1,2,3,4,5] )


    # expected output:
    '''
    5->4->3->2->1->None
    '''
    head_of_reverse = Solution().reverseList( head )
    linked_list_print( head_of_reverse )

    return



if __name__ == '__main__':

    test_bench()
