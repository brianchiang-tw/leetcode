'''

Description:

Given a binary string s (a string consisting only of '0' and '1's).

Return the number of substrings with all characters 1's.

Since the answer may be too large, return it modulo 10^9 + 7.

 

Example 1:

Input: s = "0110111"
Output: 9
Explanation: There are 9 substring in total with only 1's characters.
"1" -> 5 times.
"11" -> 3 times.
"111" -> 1 time.



Example 2:

Input: s = "101"
Output: 2
Explanation: Substring "1" is shown 2 times in s.



Example 3:

Input: s = "111111"
Output: 21
Explanation: Each substring contains only 1's characters.



Example 4:

Input: s = "000"
Output: 0
 

Constraints:

s[i] == '0' or s[i] == '1'
1 <= s.length <= 10^5

'''



class Solution:
    def numSub(self, s: str) -> int:
        
		# record of previous ditit
        prev = 0
        
        number_of_substrings_of_1 = 0
        
		# linear scan
        for char in s:
            
			# type conversion to integer
            cur_num = int(char)
            
            if cur_num:
				# current digit is 1
                
                cur_num = prev + 1
                
				# add counter
                number_of_substrings_of_1 += cur_num
                    
            prev = cur_num
            
        return number_of_substrings_of_1 % (10**9 + 7)


# n : the length of input string

## Time Complexity: O( n )
#
# The overhead in time is the cost of iteration, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for loop index and counter, which is of O( 1 )

import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().numSub(s = "0110111")
        self.assertEqual(result, 9)


    def test_case_2( self ):
    
        result = Solution().numSub(s = "101")
        self.assertEqual(result, 2)


    def test_case_3( self ):
        
        result = Solution().numSub(s = "111111")
        self.assertEqual(result, 21)


    def test_case_4( self ):
            
        result = Solution().numSub(s = "000")
        self.assertEqual(result, 0)       



if __name__ == '__main__':

    unittest.main() 