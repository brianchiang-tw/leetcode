'''

Description:

Given a linked list, rotate the list to the right by k places, where k is non-negative.




Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL



Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL

'''



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        
        # ----------------------------------------------------
        
        def get_length( node ):
            # get the length of linked list, and link tail to head
			
            n = 0
            original_head = node
            
            while True:
                
                if node:
                    
                    # update the length of linked list
                    n += 1   
                    
                    if node.next is None:
                            
                        # link the tail to head
                        node.next = original_head
                        break

                    # move to next node
                    node = node.next
                
            return n
                
        # ----------------------------------------------------
        
        if head is None:
            # Quick response for empty linked list
            return None
        
        # get the length of linked list, and link tail to head
        n = get_length(head)
        
        # remove redundnt rotation
        k = k % n 
        
        cur, new_head = head, None
        for _ in range( n - k - 1) :
            cur = cur.next
        
        # assign new head
        new_head = cur.next
        
        # break the linkage point to new_head
        cur.next = None
        
        return new_head


# n : the length of linked list

## Time Complexity: O( n )
#
# The overhead in time is the cost of while-loop and for-loop, which are of O( n )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for loop index and temporary variable, which is of O( 1 )


def linked_list_factory( elements ):
    
    last_node = None
    for element in reversed( elements ):
        cur_node = ListNode( element )
        cur_node.next = last_node
        last_node = cur_node

    return last_node


def linked_list_visit( node ):

    cur = node
    result = []

    while cur:
        result.append( cur.val )
        cur = cur.next
    
    return result


import unittest
class Testing( unittest.TestCase ):

    def test_case_1( self ):

        linked_list = linked_list_factory( elements=[0,1,2] )
        
        new_head = Solution().rotateRight(head=linked_list, k=4)
        
        result = linked_list_visit( node=new_head )

        self.assertEqual(result, [2,0,1] )


    def test_case_2( self ):

        linked_list = linked_list_factory( elements=[1,2,3,4,5] )
        
        new_head = Solution().rotateRight(head=linked_list, k=2)
        
        result = linked_list_visit( node=new_head )

        self.assertEqual(result, [4,5,1,2,3] )




if __name__ == '__main__':

    unittest.main()        