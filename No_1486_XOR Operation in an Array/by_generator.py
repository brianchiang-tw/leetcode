'''

Description:

Given an integer n and an integer start.

Define an array nums where nums[i] = start + 2*i (0-indexed) and n == nums.length.

Return the bitwise XOR of all elements of nums.

 

Example 1:

Input: n = 5, start = 0
Output: 8
Explanation: Array nums is equal to [0, 2, 4, 6, 8] where (0 ^ 2 ^ 4 ^ 6 ^ 8) = 8.
Where "^" corresponds to bitwise XOR operator.



Example 2:

Input: n = 4, start = 3
Output: 8
Explanation: Array nums is equal to [3, 5, 7, 9] where (3 ^ 5 ^ 7 ^ 9) = 8.



Example 3:

Input: n = 1, start = 7
Output: 7



Example 4:

Input: n = 10, start = 5
Output: 2
 

Constraints:

1 <= n <= 1000
0 <= start <= 1000
n == nums.length

'''



class Solution:
    def xorOperation(self, n: int, start: int) -> int:

        def series(n: int, start:int):
            
			# generate next number by definition
            for i in range(n):
                yield (start + 2 * i)
                
        # -------------------------------------------------
        
        result = 0
		
		# compute XOR for all number in given series
        for next_number in series(n, start):
            result ^= next_number
            
        return result



# n : the value of input parameter n

## Time Complexity: O( n )
#
# The overhead in time is the cost of for loop iteration, which is of O( n ).

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for loop index and temporary variable, which are of O( 1 ).


import unittest
class Testing( unittest.TestCase ):

    def test_case_1(self):

        result = Solution().xorOperation( n = 5, start = 0 )
        self.assertEqual( result, 8)



    def test_case_2(self):
    
        result = Solution().xorOperation( n = 4, start = 3 )
        self.assertEqual( result, 8)



    def test_case_3(self):
        
        result = Solution().xorOperation( n = 1, start = 7 )
        self.assertEqual( result, 7)



    def test_case_3(self):
        
        result = Solution().xorOperation( n = 1, start = 7 )
        self.assertEqual( result, 7)



    def test_case_4(self):
        
        result = Solution().xorOperation( n = 10, start = 5 )
        self.assertEqual( result, 2)




if __name__ == '__main__':

    unittest.main()