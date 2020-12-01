'''

Description:

Given an array of digits which is sorted in non-decreasing order. You can write numbers using each digits[i] as many times as we want. For example, if digits = ['1','3','5'], we may write numbers such as '13', '551', and '1351315'.

Return the number of positive integers that can be generated that are less than or equal to a given integer n.

 

Example 1:

Input: digits = ["1","3","5","7"], n = 100
Output: 20
Explanation: 
The 20 numbers that can be written are:
1, 3, 5, 7, 11, 13, 15, 17, 31, 33, 35, 37, 51, 53, 55, 57, 71, 73, 75, 77.



Example 2:

Input: digits = ["1","4","9"], n = 1000000000
Output: 29523
Explanation: 
We can write 3 one digit numbers, 9 two digit numbers, 27 three digit numbers,
81 four digit numbers, 243 five digit numbers, 729 six digit numbers,
2187 seven digit numbers, 6561 eight digit numbers, and 19683 nine digit numbers.
In total, this is 29523 integers that can be written using the digits array.



Example 3:

Input: digits = ["7"], n = 8
Output: 1
 

Constraints:

1 <= digits.length <= 9
digits[i].length == 1
digits[i] is a digit from '1' to '9'.
All the values in digits are unique.
digits is sorted in non-decreasing order.
1 <= n <= 109

'''



from typing import List

class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        
        
        N = str(n)
        size = len(N)
        
        # handle for number whose digits length smaller than size
        smaller = sum( len(digits)**d for d in range(1, size) )
        
        i = 0
        result = smaller
        
        # handle for numbers whose digits length equal to size
        while i < size:
            
            result += sum( d < N[i] for d in digits ) * ( len(digits) ** (size-1-i) )
            
            if N[i] not in digits:
                break
            
            i += 1
            
        return result + ( i==size )




# s: the size of str(N)

## Time Complexity: O( log s )
#
# The overhead in time is the cost of iteration, which is of O( log s)

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for loop index and temporary variable, which is of O( 1 )


import unittest

class Testing( unittest.TestCase ):

    def test_case_1(self):

        result = Solution().atMostNGivenDigitSet( digits = ["1","3","5","7"], n = 100 )
        self.assertEqual(result, 20)

    
    def test_case_2(self):

        result = Solution().atMostNGivenDigitSet( digits = ["1","4","9"], n = 1000000000 )
        self.assertEqual(result, 29523)

    
    def test_case_3(self):

        result = Solution().atMostNGivenDigitSet( digits = ["7"], n = 8 )
        self.assertEqual(result, 1)


if __name__ == '__main__':

    unittest.main()        