'''

Description:

Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL



Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
Note:

The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...

'''



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        
        head_of_even = None
        
        try:
            
            head_of_even = head.next
            
        except AttributeError:
            # Linked list is either empty or of one node only
            return head
        
        cur_odd, cur_even = head, head_of_even
        
        while True:
            
            try:
                # link odd-indexed node
                cur_odd.next = cur_odd.next.next
                
                # link even-indexed node
                cur_even.next = cur_even.next.next
            
                # move to next position
                cur_odd, cur_even = cur_odd.next, cur_even.next
            
            except AttributeError:
                break
        
        # append even nodes to tail of odd nodes
        cur_odd.next = head_of_even
        
        return head



# n : the length of linke list

## Time Complexity: O( n )
# 
# The overhead in time is the cost of linear scan, which is of O( n ).

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for two-pointers and temporary varaible, which are of O( 1 )






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

    test_data = [
                    linked_list_factory( [1,2,3,4,5] ),
                    linked_list_factory( [2,1,3,5,6,4,7] ),
                ]

    # expected output:
    '''
    1->3->5->2->4->None
    2->3->6->7->1->5->4->None
    '''

    for t in test_data:

        head_of_result =  Solution().oddEvenList( head = t )

        linked_list_print( head_of_result )
    
    return



if __name__ == '__main__':

    test_bench()    