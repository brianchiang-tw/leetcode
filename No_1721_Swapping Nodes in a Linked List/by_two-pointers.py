'''

Description:

You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]



Example 2:

Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]



Example 3:

Input: head = [1], k = 1
Output: [1]



Example 4:

Input: head = [1,2], k = 1
Output: [2,1]



Example 5:

Input: head = [1,2,3], k = 2
Output: [1,2,3]
 

Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 105
0 <= Node.val <= 100

'''



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        
        # record for first kth node, last kth node, and running cursor
        first_k, last_k, cur = None, None, head
        
        
        # Step #1: locate first_k to corresponding position
        for _ in range(k-1):
            cur = cur.next
        
        first_k = cur
        
        
        # Step #2: locate last_k to corresponding position
        last_k, cur = head, cur.next
        
        while cur:
            cur, last_k = cur.next, last_k.next
        
        # Step #3: swap value between first kth node and last kth node
        first_k.val, last_k.val = last_k.val, first_k.val
        
        return head

# n : the length of linked list 

## Time Complexity: O( n )
#
# The overhead in time is the cost of linear traversal, which is of O( n )

## Space Complexity: O( 1 )
#
# The overhead in space is the two-pointers as well as temporary vairable, which is of O( 1 )


def linked_list_builder( data ):

    last_node = None
    for val in data[::-1]:
        cur = ListNode( val )
        cur.next = last_node
        last_node = cur
    
    return last_node



def trace_linked_list( head ):

    path = []

    cur = head
    while cur:
        path.append( cur.val )
        cur = cur.next

    return path



import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        head = linked_list_builder([1, 2, 3, 4, 5])
        res = Solution().swapNodes(head, k=2)
        result = trace_linked_list( res )
        self.assertEqual(result, [1, 4, 3, 2, 5])


    def test_case_2( self ):

        head = linked_list_builder([7, 9, 6, 6, 7, 8, 3, 0, 9, 5])
        res = Solution().swapNodes(head, k=5)
        result = trace_linked_list( res )
        self.assertEqual(result,  [7, 9, 6, 6, 8, 7, 3, 0, 9, 5])


    def test_case_3( self ):

        head = linked_list_builder([1])
        res = Solution().swapNodes(head, k=1)
        result = trace_linked_list( res )
        self.assertEqual(result,  [1])


    def test_case_4( self ):

        head = linked_list_builder([1,2])
        res = Solution().swapNodes(head, k=1)
        result = trace_linked_list( res )
        self.assertEqual(result,  [2,1])


    def test_case_5( self ):

        head = linked_list_builder([1,2,3])
        res = Solution().swapNodes(head, k=2)
        result = trace_linked_list( res )
        self.assertEqual(result,  [1,2,3])        


if __name__ == '__main__':

    unittest.main()        