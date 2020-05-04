'''

Description:

Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:


begin to intersect at node c1.

 

Example 1:


Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,0,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
 

Example 2:


Input: intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Reference of the node with value = 2
Input Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [0,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.
 

Example 3:


Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: null
Input Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.
 

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
        
        cur_A, cur_B = headA, headB

        while cur_A != cur_B:
            
            cur_A = cur_A.next if cur_A else headB
            cur_B = cur_B.next if cur_B else headA
            
        return cur_A



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
