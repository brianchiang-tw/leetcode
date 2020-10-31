'''

Description:

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Notice that you should not modify the linked list.

Follow up:

Can you solve it using O(1) (i.e. constant) memory?

 

Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.



Example 2:


Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.



Example 3:


Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.
 

Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.

'''



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:

        slow, fast = head, head

        # check cycle exist or not
        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
				# slow and fast meet somewhere in linked list, it has cycle
                break
				
        else:
			# no cycle
            return None


        # locate junction point from head node
        cur = head

        while cur != slow:
            cur = cur.next
            slow = slow.next
        
        return cur



# n : the nodes of linked list

## Time Complexity: O( n )
#
# The overhead in time is the cost of cycle detection, which is of O( n )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage of double pointers, which is of O( 1 )



import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        node_1 = ListNode(1)
        node_2 = ListNode(2)
        node_3 = ListNode(3)
        node_4 = ListNode(4)
        node_5 = ListNode(5)

        node_1.next = node_2
        node_2.next = node_3
        node_3.next = node_4
        node_4.next = node_5

        # make a cycle edge points from 5 to 3
        node_5.next = node_3

        # junction point should be node_3
        result = Solution().detectCycle( node_1 )
        self.assertEqual(result, node_3)


    def test_case_2( self ):

        node_1 = ListNode(1)
        node_2 = ListNode(2)
        node_3 = ListNode(3)
        node_4 = ListNode(4)
        node_5 = ListNode(5)

        node_1.next = node_2
        node_2.next = node_3
        node_3.next = node_4
        node_4.next = node_5

        # no cycle edge in this test case

        # junction point should be None
        result = Solution().detectCycle( node_1 )
        self.assertEqual(result, None)



if __name__ == '__main__':

    unittest.main()        