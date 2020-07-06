'''

Description

Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

'''


from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        result = []
        
        # use carry_in on LSB as +1
        carry_in = 1
        
        for digit in reversed(digits):
            
            # update carry_in and digit_sum
            carry_in, digit_sum = divmod(digit + carry_in, 10)
            
            result.append(digit_sum)
        
        
        if carry_in:
            # check carry_in on MSB for last iteration
            result.append(carry_in)
            
        
        return result[::-1]



# n : the length of input list, digits.

## Time Complexity: O( n )
#
# The overhead in time is the cost of for loop, which is of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the storage for list, result, which is of O( n ).


import unittest
class Testing( unittest.TestCase ):

    def test_case_1(self):

        result = Solution().plusOne( digits = [1,2,3] )
        self.assertEqual(result, [1,2,4])
    

    def test_case_2(self):

        result = Solution().plusOne( digits = [4,3,2,1] )
        self.assertEqual(result, [4,3,2,2])


    def test_case_3(self):

        result = Solution().plusOne( digits = [9,9,9] )
        self.assertEqual(result, [1,0,0,0])
    
    


if __name__ == '__main__':

    unittest.main()