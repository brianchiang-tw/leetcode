'''

Description:

Given the head of a linked list, return the list after sorting it in ascending order.

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

 

Example 1:


Input: head = [4,2,1,3]
Output: [1,2,3,4]



Example 2:


Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]



Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is in the range [0, 5 * 104].
-105 <= Node.val <= 105

'''




# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


            
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        
        # -------------------------------
        
        def merge( a, b):
            
            if not a:
                return b
            
            elif not b:
                return a
            
            if a.val < b.val:
                a.next = merge(a.next, b)
                return a
                
            else:
                b.next = merge(a, b.next)
                return b
        
        # -------------------------------
        
        ## base case
        
        if head is None:
            # empty node
            return None
        
        elif head.next is None:
            # one node only
            return head
        
        ## general case
        # divide into two halves
        
        pre, slow, fast = None, head, head
        
        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next
        
        pre.next = None

        
        # sort by divide-and-conquer
        
        a = self.sortList(head)
        b = self.sortList(slow)
        result = merge(a, b)
        return result


# n : the length of linked list

## Time Complexity: O( n log n )
#
# The overhead in time is the cost of merge sort, which is of O( n log n )

## Space Complexity: O( n )
#
# The overhead in space is the cost of linked list merge, which is of O( n )



def linked_list_factory( elements ):
    
    last_node = None
    for element in reversed( elements ):
        cur_node = ListNode( element )
        cur_node.next = last_node
        last_node = cur_node

    return last_node


def linked_list_visit( node ):

    cur = node
    result = []

    while cur:
        result.append( cur.val )
        cur = cur.next
    
    return result


import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        head = linked_list_factory( [4,2,1,3] )
        head = Solution().sortList( head )
        result = linked_list_visit( head )
        self.assertEqual(result, [1, 2, 3, 4] )


    def test_case_2( self ):

        head = linked_list_factory( [-1,5,3,4,0] )
        head = Solution().sortList( head )
        result = linked_list_visit( head )
        self.assertEqual(result, [-1, 0, 3, 4, 5] )


    def test_case_3( self ):

        head = linked_list_factory( [] )
        head = Solution().sortList( head )
        result = linked_list_visit( head )
        self.assertEqual(result, [] )

if __name__ == '__main__':

    unittest.main()        
