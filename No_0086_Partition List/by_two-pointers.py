'''

Description:

Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

 

Example 1:


Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]



Example 2:

Input: head = [2,1], x = 2
Output: [1,2]
 

Constraints:

The number of nodes in the list is in the range [0, 200].
-100 <= Node.val <= 100
-200 <= x <= 200

'''



# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def partition(self, head: ListNode, x:int)->ListNode:

        if not head:

            # Quick response for empty linked list
            return None


        # < as dummy head value for less_than linked list
        less_than = ListNode("<")

        # >= as dummy head value for not_less_than linked list
        not_less_than = ListNode(">=")

        # backup dummy head node position for less_than and not_less_than for linkage update later
        head_of_less_than, head_of_not_less_than = less_than, not_less_than

        ## Separate original linked list into two lists
        # one is less than x, where node value < x
        # the other is not less than x, where node value >= x

        cur = head
        while cur:

            if cur.val < x:
                less_than.next = cur
                less_than = less_than.next

            else:
                not_less_than.next = cur
                not_less_than = not_less_than.next

            cur = cur.next

        # update linkage

        # connect less than's tail to not_less_than
        less_than.next = head_of_not_less_than.next
        
        # let not_less_than's tail point to None (i.e., empty node)
        not_less_than.next = None

        return head_of_less_than.next


# n : the length of linked list

## Time Complexity: O( n )
#
# The overhead in time is the cost of linear traversal, which is of O( n )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage of two-pointers, which is of O( 1 )

def linked_list_factory( elements ):
    
    last_node = None
    for element in reversed( elements ):
        cur_node = ListNode( element )
        cur_node.next = last_node
        last_node = cur_node

    return last_node



def visit_linked_list( head: ListNode ):

    cur = head
    traversal_path = []
    while cur:

        traversal_path.append( cur.val )
        cur = cur.next

    
    return traversal_path



import unittest

class Testing( unittest.TestCase ):

    def setUp(self) -> None:
        self.solver = Solution().partition
        return


    def test_case_1( self ):

        head = linked_list_factory([1, 4, 3, 2, 5, 2])
        result = self.solver(head, x=3)

        path = visit_linked_list( result )
        self.assertEqual(path, [1,2,2,4,3,5])



    def test_case_2( self ):

        head = linked_list_factory([2, 1])
        result = self.solver(head, x=2)

        path = visit_linked_list( result )
        self.assertEqual(path, [1,2])



if __name__ == '__main__':

    unittest.main()