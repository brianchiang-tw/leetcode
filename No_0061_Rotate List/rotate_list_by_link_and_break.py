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
        
        # connect tail and head, make a circular linked list
             
        cur, size = head, 1
        
        while cur.next:
            
            size += 1
            cur = cur.next
        
        # link
        cur.next = head
        
        
        
        # locate the new head after rotation, and break the circle
        
        r = size - ( k % size )
        cur = head
        
        for i in range(1, r):
            cur = cur.next
            
        new_head_after_rotation = cur.next
        
        # break
        cur.next = None
        
        return new_head_after_rotation


# n : the number of elements in linked list

## Time Compleixty: O( n )
#
# The major overhead in time is the while loop iterating on cur, which is of O( n ).
# The minor overhead in time is the for loop iterating on i, which is of O( n-k ).

## Space Complexity: O( 1 )
#
# The major overhead in space is the variable for looping and node operation, which is of O( 1 )



def traverse( node:ListNode ):

    cur = node

    
    while cur:
        print( cur.val, end = ' ')
        cur = cur.next

    print()

    return


def test_bench():

    # expected output:
    '''
    5 6 1 2 3 4
    '''

    head = ListNode( 1 )
    head.next = ListNode( 2 )
    head.next.next = ListNode( 3 )
    head.next.next.next = ListNode( 4 )
    head.next.next.next.next = ListNode( 5 )
    head.next.next.next.next.next = ListNode( 6 )

    head_after_rotation = Solution().rotateRight( head, 2)

    traverse( head_after_rotation )

    return 



if __name__ == '__main__':

    test_bench()