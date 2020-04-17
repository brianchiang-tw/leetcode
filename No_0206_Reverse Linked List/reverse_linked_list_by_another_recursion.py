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
        
        new_head = None
        
        def helper( head: ListNode ):
        
            if head.next is not None:

                next_hop = head.next

                # reverse next node
                helper( next_hop )

                # reverse link direction of current node
                head.next = None
                next_hop.next = head
                
                return head

            else:
                # base case:
                # Tail node is met
                # Tail node is also the new head node
                nonlocal new_head
                new_head = head

                return head
            
        # ---------------------------------------------
        
        if head:
            # non-empty linked list
            helper( head)
            return new_head
        else:
            # empty linked list
            return None
        



# n : the length of linked list

## Time Complexity: O( n )
#
# The overhead in time is the call depth of recursion, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is to maintain call stack for recursion, which is of O( n )



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