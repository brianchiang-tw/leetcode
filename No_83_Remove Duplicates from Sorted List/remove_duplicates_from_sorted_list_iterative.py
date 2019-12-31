'''

Description:

Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3

'''



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        cur = head
        
        while cur:
            
            # detect and remove nodes of repitition
            if cur.next and cur.val == cur.next.val :
                cur.next = cur.next.next
                continue
                
            cur = cur.next
        
        return head



# n : the length of input linked list

## Time Complexity: O( n )
#
# The major overhead in time is the while cur loop, which is of O( n )

## Space Complexity: O( n )
#
# The major oberhead in space is the variable for while loop, which is of O( 1 )




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
    1 
    1 2 3 
    '''



    head = ListNode( 1 )
    head.next = ListNode( 1 )
    head.next.next = ListNode( 1 )

    Solution().deleteDuplicates( head )

    traverse( head )


    head = ListNode( 1 )
    head.next = ListNode( 1 )
    head.next.next = ListNode( 2 )
    head.next.next.next = ListNode( 2 )
    head.next.next.next.next = ListNode( 3 )
    head.next.next.next.next.next = ListNode( 3 )

    Solution().deleteDuplicates( head )

    traverse( head )

    return 



if __name__ == '__main__':

    test_bench()