'''

Description:

Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.

Example 1:

Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
 

Note:

1 <= k <= n <= 30,000.
Elements of the given array will be in the range [-10,000, 10,000].
 

'''



from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        # Concept:
        # MaxAverage is equivelent to ( MaxPartialSum/k )
        
        # MaxPartialSum is equivalnet to nums[0:k] + Max( sliding gain )
        # MaxPartialSum 
        # = nums[0:k] + Max( sliding gain )

        
        
        
        max_sliding_gain = 0
        sliding_gain = 0
        
        for i in range(0, len(nums)-k ):
            
            sliding_gain += nums[i+k]-nums[i]
            
            # update maximum sliding gain
            max_sliding_gain = max( max_sliding_gain,  sliding_gain )
            
            
        return ( sum( nums[0:k] ) + max_sliding_gain) / k



# n : the length of input list, nums.

## Time Complexity: O( n )
#
# The overhead in time is the for loop iterating on i, which is of O( n ).

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for looping index, and sliding gain, which is of O( n ).



def test_bench():

    test_data = [
                    ([1,12,-5,-6,50,3], 4),
                    ([1,12,-5,-6,50,3], 3),
                    ([1,100,-50,70,-20,-90,80,110,120,-10, 5], 4)
                ]

    # expected output:
    '''
    12.75
    15.666666666666666
    75.0
    '''

    for sequence, k in test_data:

        print( Solution().findMaxAverage(sequence, k) )
    
    return 



if __name__ == '__main__':

    test_bench()