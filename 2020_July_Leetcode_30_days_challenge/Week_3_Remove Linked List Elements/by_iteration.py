'''

Description:

Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5

'''



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
		# Use dummy head make it easier to handle the case of head node removal
        dummy_head = ListNode(-1)
        dummy_head.next = head
        
        prev, cur = dummy_head, head
        
        while cur:
            
            if cur.val == val:
                
                # current node is target node
                # update linkage, and remove target node with val
                
                target = cur
                prev.next = target.next
                del target
                
                # move to next position
                cur = prev.next
                
            else:
                
                # move to next position
                prev, cur = cur, cur.next
            
        return dummy_head.next



# n : the length of linked list

## Time Complexity: O( n )
#
# The major overhead in time is the while loop iterating on cur, which is of O( n ).

## Space Complexity: O( 1 )
#
# The major overhead in space is the storage for two-pointers, which is of O( 1 ).



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

    head = linked_list_factory([1, 2, 6, 3, 4, 5, 6])

    # before:
    # 1->2->6->3->4->5->6->None
    linked_list_print(head)

    head = Solution().removeElements( head, 6)

    # after:
    # 1->2->3->4->5->None
    linked_list_print(head)



if __name__ == '__main__':

    test_bench()