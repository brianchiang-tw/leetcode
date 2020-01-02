'''

Description:

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3

'''



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        

        
        # dummy head node
        dummy_head_node = ListNode(0)

        prev = dummy_head_node
        prev.next = head
        
        cur = head
        
        while cur:
        
            if cur.next and cur.val != cur.next.val:
                # distinct node
                prev = cur
                cur  = cur.next
            
            else:

                if cur.next:
        
                    # detect and remove nodes of repitition
                    while cur.next and cur.val == cur.next.val :
                        cur.next = cur.next.next

                    prev.next = cur.next
                    
                else:
                    # end of linked list
                    pass

                cur = cur.next

        
        return dummy_head_node.next



# n : the length of input linked list

## Time Complexity: O( n )
#
# The major overhead in time is the outer while cur loop, which is of O( n )

## Space Complexity: O( n )
#
# The major oberhead in space is the variable for while loops, which is of O( 1 )




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
    2 3
    1 2 5 
    '''



    head = ListNode( 1 )
    head.next = ListNode( 1 )
    head.next.next = ListNode( 1 )
    head.next.next.next = ListNode( 2 )
    head.next.next.next.next = ListNode( 3 )

    head = Solution().deleteDuplicates( head )

    traverse( head )


    head = ListNode( 1 )
    head.next = ListNode( 2 )
    head.next.next = ListNode( 3 )
    head.next.next.next = ListNode( 3 )
    head.next.next.next.next = ListNode( 4 )
    head.next.next.next.next.next = ListNode( 4 )
    head.next.next.next.next.next.next = ListNode( 5 )

    head = Solution().deleteDuplicates( head )

    traverse( head )

    return 



if __name__ == '__main__':

    test_bench()