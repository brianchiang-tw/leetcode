'''

Description:

Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.

'''



from typing import List
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        
        size = len(nums)
            
        local_max, local_min = nums[0], nums[-1]

        start, end = -1, -2

        for i in range(1, size):

            local_max = max( local_max, nums[i] )
            local_min = min( local_min, nums[size-1-i])

            if local_max > nums[i]:
                # nums[i] < nums[i-1]
                # find mismatch of ascending order
                end = i

            if local_min < nums[size-1-i]:
                # nums[size-1-i] > nums[size-i]
                # find mismatch of ascending order
                start = size-1-i

        return end-start+1



# n : the length of input list, nums.

## Time Complexity: O( n )
#
# The overhead in time is the for loop iteratong on i, which is of O( 1 ).

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for looping variable and pivot, which is of O( 1 ).


def test_bench():

    test_data = [
                    [2, 6, 4, 8, 10, 9, 15]
                ]

    for sequence in test_data:

        print( Solution().findUnsortedSubarray(sequence) )
    
    return 



if __name__ == '__main__':

    test_bench()