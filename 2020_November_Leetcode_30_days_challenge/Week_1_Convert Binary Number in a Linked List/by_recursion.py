'''

Description:

Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

 

Example 1:


Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10



Example 2:

Input: head = [0]
Output: 0



Example 3:

Input: head = [1]
Output: 1



Example 4:

Input: head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
Output: 18880



Example 5:

Input: head = [0,0]
Output: 0
 

Constraints:

The Linked List is not empty.
Number of nodes will not exceed 30.
Each node's value is either 0 or 1.



Hint #1  
Traverse the linked list and store all values in a string or array. convert the values obtained to decimal value.



Hint #2  
You can solve the problem in O(1) memory using bits operation. use shift left operation ( << ) and or operation ( | ) to get the decimal value in one operation.

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        # -----------------------------
        def bin_to_dec(cur, value):
            
            if not cur:
                return value
            
            else:
                return bin_to_dec( cur=cur.next, value=(value << 1) + cur.val )
        # -----------------------------
        
        return bin_to_dec(cur=head, value=0)



# n : the length of linked list

## Time Complexity: O( n )
#
# The overhead in time is the cost of linked list traversal, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for recursion call stack, which is of O( n )


def linked_list_factory( elements ):
    
    last_node = None
    for element in reversed( elements ):
        cur_node = ListNode( element )
        cur_node.next = last_node
        last_node = cur_node

    return last_node


from typing import List
import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):
        
        root = linked_list_factory([1,0,1])
        result = Solution().getDecimalValue(head=root)
        self.assertEqual(result, 5)


    def test_case_2( self ):
        
        root = linked_list_factory([0])
        result = Solution().getDecimalValue(head=root)
        self.assertEqual(result, 0)


    def test_case_3( self ):
        
        root = linked_list_factory([1])
        result = Solution().getDecimalValue(head=root)
        self.assertEqual(result, 1)        


    def test_case_4( self ):
        
        root = linked_list_factory([1,0,0,1,0,0,1,1,1,0,0,0,0,0,0])
        result = Solution().getDecimalValue(head=root)
        self.assertEqual(result, 18880)           


    def test_case_5( self ):
        
        root = linked_list_factory([0,0])
        result = Solution().getDecimalValue(head=root)
        self.assertEqual(result, 0)                   


if __name__ == '__main__':

    unittest.main()        