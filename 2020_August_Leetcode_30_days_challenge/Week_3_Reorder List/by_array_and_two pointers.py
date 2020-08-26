'''

Description:

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.



Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.

'''




# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
		
		# ----------------------------------------------
		# Save linked list in array
		
        arr = []
        
        cur, length = head, 0
		
        while cur:
            arr.append( cur )
            cur, length = cur.next, length + 1
        
		# ----------------------------------------------
        # Reorder with two-pointers
		
        left, right = 0, length-1
        last = head
        
        while left < right:
            arr[left].next = arr[right]
            left += 1
            
            if left == right: 
                last = arr[right]
                break
                
            arr[right].next = arr[left]
            right -= 1
            
            last = arr[left]
        
        if last:
            last.next= None


# n : the length of input linked list

## Time Complexity: O( n )
#
# The overhead in time is the cost of iteration, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for array of nodes, which is of O( n )



def gen_linked_list( arr ):

    last, cur = None, None
    for value in reversed(arr):
        cur = ListNode( value )
        cur.next = last
        last = cur

    return cur


def traverse_linked_list( head ):

    path = []

    cur = head
    while cur:
        path.append( cur.val )
        cur = cur.next

    return path


import unittest
class Testing( unittest.TestCase ):

    def test_case_1( self ):
        
        head = gen_linked_list( arr=[1,2,3,4] )
        Solution().reorderList( head )
        result = traverse_linked_list( head )
        self.assertEqual(result, [1,4,2,3] )


    def test_case_2( self ):
        
        head = gen_linked_list( arr=[1,2,3,4,5] )
        Solution().reorderList( head )
        result = traverse_linked_list( head )
        self.assertEqual(result, [1,5,2,4,3] )


if __name__ == '__main__':

    unittest.main()