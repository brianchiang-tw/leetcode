'''

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

'''



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
        
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        
        dummy_head = ListNode('@')
        iterator = dummy_head
    
        carry_in = 0
        
        # add digit by digit
        while l1 or l2:
            
            val_1 = l1.val if l1 else 0
            val_2 = l2.val if l2 else 0
            
            carry_in, digit_sum = divmod( val_1 + val_2 + carry_in, 10)
            
            iterator.next = ListNode( digit_sum )
            iterator = iterator.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        # handle for the carry-in on most significant digit
        if carry_in:
            iterator.next = ListNode( carry_in )
        
        return dummy_head.next



# m : the length of linked list l1
# n : the length of linked list l2

## Time Complexity: O( m + n )
#
# The overhead in time is the while loop, iterating on l1 or l2, which is of O( m + n )

## Space Complexity: O( m + n )
#
# The overhead in space is the storage for the linked list of summation, which is of O( m + n )

def number_of_linked_list( node: ListNode):

    number_string = ''
    cur = node
    while cur:
        number_string += str(cur.val)
        cur = cur.next

    return number_string[::-1]

def test_bench():

    ## Test_case_1
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    head_of_sum = Solution().addTwoNumbers( l1 = l1, l2 = l2 )

    print( number_of_linked_list(head_of_sum) )



if __name__ == '__main__':

    test_bench()