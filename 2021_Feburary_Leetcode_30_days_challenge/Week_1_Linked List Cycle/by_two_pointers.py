'''

Description:

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

 

Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).



Example 2:


Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.



Example 3:


Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
 

Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.
 

Follow up: Can you solve it using O(1) (i.e. constant) memory?

'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        # two pointers
        slow, fast = head, head
        
        
        # slow runner move 1 step, fast runner move 2 steps per iteration
        # if fast runner meets slow one somewhere, then there is a cycle in linked list
        
        while fast and fast.next:
            
            slow, fast = slow.next, fast.next.next
            
            if slow is fast:
                return True
            
        return False



## Time Complexity: O( n )
#
# The overhead in time is the cost of iteration, which is of O( n )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for two-pointers, which is of O( 1 )



from typing import List
import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):
        
        a = ListNode( 1 )
        b = ListNode( 2 )
        c = ListNode( 3 )
        d = ListNode( 4 )

        a.next = b
        b.next = c
        c.next = d
        d.next = b

        result = Solution().hasCycle( head=a )
        self.assertEqual(result, True)


    def test_case_2( self ):

        a = ListNode( 1 )
        b = ListNode( 2 )
        
        a.next = b
        b.next = a

        result = Solution().hasCycle( head=a )
        self.assertEqual(result, True)

    
    def test_case_3( self ):

        a = ListNode( 1 )
        
        result = Solution().hasCycle( head=a )
        self.assertEqual(result, False)

if __name__ == '__main__':

    unittest.main()