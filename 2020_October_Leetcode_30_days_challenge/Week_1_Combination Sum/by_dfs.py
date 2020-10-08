'''

Description:

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.



Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]



Example 3:

Input: candidates = [2], target = 1
Output: []



Example 4:

Input: candidates = [1], target = 1
Output: [[1]]



Example 5:

Input: candidates = [1], target = 2
Output: [[1,1]]
 

Constraints:

1 <= candidates.length <= 30
1 <= candidates[i] <= 200
All elements of candidates are distinct.
1 <= target <= 500

'''


from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        
        minimum = candidates[0]
        
        result = []
        
        # ----------------------------------------------------------------
        def dfs( target, start, end, pick):
            
            if target == 0:
                
                result.append( pick[::] )
                return
            
            for i in range(start,end+1):
                
                cur = candidates[i]
                
                remain = target - cur
                
                if cur > target:
                    # impossible to meet target, cur is too large
                    break
                    
                if remain and remain < minimum:
                    # impossible to meet target for cur, remain is to small
                    continue
                
                dfs( target=remain, start=i, end=end, pick=pick+[cur])
        # ----------------------------------------------------------------
        
        dfs( target=target, start=0, end=len(candidates)-1, pick=[] )
        return result



# n : the length of candidates
# t : the value of target

## Time Complexity: O( n * 2^n )
#
# The overhead in time is the cost of element picking, which is of O( n * 2^n )

## Space Complexity: O( t )
#
# The overhead in space is the storage for recursion call stack, which is of O( t ).


import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().combinationSum( candidates=[2,3,6,7], target=7 )
        self.assertEqual(result, [[2,2,3],[7]] )
    
    
    def test_case_2( self ):

        result = Solution().combinationSum( candidates = [2], target = 1 )
        self.assertEqual(result, [] )


    def test_case_3( self ):

        result = Solution().combinationSum( candidates = [2,3,5], target = 8 )
        self.assertEqual(result, [[2,2,2,2],[2,3,3],[3,5]] )


    def test_case_4( self ):

        result = Solution().combinationSum( candidates = [1], target = 1 )
        self.assertEqual(result, [[1]] )


    def test_case_5( self ):

        result = Solution().combinationSum( candidates = [1], target = 2 )
        self.assertEqual(result, [[1,1]] )


if __name__ == '__main__':

    unittest.main()        