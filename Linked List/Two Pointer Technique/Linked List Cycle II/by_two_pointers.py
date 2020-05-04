'''

Description:

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.

 

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


 

Follow-up:
Can you solve it without using extra space?

'''



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        
        fast, slow = head, head
        
        while True:
            
            try:
                
                fast = fast.next.next
                slow = slow.next
                
                if slow == fast:
                    break
            
            except:
                return None
        

        # Use checker to locate the junction of cycle
        checker = head
        
        while checker != slow:
            checker = checker.next
            slow = slow.next
            
        return checker



# n : the length of input linked list

## Time Complexity: O( n )
#
# The overhead in time is the while loop iterating on two-pointers, which is of O( n ).

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for two-pointers, which is of O( 1 ).



def test_bench():

    '''
    3 -> 2 -> 0 -> 4
         ^         |
         |         |
         -----------

    '''
    # expected output:
    '''
    2
    '''
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = head.next

    junction_node = Solution().detectCycle(head)

    if junction_node:
        print( junction_node.val)
    else:
        print( "None" )

    return



if __name__ == '__main__':

    test_bench()
