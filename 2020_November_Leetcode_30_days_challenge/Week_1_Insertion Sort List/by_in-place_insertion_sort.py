'''

Description:

Sort a linked list using insertion sort.


A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list.
With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list
 

Algorithm of Insertion Sort:

Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
It repeats until no input elements remain.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4



Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5

'''



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        
        # dummy head node, set to -infinity, which is guaranteed to be smallest value
        dummy_head = ListNode(float('-inf'))
        
        # as a basis of compare node
        compare = dummy_head
        
        # the node which is being inserted this round, initialized to be head node
        cur_selected = head
        
        # carry out insertion sort one by one
        while cur_selected:
            
            if compare and compare.val > cur_selected.val:
                
                # cur selected node is smaller than compare node, reset compare to dummy_head to find proper insert location
                compare = dummy_head
                
            while compare.next and compare.next.val < cur_selected.val:
                # 1) move to insert location by value comparison with compare node
                compare = compare.next
            
            # 2) insert cur selected node to be the one after compare node
            # 3) update cur_selected as next one after insertion
            compare.next, compare.next.next, cur_selected = cur_selected, compare.next, cur_selected.next
        
        
        return dummy_head.next


# n : the length of linked list

## Time Complexity: O( n^2 )
#
# The overhead in time is the cost of insertion sort, which is of O( n^2 )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for loop index and temporary varaible, which is of O( 1 )



def linked_list_factory( elements ):
    
    last_node = None
    for element in reversed( elements ):
        cur_node = ListNode( element )
        cur_node.next = last_node
        last_node = cur_node

    return last_node


def linked_list_traversal( node ):

    while node:
        yield node.val
        node = node.next


from typing import List
import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):
        
        root = linked_list_factory([4,2,1,3])
        result = Solution().insertionSortList(head=root)
        self.assertEqual( [ *linked_list_traversal(result) ], [1,2,3,4])


    def test_case_2( self ):
        
        root = linked_list_factory([-1,5,3,4,0])
        result = Solution().insertionSortList(head=root)
        self.assertEqual( [ *linked_list_traversal(result) ], [-1,0,3,4,5])


            


if __name__ == '__main__':

    unittest.main()                