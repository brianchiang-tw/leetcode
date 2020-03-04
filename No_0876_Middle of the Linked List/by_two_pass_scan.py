'''

Description:

Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.

 

Example 1:

Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.



Example 2:

Input: [1,2,3,4,5,6]
Output: Node 4 from this list (Serialization: [4,5,6])
Since the list has two middle nodes with values 3 and 4, we return the second one.
 

Note:

The number of nodes in the given list will be between 1 and 100.

'''



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        
        def get_length( node: ListNode)-> int:
            
            cur, length = node, 0
            while cur:
                cur = cur.next
                length += 1
                
            return length
        
        # -----------------------------------------
        
        length = get_length(head)
        
        mid = ( length // 2 )
        
        iterator = head
        for i in range(mid):
            iterator = iterator.next
            
        return iterator



# n : the number of nodes in linked list

## Time Complexity: O( n )
#
# The overhead in time is the while loop, iterating on linked list, which is of O( n )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for fast runner and slow runner, which is of O( 1 )


def test_bench():

    ## test case_#1

    root_1 = ListNode(1)
    root_1.next = ListNode(2)
    root_1.next.next = ListNode(3)
    root_1.next.next.next = ListNode(4)
    root_1.next.next.next.next = ListNode(5)

    mid_node = Solution().middleNode( head = root_1)
    # expected output:
    '''
    3
    '''
    print( mid_node.val )



    ## test case_#2

    root_1 = ListNode(1)
    root_1.next = ListNode(2)
    root_1.next.next = ListNode(3)
    root_1.next.next.next = ListNode(4)
    root_1.next.next.next.next = ListNode(5)
    root_1.next.next.next.next.next = ListNode(6)

    mid_node = Solution().middleNode( head = root_1)
    # expected output:
    '''
    4
    '''
    print( mid_node.val )


if __name__ == '__main__':

    test_bench()