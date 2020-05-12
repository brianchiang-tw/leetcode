'''

Description:

You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

 

Example 1:

Input: [1,1,2,3,3,4,4,8,8]
Output: 2



Example 2:

Input: [3,3,7,7,10,11,11]
Output: 10
 

Note: Your solution should run in O(log n) time and O(1) space.

'''



from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        size = len(nums)
        
        left, right = 0, size // 2
        
        while left < right:
            
            pair_index = left + ( right - left ) // 2
            
            if nums[2*pair_index] != nums[2*pair_index+1]:
                # If current pair is mis-matched
                # then go left-half to find the first pair of mis-match
                right = pair_index
            
            else:
                # If current pair is with the same number appeared twice
                # then go right-half to find the first pair of mis-match
                left = pair_index + 1
        
        # when the while loop terminates, left = right = the first pair index of mis-match
        return nums[2*right]



# n : the length of input list, nums

## Time Complexity: O( log n )
#
# The overhead in time is the cost of binary search, which is of O( log n ).

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for two-pointers and temporary variable, which is of O( 1 ).


from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'sequence')


def test_bench():

    test_data = [
                    TestEntry( sequence = [1,1,2,3,3,4,4,8,8] ),
                    TestEntry( sequence = [3,3,7,7,10,11,11] ),
                    TestEntry( sequence = [1,1,2,2,3,3,5,6,6] ),
                ]        

    # expected output:
    '''
    2
    10
    5
    '''

    for t in test_data:

        print( Solution().singleNonDuplicate( nums = t.sequence ) )
    
    return



if __name__ == '__main__':

    test_bench()