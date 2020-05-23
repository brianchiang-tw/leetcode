'''

Description:

Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL



Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL

'''



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        
        # corner case
        if head is None:
            return None
        
        # Step_#1
        # connect tail and head, make a circular linked list
             
        cur, size = head, 1
        
        while cur.next:
            
            size += 1
            cur = cur.next
        
        # link
        cur.next = head
        
        
        # Step_#2
        # locate the new head after rotation, and break the circle
        
        r = size - ( k % size )
        cur = head
        
        for i in range(1, r):
            cur = cur.next
            
        new_head_after_rotation = cur.next
        
        # break
        cur.next = None
        
        return new_head_after_rotation



# n : the length of linked list

## Time Complexity: O( n )
#
# The overhead in time is the cost of linear traversal, which is of O( n ).

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for loop index and temporary variable, which is of O( n ).



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



from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'linked_list k')

def test_bench():

    test_data = [
                    TestEntry( linked_list = linked_list_factory([1,2,3,4,5]), k = 2 ),
                    TestEntry( linked_list = linked_list_factory([0,1,2]), k = 4 ),
                ]

    # expected output:
    '''
    4->5->1->2->3->None
    2->0->1->None
    '''

    for t in test_data:

        result =  Solution().rotateRight( head = t.linked_list, k = t.k)
        linked_list_print( result )
    
    return



if __name__ == '__main__':

    test_bench()