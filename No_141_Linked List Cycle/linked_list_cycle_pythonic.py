'''

Description:

Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, 
we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. 

If pos is -1, then there is no cycle in the linked list.

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        try:
            slow_runner, fast_runner = head, head.next

            while slow_runner is not fast_runner:

                slow_runner, fast_runner = slow_runner.next, fast_runner.next.next
                
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