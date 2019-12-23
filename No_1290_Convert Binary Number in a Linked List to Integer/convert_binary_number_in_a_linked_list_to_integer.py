# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        value = 0
        cur = head
        
        while cur is not None:
            
            # update integer value on each iteration
            value = ( value << 1 ) | cur.val
            
            # current pointer moves to next node
            cur = cur.next
            
        return value



# n : the number of nodes in input linked list

## Time Complexity: O( n )
#
# The overhead in time is to traverse each node once to calculate corresponding decimal value
# The upper bound is the iterations of while loop, and it is of O( n )

## Space Complexity: O( 1 )
#
# The overhead in space is to maintain variable for binary-to-decimal computation.
# The size of value and cur is fixed size, thus it is of O( 1 )



def test_bench():


    # example:
    # input: binary 1101
    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(1)


    # expected output:
    '''
    13
    '''
    print( Solution().getDecimalValue(head ))

    return 



if __name__ == '__main__':

    test_bench()