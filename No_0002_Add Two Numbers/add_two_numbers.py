'''
Description:

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

'''



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def get_num_from_linklist( self, node ):
        
        current = node
        str_number = str()
        
        while( current is not None ):
            
            # concatenating number into str_numer in temrs of string
            str_number += str(current.val)
            
            # move to next node
            current = current.next
            
        # reverse string to get in-order form
        str_number = str_number[::-1]
        
        # convert string to integer
        return int(str_number)
        
        
        
    def make_strnum_to_linklist( self, str_num ):
        
        # Last digit of str_num is head node
        head_node = ListNode( str_num[-1] )
        
       
        while len(str_num) != 1 :
            
            # append one digit
            new_node = ListNode( str_num[0] )
            # shrink str_num by one character
            str_num = str_num[1:]
        
            # append to linklist
            if head_node.next is None:
                # next of head_node is None
                
                head_node.next = new_node
                
            else:
                # next of head_node is another node
                
                next_of_new_node = head_node.next
                
                # assign new_node as head_node's next
                head_node.next = new_node
                
                # assign new_of_new_node as new_node's next
                new_node.next = next_of_new_node
        
        
        return head_node
    
    
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        num_1 = self.get_num_from_linklist( l1 )
        
        num_2 = self.get_num_from_linklist( l2 )
        
        sum = num_1 + num_2
        
        str_sum = str(sum)
        
        head_of_link_list = self.make_strnum_to_linklist( str_sum )
        
        return head_of_link_list
    

        
    