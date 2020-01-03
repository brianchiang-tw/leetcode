'''

Description:

Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5

'''



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        dummy_head_node = ListNode(0)
        dummy_head_node.next = head
        
        prev = dummy_head_node
        cur = head 
        
        while cur:
            
            if cur.val == val:
                prev.next = cur.next
            else:    
                prev = cur
                
            cur = cur.next
            
        
        return dummy_head_node.next



# n : the length of linked list

## Time Complexity: O( n )
#
# The major overhead in time is the while loop iterating on cur, which is of O( n ).

## Space Complexity: O( 1 )
#
# The major overhead in space is the storage for node operation poitner, which is of O( 1 ).



def traverse( node:ListNode ):

    cur = node
    while cur:
        print( cur.val, end = ' ')
        cur = cur.next

    return 


def test_bench():

    head = ListNode(2)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)

    result = Solution().removeElements( head, 2)

    traverse( result )

    return 



if __name__ == '__main__':

    test_bench()