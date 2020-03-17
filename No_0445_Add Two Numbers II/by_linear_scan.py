'''

Description:

You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7

'''




# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        
        def get_number( node: ListNode):
            
            number = 0
            
            while node:
                
                number = number * 10 + node.val
                
                node = node.next
                
            return number
        
        
        # -------------------------------------
        
        def make_linked_list( x: int):
            
            dummy_head = ListNode( 0 )            
            next_node = None
            
            if x == 0:
                return dummy_head
            
            while x:
                
                dummy_head.next = ListNode( x % 10 )
                dummy_head.next.next = next_node
                
                next_node = dummy_head.next
                x = x // 10
            
            return dummy_head.next
        
        # -------------------------------------
        
        a = get_number( l1 )
        b = get_number( l2 )
        
        
        return make_linked_list( a + b )



# m : the length of first linked list input
# n : the length of second linked list input

## Time Complexity: O( m + n )
#
# The overhead in time is the cost of linear scan, which is O( m + n )

## Space Complexity: O( max(m, n) )
#
# The overhead in space is the storage for output linked list, which is of O( max(m, n) )

def print_linked_list( node ):

    while node:
        print( node.val, end = ' ')
        node = node.next



def test_bench():

    l1 = ListNode(7)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    l1.next.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    result = Solution().addTwoNumbers( l1, l2 )

    print_linked_list( result )



if __name__ == '__main__':

    test_bench()