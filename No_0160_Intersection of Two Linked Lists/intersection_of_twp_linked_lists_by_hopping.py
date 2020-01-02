'''

Description:

Write a program to find the node at which the intersection of two singly linked lists begins.

Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.

'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        cur_a, cur_b = headA, headB
        
        while cur_a != cur_b:
            
            cur_a =  cur_a.next if cur_a else  headB 
            cur_b =  cur_b.next if cur_b else  headA 
                
        return cur_a


# m : length of linked list A
# n : length of linked list B

## Time Compleixty: O( m + n )
#
# The major overhead in time is the while loop on cur_a and cur_b, which is of O( m + n )

## Space Complexity: O( 1 )
#
# The major overhead in space is the storage for pointer cur_a and cur_b, which is of O( a )



def test_bench():

    '''
    a:      2 -> 3 -> 4
                /
    b: 1 -> 2---
    '''


    # expected output:
    '''
    3
    '''

    node_2a = ListNode(2)
    node_3 = ListNode(3)
    node_4 = ListNode(4)

    node_1b = ListNode(1)
    node_2b = ListNode(2)

    node_2a.next = node_3
    node_3.next= node_4

    node_1b.next = node_2b
    node_2b.next = node_3

    headA = node_2a
    headB = node_1b

    print( Solution().getIntersectionNode(headA, headB).val )

    return



if __name__ == '__main__':

    test_bench()