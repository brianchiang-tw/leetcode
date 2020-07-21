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
        
        dummy_head = ListNode(-1)
        dummy_head.next = head
        
        def helper(prev, node):
            
            if node:
                # general case
                if node.val == val:
					# current node is target
                    prev.next = node.next
                    helper(prev=prev, node=node.next)
                else:
					# current node is not target
                    helper(prev=node, node=node.next)
                    
            else:
				# base case aka stop condition
				# current node is None (i.e., tail of linked list)
                return
        # ----------------------------------------------
        
        helper(prev=dummy_head, node=head)
        
        return dummy_head.next



# n : the length of linked list

## Time Complexity: O( n )
#
# The major overhead in time is the depth of recursion, which is of O( n ).

## Space Complexity: O( n )
#
# The major overhead in space is the storage for recursion call stack, which is of O( n ).



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