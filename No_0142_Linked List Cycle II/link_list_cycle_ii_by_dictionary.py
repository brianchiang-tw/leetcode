'''

Description:

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.

'''



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        
        id_node_dict = {}
        
        cur = head
        
        while cur:
            
            if id(cur) in id_node_dict:
                # with cycle, return the junction node
                return id_node_dict[id(cur)]
            
            else:
                
                # update dictionary
                # key = object id
                # value = node
                id_node_dict [id(cur) ]  = cur
                
                # keep moving
                cur = cur.next
        
        
        # without cycle, return Null
        return None



# n : the length of input linked list

## Time Complexity: O( n )
#
# The overhead in time is the while loop iterating on cur, which is of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the storage for the dictionary, id_node_dict, which is of O( n ).



def test_bench():

    '''
    3 -> 2 -> 0 -> 4
         ^         |
         |         |
         -----------

    '''
    # expected output:
    '''
    2
    '''
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = head.next

    junction_node = Solution().detectCycle(head)

    if junction_node:
        print( junction_node.val)
    else:
        print( "None" )

    return



if __name__ == '__main__':

    test_bench()
