'''

Desription:

Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.



Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]



Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]

'''


from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        
        src = [ *range(1, 10) ]
        
        result = []
        
        # ---------------------------------------
        
        def dfs( cur, idx, target):
            
            if target < 0:
                
                # base case
                # target < 0, no solution
                return
            
            
            elif target == 0 and len(cur) == k:
                
                # base case
                # satisy the requirement with k distinct numbers
                result.append( cur[::] )
                
                return
            
            # general case
            for j in range(idx, len(src)):
                
                # solve in dfs
                cur.append( src[j] )
                dfs( cur, j+1, target-src[j] )
                cur.pop()
            
            return
        
        # ---------------------------------------
        
        dfs(cur=[], idx=0, target=n)
        return result



# k : the value of input parameter k

## Time Complexity: O( C(9, k) )
#
# The overhead in time is the cost of combination C(9, k)

## Space Complexity: O( k )
#
# The overhead in space is the storage for recursion call stack, which is of O( k )


import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().combinationSum3( k = 3, n = 7 )
        self.assertCountEqual( result, [[1,2,4]] )


    def test_case_2( self ):

        result = Solution().combinationSum3( k = 3, n = 9 )
        self.assertCountEqual( result, [[1,2,6], [1,3,5], [2,3,4]] )


if __name__ == '__main__':

    unittest.main()        