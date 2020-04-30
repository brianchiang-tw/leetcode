'''

Description:

Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

Given linked list -- head = [4,5,1,9], which looks like following:



 

Example 1:

Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.



Example 2:

Input: head = [4,5,1,9], node = 1
Output: [4,5,9]
Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.
 

Note:

The linked list will have at least two elements.
All of the nodes' values will be unique.
The given node will not be the tail and it will always be a valid node of the linked list.
Do not return anything from your function.

'''



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        # victim is the one which is node's next
        # let current node copy the value of next node
        # then break the linkage of next node
        
        node.val, node.next = node.next.val, node.next.next



# n : the length of linked list

## Time Compleixty: O( 1 )
#
# The overhead in time is the victim node operation, which is of O( 1 ).


## Space Complexity: O( 1 )
#
# The overhead in space is the storage for node operation, which is of O( 1 ).



def traverse( node:ListNode ):

    cur = node
    while cur:
        print( cur.val, end = ' ')
        cur = cur.next

    return 



def test_bench():

    '''
    1 -> 2 -> 3 -> 4, delete node 2
    '''

    # expexted output:
    '''
    1 3 4
    '''

    head = ListNode(1)
    node_2 = ListNode(2)
    head.next = node_2
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)

    Solution().deleteNode( node_2 )

    traverse( head )

    return



if __name__ == '__main__':

    test_bench()