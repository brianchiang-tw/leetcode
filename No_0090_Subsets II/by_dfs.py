'''

Description:

Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

'''


from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        
        # ------------------------
        
        def dfs(start, end, cur):
            
            result.append( cur[::] )
            
            for i in range(start, end+1):
                
                if i > start and nums[i] == nums[i-1]:
                    # skip duplicate subset
                    continue
                
                # select current number
                cur.append( nums[i] )
                
                # keep making subset in DFS
                dfs(start=i+1, end=end, cur=cur)
                
                # undo selection
                cur.pop()
        
        # --------------------------
        
        # keep nums in sorted with ascending order
        nums.sort()
        
        dfs( start=0, end=len(nums)-1, cur=[] )
        return result


# n : the length of nums

## Time Complexity: O( n * (2 ^ n) )
#
# The overhead in time is the cost of dfs, which is of O( n * (2 ^ n) )

## Space Complexity: O( 2 ^ n )
#
# The overhead in space is the storage for output, which is of O( 2 ^ n )


import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().subsetsWithDup( nums=[1,2,2] )
        self.assertCountEqual(result, [
                                        [2],
                                        [1],
                                        [1,2,2],
                                        [2,2],
                                        [1,2],
                                        []
                                    ]
                            )



if __name__ == '__main__':

    unittest.main()