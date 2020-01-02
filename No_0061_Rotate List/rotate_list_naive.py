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
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        
        
        if head is None:
            return None
        
        list_of_element = []
        cur = head
        
        while cur:
            
            list_of_element.append( cur.val )
            cur = cur.next
            
            
        k = k % len(list_of_element)
        
        list_of_element = list_of_element[::-1]
        
        list_of_element[:k] = list_of_element[:k][::-1]
        list_of_element[k:] = list_of_element[k:][::-1]
        
        
        new_head = None
        
        
        for x in list_of_element:
            
            if new_head is None:
                
                new_head = ListNode(x)
                cur = new_head
                
            else:
                
                cur.next = ListNode(x)
                cur = cur.next
                
                
        return new_head
        