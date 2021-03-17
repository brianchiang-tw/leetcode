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
        
        # buffer list to save linked list, and running cursor
        buffer, cur = [], head
        
        # Step #1: save linked list into buffer list
        
        while cur:
            buffer.append(cur)
            cur = cur.next
    
    
        # Step #2: swap value between first kth node and last kth node.
        # Note: take care that most programming language is zero-based numbering
        
        buffer[k-1].val, buffer[-k].val = buffer[-k].val, buffer[k-1].val
        
        return buffer[0]

# n : the length of linked list 

## Time Complexity: O( n )
#
# The overhead in time is the cost of linear traversal, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the stroage for buffer, which is of O( n )


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