''''

Description:

You are given a sorted unique integer array nums.

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
 

Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"



Example 2:

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"



Example 3:

Input: nums = []
Output: []



Example 4:

Input: nums = [-1]
Output: ["-1"]



Example 5:

Input: nums = [0]
Output: ["0"]
 

Constraints:

0 <= nums.length <= 20
-231 <= nums[i] <= 231 - 1
All the values of nums are unique.
nums is sorted in ascending order.

'''


from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        ranges = []
        
        for number in nums:
            
            # add one new interval
            if not ranges or number > ranges[-1][-1] + 1:
                ranges += [],
            
            # update interval endpoint value
            ranges[-1][1:] = number, 
            
        # generate output
        return [ '->'.join( map(str, interval)) for interval in ranges]
                


# n: the length of nums

## Time Complexity: O( n )
#
# The overhead in time is the cost of iteration, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for intervals, which is of O( n )


import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().summaryRanges( nums=[0,1,2,4,5,7] )
        self.assertEqual(result, ["0->2","4->5","7"])

    
    def test_case_2( self ):

        result = Solution().summaryRanges( nums=[0,2,3,4,6,8,9] )
        self.assertEqual(result, ["0","2->4","6","8->9"])

    
    def test_case_3( self ):

        result = Solution().summaryRanges( nums=[] )
        self.assertEqual(result, [])


    def test_case_4( self ):

        result = Solution().summaryRanges( nums=[-1] )
        self.assertEqual(result, ["-1"])        



if __name__ == '__main__':

    unittest.main()        