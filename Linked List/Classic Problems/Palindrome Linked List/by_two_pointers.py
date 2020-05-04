'''

Description:

Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?

'''



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    
    def reverse_linked_list(self, node: ListNode)-> ListNode:
        
        prev, cur = None, node
        
        while cur:
            
            # backup original next hop
            next_hop = cur.next
            
            # reverse linkage direction
            cur.next = prev
            prev = cur
            
            # move to next position
            cur = next_hop
            
        # new head of reversed linked list
        return prev
    
    def isPalindrome(self, head: ListNode) -> bool:
        
        slow, fast = head, head
        
        while fast and fast.next:
            
            slow = slow.next
            fast = fast.next.next

        if fast:
            slow = slow.next
        
        # Reverse the linkage of right half of linked list
        tail = self.reverse_linked_list( slow )
        
        
        # Accept if left half sequence == right half sequence
        # Reject, otherwise
        while tail:
            
            if tail.val != head.val:
                return False
            
            head, tail = head.next, tail.next
        
        return True



# n : the length of linked list

## Time Complexity: O( n )
#
# The overhead in time is the cost of linear scan on linked list, which is of O( n )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for two-pointers, which is of O( 1 )



def linked_list_factory( elements ):
    
    last_node = None
    for element in reversed( elements ):
        cur_node = ListNode( element )
        cur_node.next = last_node
        last_node = cur_node

    return last_node



from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'head_node_of_linked_list')

def test_bench():

    test_data = [
                    TestEntry( head_node_of_linked_list = linked_list_factory( [1,2] ) ),
                    TestEntry( head_node_of_linked_list = linked_list_factory( [1,2,3,2,1] ) ),
                    TestEntry( head_node_of_linked_list = linked_list_factory( [1,2,3,4,5] ) ),
                    TestEntry( head_node_of_linked_list = linked_list_factory( [1,2,2,1] ) ),
                    TestEntry( head_node_of_linked_list = linked_list_factory( [1,2,1] ) ),
                    TestEntry( head_node_of_linked_list = linked_list_factory( [0,1,2] ) ),
                    TestEntry( head_node_of_linked_list = linked_list_factory( [1,1] ) ),
                    TestEntry( head_node_of_linked_list = linked_list_factory( [1] ) ),
                ]

    # expected output:
    '''
    False
    True
    False
    True
    True
    False
    True
    True
    '''

    for t in test_data:

        print( Solution().isPalindrome( head = t.head_node_of_linked_list) )
    
    return



if __name__ == '__main__':

    test_bench()
    