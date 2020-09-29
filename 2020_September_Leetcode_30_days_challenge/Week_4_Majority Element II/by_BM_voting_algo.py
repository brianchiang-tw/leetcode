'''

Description:

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Follow-up: Could you solve the problem in linear time and in O(1) space?

 

Example 1:

Input: nums = [3,2,3]
Output: [3]



Example 2:

Input: nums = [1]
Output: [1]



Example 3:

Input: nums = [1,2]
Output: [1,2]
 

Constraints:

1 <= nums.length <= 5 * 104
-109 <= nums[i] <= 109

'''



from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        # a list of majority elements
        majority = []
        
        # threshold for majority validation and verification
        threshold = len(nums) // 3
        
        # Record for possible majority candidates, at most two majority elements is allowed by math-proof.
        candidate = [0, 0]
        
        # Voting for majority candidates
        voting = [0, 0]
        
        ## Step_#1:
        # Find possible majority candidates
        for number in nums:
            
            if number == candidate[0]:
                # up vote to first candidate
                voting[0] += 1
                
            elif number == candidate[1]:
                # up vote to second candidate
                voting[1] += 1
            
            elif not voting[0]:
                # set first candidate
                candidate[0] = number
                voting[0] = 1
                
            elif not voting[1]:
                # set second candidate
                candidate[1] = number
                voting[1] = 1
                
            else:
                # down vote if mis-match
                voting[0] -= 1
                voting[1] -= 1
        
        
        ## Step_#2:
        # Validation:
        voting = [0, 0]
        
        for number in nums:
            
            if number == candidate[0]:
                # update up vote for first candidate
                voting[0] += 1
                
            elif number == candidate[1]:
                # update up vote for second candidate
                voting[1] += 1
        
        
        for i, vote in enumerate(voting):
            
            # Verify majority by threshold
            if vote > threshold:
                majority.append( candidate[i] )
            
            
        return majority



# n : the length of input nums

## Time Complexity: O( n )
#
# The overhead in time is the cost of for-loop iteration, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for loop index and temporary variable, which are of O( 1 )


import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().majorityElement( nums = [3,2,3] )
        self.assertEqual(result, [3])


    def test_case_2( self ):

        result = Solution().majorityElement( nums = [1] )
        self.assertEqual(result, [1])


    def test_case_3( self ):

        result = Solution().majorityElement( nums = [1,2] )
        self.assertEqual(result, [1,2])



if __name__ == '__main__':

    unittest.main()