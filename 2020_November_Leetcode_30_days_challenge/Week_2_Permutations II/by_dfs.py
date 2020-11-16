'''

Description:

Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

 

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]


 
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10

'''


from typing import List
from collections import defaultdict

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        # preprocessing, make nums sorted in ascending order
        nums.sort()
        
        # full length of nums
        size = len(nums)
        
        # record of all unique permutations
        result = []
        
        # visit flag of index j
        visited = defaultdict(lambda:False)
        
        # -------------------------------------------
        
        def dfs( cur, count):
            
            if count == size:
                
                ## Base case aka stop condition
                # count meet the full length, current permutation is accomplished
                result.append( cur[::] )
                return
            
            else:
                
                ## General case:
                
                # Make permutation with different index j
                
                for j in range(0, size):
                    
                    if (j > 0) and not visited[j-1] and (nums[j] == nums[j-1]):
                        # skip this turn due to repeated element
                        continue
                        
                    if visited[j]:
                        # skip this turn because j has been visited
                        continue
                    
                    # occupy j as visited        
                    visited[j] = True

                    # append current element into permutation
                    cur.append( nums[j] )

                    # make next level permutation with DFS
                    dfs( cur, count+1)

                    # pop current element from permutation
                    cur.pop()
                    
                    # release j as not visited
                    visited[j] = False

        # -------------------------------------------
        
        dfs(cur=[], count=0)
        return result


# n : the length of nums

## Time Complexity: O( n! )
#
# The overhead in time is the cost of permutation generation, which is of O( n! )

## Space Complexity: O( n! )
#
# The overhead in space is the stroage for all permuation, which is of O( n! )


import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().permuteUnique( nums=[1,1,2] )
        self.assertCountEqual(result, [[1,1,2],[1,2,1],[2,1,1]] )


    def test_case_2( self ):

        result = Solution().permuteUnique( nums=[1,2,3] )
        self.assertCountEqual(result, [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]] )


if __name__ == '__main__':

    unittest.main()        