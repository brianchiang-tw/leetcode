'''

Description:

Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false


Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    
    def reverse_linked_list(self, node: ListNode)-> ListNode:
        
        prev, cur = None, node
        
        while cur:
            
            # backup original next hop
            next_hop = cur.next
            
            # reverse linkage direction
            cur.next = prev
            prev = cur
            
            # move to next position
            cur = next_hop
            
        # new head of reversed linked list
        return prev
    
	# -----------------------------------------------------------------------------
	
    def isPalindrome(self, head: ListNode) -> bool:
        
		# use two-pointers to locate the mid-point of linked list
		
        slow, fast = head, head
        
        while fast and fast.next:
            
            slow = slow.next
            fast = fast.next.next
		
		# skip central node if length of linked list is odd number.
        if fast:
            slow = slow.next
        
        # Reverse the linkage of right half of linked list
        tail = self.reverse_linked_list( slow )
        
        
        # Accept if left half sequence == right half sequence
        # Reject, otherwise
        while tail:
            
            if tail.val != head.val:
                return False
            
            head, tail = head.next, tail.next
        
        return True


# n : the length of linked list

## Time Complexity: O( n )
#
# The overhead in time is the cost of iteration, which is of O( n )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for loop index and temporary variable, which is of O( 1 )

def linked_list_factory( elements ):
    
    last_node = None
    for element in reversed( elements ):
        cur_node = ListNode( element )
        cur_node.next = last_node
        last_node = cur_node

    return last_node


import unittest

class Testing( unittest.TestCase ):

    def setUp(self) -> None:
        self.solver = Solution().isPalindrome
        return

    def test_case_1( self ):
        head = linked_list_factory([1,2,2,1])
        result = self.solver(head)
        self.assertEqual(result, True)

    def test_case_2( self ):
        head = linked_list_factory([1,2])
        result = self.solver(head)
        self.assertEqual(result, False)

if __name__ == '__main__':

    unittest.main()        