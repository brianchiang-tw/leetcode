'''

Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

Example 1:
Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
Note:

0 < nums.length <= 50000.
0 < nums[i] < 1000.
0 <= k < 10^6.

'''




from typing import List
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        if k <= 1:
            # Quick response for invalid k on product of positive numbers
            return 0
        
        else:
            left_sentry = 0

            num_of_subarray = 0
            product_of_subarry = 1

            # update right bound of sliding window
            for right_sentry in range( len(nums) ):

                product_of_subarry *= nums[right_sentry]

                # update left bound of sliding window
                while product_of_subarry >= k:
                    product_of_subarry //= nums[left_sentry]
                    left_sentry += 1

                # Note:
                # window size = right_sentry - left_sentry + 1

                # update number of subarrary with product < k
                num_of_subarray += right_sentry - left_sentry + 1

            return num_of_subarray



def test_bench():

    test_data = [
                    ([10, 5, 2, 6], 100),
                    ([10, 5, 2, 6, 7, 11, 8], 100),
                ]

    # expected output:
    '''
    8
    15
    '''
    
    for sequence, k in test_data:

        print( Solution().numSubarrayProductLessThanK(sequence, k ) )

    return 



if __name__ == '__main__':

    test_bench()