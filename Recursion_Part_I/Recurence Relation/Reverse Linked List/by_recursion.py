'''

Description:

Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?

'''



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        new_head = None
        
        def helper( head: ListNode ):
        
            if head.next is not None:

                next_hop = head.next

                # reverse next node
                helper( next_hop )

                # reverse link direction of current node
                head.next = None
                next_hop.next = head
                

            else:
                # base case:
                # Tail node is met
                # Tail node is also the new head node
                nonlocal new_head
                new_head = head

                
            
        # ---------------------------------------------
        
        if head:
            helper( head)
            return new_head
        else:
            return None



# n : the length of linked list

## Time Complexity: O( n )
#
# The overhead in time is the cost of linear traversal, which is of O( n ).


## Space Complexity: O( n )
#
# The overhead in space is the storage for recursion call stack, which is of O( n )


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

    root = linked_list_factory( [1, 2, 3, 4, 5] )
    
    # expected output:
    '''
    1->2->3->4->5->None
    '''
    linked_list_print( root )

    # expected output:
    '''
    5->4->3->2->1->None
    '''

    root = Solution().reverseList( root )

    linked_list_print( root )



if __name__ == '__main__':

    test_bench()