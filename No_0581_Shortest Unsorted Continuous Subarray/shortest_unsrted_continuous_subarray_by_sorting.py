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
        
        already_ascending = all( [ nums[i] <= nums[i+1] for i in range(size-1) ] )
        
        if already_ascending:
            return 0
        
        else:
            well_order = sorted(nums)

            first_mismatch, last_mismatch = 0, 0
            for i in range( size-1 ):
                if nums[i] != well_order[i]:
                    first_mismatch = i
                    break


            for j in range( size-1, -1, -1):
                if nums[j] != well_order[j]:
                    last_mismatch = j
                    break


            return last_mismatch - first_mismatch + 1



# n : the length of input list, nums.

## Time Complexity: O( n log n ) on average, and O( n ^ 2) on worst.
#
# The overhead in time is the same as the sorting, which is of O( n log n ) on average, and O( n ^ 2) on worst.

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