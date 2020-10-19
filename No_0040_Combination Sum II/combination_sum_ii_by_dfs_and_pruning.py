'''

Description:

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.



Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]



Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]

'''


from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        # keep candidates in ascending order
        candidates.sort()
        
        # record of valid combination
        result = []
        
        def combination_find( target, start, end, path):
            
             
            if target == 0:
                # combination sum meets target
                # update current valid combination
                result.append( path )
                return 
            
            for i in range(start, end+1):     
                           
                if i > start and candidates[i] == candidates[i-1]:
                    # avoid repetition
                    continue
                    
                current = candidates[i]
                
                if current > target:
                    # pruning:
                    # current minimal element is larger than target
                    # impossible to find valid combination
                    break
                
                # update target in next round as remaining
                remaining = target - current
                
                # DFS search, update start index as i+1 and move forward
                combination_find(remaining, i+1, end, path + [ current ] )
        
        # DFS search
        combination_find( target, 0, len(candidates)-1, [] )
        return result


# n : the length of candidates

## Time Complexity: O( n * 2^n )
#
# The overhead in time is the cost of element seleciton, which is of O( n * 2^n )

## Space Complexity: O( 2^n )
#
# The overhead in space is the storage for result, which is of O( 2^n )

import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().combinationSum2( candidates = [10,1,2,7,6,1,5], target = 8)
        self.assertCountEqual(result, [[1, 7],[1, 2, 5],[2, 6],[1, 1, 6]] )


    def test_case_2( self ):

        result = Solution().combinationSum2( candidates = [2,5,2,1,2], target = 5 )
        self.assertCountEqual(result, [[1,2,2],[5]] )


if __name__ == '__main__':

    unittest.main()