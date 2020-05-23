'''

Description:

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



# m : the length of input linked list l1
# n : the length of input linked list l2

## Time Complexity: O( max(m, n) )
#
# The overhead in time is the cost of iteration of addition, which is of O( max(m,n) )

## Space Complexity: O( max(m, n) )
#
# The overhead in space is the storage for linked list of addition result, which is of O( max( m ,n ) )


from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'a b')



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

    test_data = [
                    TestEntry( a = linked_list_factory( [2, 4, 3 ] ), b = linked_list_factory( [5, 6, 4 ] )),
                    TestEntry( a = linked_list_factory( [3] ), b = linked_list_factory( [9, 9, 9 ] ) ),
                ]

    # expected output:
    '''
    7->0->8->None
    2->0->0->1->None
    '''

    for t in test_data:

        result = Solution().addTwoNumbers( l1 = t.a, l2 = t.b )
        linked_list_print( result )

    return



if __name__ == '__main__':

    test_bench()


        
    