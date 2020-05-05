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
        
        try:
            head_of_even = head.next
            
        except AttributeError:
            
            # Quick response for empty linked list
            return None
        
        cur_odd, cur_even = head, head.next
        
        while cur_odd:
            
            try:
                # link next odd-indexed node
                cur_odd.next = cur_odd.next.next

                # link next even-indexed node
                cur_even.next = cur_even.next.next

                # update pointer to next position
                cur_odd = cur_odd.next 
                cur_even = cur_even.next
                
            except AttributeError:
                # Naturally stop the loop when we meet empty node (i.e., None)
                break
        
        
        # Append even-indexed linked list after the tail of odd-indexed linked list
        cur_odd.next = head_of_even
        
        return head



# n : the length of input linked list.

## Time Complexity: O( n )
#
# The overhead in time is the cost of linear scan, which is of O( n )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for temporary pointer and looping variable, which is of O( 1 )


def linked_list_builder( data ):

    last_node = None
    for val in data[::-1]:
        cur = ListNode( val )
        cur.next = last_node
        last_node = cur
    
    return last_node



def print_linked_list( head ):

    path = []

    cur = head
    while cur:
        path.append( str(cur.val) )
        cur = cur.next
    
    print( '->'.join(path) )

    return



from collections import namedtuple
TestEntry = namedtuple('TestEntry','head')
def test_bench():

    head_1 = linked_list_builder( [1,2,3,4,5] )
    head_2 = linked_list_builder( [2,1,3,5,6,4,7] )
    head_3 = linked_list_builder( [] )
    head_4 = linked_list_builder( [9] )
    head_5 = linked_list_builder( [1,2,3] )

    test_data = [
                    TestEntry( head = head_1 ),
                    TestEntry( head = head_2 ),
                    TestEntry( head = head_3 ),
                    TestEntry( head = head_4 ),
                    TestEntry( head = head_5 ),
                ]


    # expected output:
    '''
    1->3->5->2->4
    2->3->6->7->1->5->4

    9
    1->3->2
    '''


    for t in test_data:
        print_linked_list( Solution().oddEvenList( head = t.head ) ) 


    return



if __name__ == '__main__':

    test_bench()