'''

Description:

Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?

Hint:
Maintain two pointers and update one with a delay of n steps.

'''



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        # use dummy head will make the removal of head node easier
        dummy_head = ListNode(-1)
        dummy_head.next = head
        
        # cur keeps iteration till the end
        # prev_of_removal traverses to the previous node of the one of being removed
        cur, prev_of_removal = dummy_head, dummy_head
        
        
        while cur.next != None:
            
            # n-step delay for prev_of_removal
            if n <= 0:
                prev_of_removal = prev_of_removal.next
                
            cur = cur.next
            
            n -=1
        
        
        # Remove the N-th node from end of list
        n_th_node = prev_of_removal.next
        prev_of_removal.next = n_th_node.next
        
        del n_th_node
        
        return dummy_head.next



# n : the length of linked list

## Time Complexity: O( n )
#
# The overhead in time is the cost of linear scan of linked list, which is of O( n ).

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for two-pointers, which is of O( 1 ).


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


    # expected output:
    '''
    1->2->3->4->None
    '''
    head_of_test_1 = linked_list_factory( [1,2,3,4,5] )
    head_of_test_1 = Solution().removeNthFromEnd( head_of_test_1, 1 )
    linked_list_print( head_of_test_1 )



    # expected output:
    '''
    1->2->3->5->None
    '''
    head_of_test_2 = linked_list_factory( [1,2,3,4,5] )
    head_of_test_2 = Solution().removeNthFromEnd( head_of_test_2, 2 )
    linked_list_print( head_of_test_2 )



    # expected output:
    '''
    1->2->4->5->None
    '''
    head_of_test_3 = linked_list_factory( [1,2,3,4,5] )
    head_of_test_3 = Solution().removeNthFromEnd( head_of_test_3, 3 )
    linked_list_print( head_of_test_3 )



    # expected output:
    '''
    1->3->4->5->None
    '''
    head_of_test_4 = linked_list_factory( [1,2,3,4,5] )
    head_of_test_4 = Solution().removeNthFromEnd( head_of_test_4, 4 )
    linked_list_print( head_of_test_4 )



    # expected output:
    '''
    2->3->4->5->None
    '''
    head_of_test_5 = linked_list_factory( [1,2,3,4,5] )
    head_of_test_5 = Solution().removeNthFromEnd( head_of_test_5, 5 )
    linked_list_print( head_of_test_5 )





if __name__ == '__main__':

    test_bench()