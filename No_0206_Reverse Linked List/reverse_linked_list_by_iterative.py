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
            
            # locate next hoppoing node
            next_hop = cur.next
            
            # reverse direction
            cur.next = prev
                
            prev = cur
            cur = next_hop

        # new head of reverse linked list    
        return prev
        
        

# n : the length of linked list

## Time Complexity: O( n )
#
# The overhead in time is the while loop iterating on cur, which is of O( n )

## Space Complexity: O( 1 )
#
# The revese operation is in-place, no extra space allocation is needed.
# The overhead in space is the storage for node operation, which is of O( 1 )



def traverse( node ):

    while node:
        print( node.val, end = ' ')
        node = node.next

    return



def test_bench():

    '''
    1 -> 2 -> 3 -> 4 -> 5
    '''

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    head_of_reverse = Solution().reverseList( head )


    # expected output:
    '''
    5 4 3 2 1 
    '''

    traverse( head_of_reverse)

    return



if __name__ == '__main__':

    test_bench()
