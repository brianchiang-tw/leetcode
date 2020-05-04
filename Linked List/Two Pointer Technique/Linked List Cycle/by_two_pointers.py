'''

Description:

Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

 

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.


Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.


Example 3:

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.


 

Follow up:

Can you solve it using O(1) (i.e. constant) memory?

'''



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        # Implementation of tortoise and hare algorithm
        
        fast, slow = head, head
        
        while True:

            try:
                
                fast = fast.next.next
                slow = slow.next
                
                if slow == fast:
                    return True
            
            except:
                
                return False
            
            
            



# N : total number of nodes in linked list

## Time complexity : O( N )
#
# The upper bound is decided by the fast runner, 
# the procedure ends either find a cycle( meets slow runner somewhere) or fetch the end of linked list ( None )
# Both cases are of O( N )

## Space complexity : O( 1 )
#
# The overhead is variable with fixed size for loop pivot fast runner and slow runner, of O( 1 ).



def test_bench():


    #   1 -> 2 -|
    #   ^       |
    #   |       |
    #   ---------
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = head

    # True
    print( Solution().hasCycle(head) )



    # 1 -> 2 -> 3 -> None
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)

    # False
    print( Solution().hasCycle(head) )

if __name__ == '__main__':

    test_bench()            