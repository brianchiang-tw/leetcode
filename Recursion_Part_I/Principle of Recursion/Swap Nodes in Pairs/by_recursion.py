'''

Description:

Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

 

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.

'''



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        cur = head
               
        try:
            
            # locate head of next pair
            next_pair = cur.next.next
            
            # reverse next pair
            junction = self.swapPairs( next_pair )
            
            # reverse current pair
            original_next = cur.next
            
            original_next.next = cur
            
            # build new linkage from current pair to next pair
            cur.next = junction
            
            return original_next
            
        except:
            
            # Base case:
            # Either one node or None remaining
            return cur



# n : the number of length of linked list

## Time Complexity: O( n )
#
# The overhed in time is the cost of linear traversal, which is of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the storage for recursion stack, which is of O( n ).



def linked_list_factory( elements ):
    
    last_node = None
    for element in reversed( elements ):
        cur_node = ListNode( element )
        cur_node.next = last_node
        last_node = cur_node

    return last_node



def linked_list_print( head: ListNode ):

    cur = head
    
    while cur:

        print( cur.val, end = '->' )
    
        cur = cur.next

    
    print('None\n')



def test_bench():

    root = linked_list_factory( [1, 2, 3, 4 ] )

    # expected output:
    '''
    1->2->3->4->None
    '''
    linked_list_print( root )

    root = Solution().swapPairs( root )

    # expected output:
    '''
    2->1->4->3->None
    '''

    linked_list_print( root )




if __name__ == '__main__':

    test_bench()