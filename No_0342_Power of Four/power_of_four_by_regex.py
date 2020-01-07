'''

Description:

Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

Input: 16
Output: true
Example 2:

Input: 5
Output: false
Follow up: Could you solve it without loops/recursion?

'''



import re

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num <= 0:
            return False
        elif num == 1:
            return True
        else:
            regex = r'([0]*)$'
            pattern = re.compile(regex)
            
            binary_bit_string = '{0:b}'.format(num)
            
            result = pattern.findall(binary_bit_string)
            
            count_of_1 = binary_bit_string.count('1')
            len_of_tail_0s = len( result[0] )
            
            if len_of_tail_0s and len_of_tail_0s % 2 == 0 and count_of_1 == 1:
                return True
            else:
                return False
            
            