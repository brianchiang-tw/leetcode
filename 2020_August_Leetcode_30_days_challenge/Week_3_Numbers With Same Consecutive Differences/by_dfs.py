'''

Description:

Return all non-negative integers of length N such that the absolute difference between every two consecutive digits is K.

Note that every number in the answer must not have leading zeros except for the number 0 itself. For example, 01 has one leading zero and is invalid, but 0 is valid.

You may return the answer in any order.

 

Example 1:

Input: N = 3, K = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.



Example 2:

Input: N = 2, K = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
 

Note:

1 <= N <= 9
0 <= K <= 9

'''


from typing import List

class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:

        # -------------------------------------------------
        def dfs( N, K, cur_num):
            
            if N == 0:
                # it is of n digits now, add current number to result
                result.append( cur_num )
                return
            
            last_digit = cur_num % 10
            
            if last_digit + K < 10:
                
                # next digit = last digit + K
                next_num = 10 * cur_num + last_digit + K
                dfs( N-1, K, next_num)
            
            if last_digit - K >= 0 and K != 0:
                
                # next digit = last digit - K
                next_num = 10 * cur_num + last_digit - K
                dfs( N-1, K, next_num)
        # -------------------------------------------------        
        
        result = []
        
        if N == 1:
            # special handle for corner case with N = 1
            result.append( 0 )
        
        for digit in range(1, 10):
            dfs( N-1, K, cur_num=digit)
        
        return result



# n : the value of input N

## Time Complexity: O( 2^n )
#
# The overhead in time is the cost of DFS, which is of O( 2^n )

## Space Complexity: O( 2^Nn)
#
# The overhead in space is the storage for recursion call stack, which is of O( 2^n )



import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().numsSameConsecDiff( N=3, K=7 )
        self.assertCountEqual(result, [181,292,707,818,929])


    def test_case_2( self ):

        result = Solution().numsSameConsecDiff( N=2, K=1 )
        self.assertCountEqual(result, [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98])



if __name__ == '__main__':

    unittest.main()