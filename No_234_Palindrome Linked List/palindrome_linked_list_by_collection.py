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
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        
        list_of_element = []
        
        cur = head
        
        while cur:
            
            list_of_element.append( cur.val)
            
            # cur moves forward
            cur = cur.next
            
        return list_of_element == list_of_element[::-1]



# n : the length of input linked list

## Time Complexity: O( n )
#
# The major overhead in time is the while cur loop, which is of O( n )

## Space Complexity: O( n )
#
# The major oberhead in space is the storage for list_of_element, which is of O( n ).




def traverse( node:ListNode ):

    cur = node

    
    while cur:
        print( cur.val, end = ' ')
        cur = cur.next

    print()

    return





def test_bench():

    # expected output:
    '''
    True
    True
    '''



    head = ListNode( 1 )
    head.next = ListNode( 2 )
    head.next.next = ListNode( 1 )

    print( Solution().isPalindrome( head) )


    head = ListNode( 1 )
    head.next = ListNode( 2 )
    head.next.next = ListNode( 3 )
    head.next.next.next = ListNode( 3 )
    head.next.next.next.next = ListNode( 2 )
    head.next.next.next.next.next = ListNode( 1 )

    print( Solution().isPalindrome( head) )

    return 



if __name__ == '__main__':

    test_bench()