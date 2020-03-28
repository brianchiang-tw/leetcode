'''

Description:

Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL

'''



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        
        if m == n:
            # Quick response for empty reverse interval
            return head
        
        dummy_head = ListNode(0)
        dummy_head.next = head
        
        cur, prev = head, dummy_head
        cur_idx = 1
        
        # left sentry is the the m-th node
        # right sentry is the the n-th node
        left_sentry, right_sentry = None, None
        
        # left junction is the (m-1)-th node
        # right junction is the (n+1)-th node
        left_junction, right_junction = None, None
        
        rev = False
        
        while cur:
            
            if rev:
                # now we are in reverse interval
                
                # Backup original next node
                ori_next = cur.next
                
                # Let current node point to previous node
                cur.next = prev
                
                # Update previous node
                # Update current point to original next node
                prev = cur
                cur = ori_next
                
                # Handle for right junction node
                if cur_idx == n:
                    right_sentry = prev
                    right_junction = cur

                    # Construct new linkage based on left junction and right junction
                    left_junction.next = right_sentry
                    left_sentry.next = right_junction

                    # turn oof reverse flag
                    rev = False              
                
                
            else:
                # now we are in normal interval
                
                # Handle for left junction node
                if cur_idx == m:
                
                    left_sentry = cur
                    left_junction = prev
                    
                    # turn on reverse flag
                    rev = True


                # Update previous node
                # Update current point to original next node
                prev = cur
                cur = cur.next
            
            
  
            # update visiting index
            cur_idx +=1
            
        return dummy_head.next



# n : the length of linked list

## Time Complexity: O( n )
#
# The overhead in time is the cost of linear scan, which is of O( n )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for temporary node and loop index, which is of O( 1 )


from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'headnode m n')


def print_link_list( head: ListNode):

    cur = head
    path = []
    while cur:

        path.append( str(cur.val) )
        cur = cur.next
    
    print( '->'.join( path ) )


def test_bench():

    head_1 = ListNode(3)
    head_1.next = ListNode(5)

    head_2 = ListNode(1)
    head_2.next = ListNode(2)
    head_2.next.next = ListNode(3)
    head_2.next.next.next = ListNode(4)
    head_2.next.next.next.next = ListNode(5)

    head_3 = ListNode(5)

    test_data = [
                    TestEntry( headnode = head_1, m = 1, n = 2),
                    TestEntry( headnode = head_2, m = 2, n = 4),
                    TestEntry( headnode = head_3, m = 1, n = 1),
                ]

    # expected output:
    '''
    5->3
    1->4->3->2->5
    5
    '''

    for t in test_data:
        head_of_rev =  Solution().reverseBetween( head = t.headnode, m = t.m, n = t.n) 

        print_link_list( head_of_rev )


    return



if __name__ == '__main__':

    test_bench()