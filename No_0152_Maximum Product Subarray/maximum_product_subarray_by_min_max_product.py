'''

Description:

Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

'''



from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        cur_min, cur_max = nums[0], nums[0]
        
        max_product_ever = nums[0]
        
        # check each element nums[i], and subarray ends in index i
        for i in range(1,len(nums) ):
            
            prev_min, prev_max = cur_min, cur_max
            
            # get currenct array element
            cur_num = nums[i]
            
            # update current min
            cur_min = min( cur_num, min( prev_min * cur_num, prev_max * cur_num) )
            
            # update current max
            cur_max = max( cur_num, max( prev_min * cur_num, prev_max * cur_num) )
            
            # update maximum product of subarray
            max_product_ever = max( max_product_ever, cur_max )
            
            
        return max_product_ever



# n : the length of input list, nums.

## Time Complexity: O( n )
#
# The overhead in time is the for loop iterating on i, which is of O( n )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for looping variable and min/max variable, which is of O( 1 ).



def test_bench():

    test_data = [
                    [2,3,-2,4],
                    [-2,0,-1],
                    [-10,5,-3,7,0,6,-8,-9,21]
                ]

    # expected output:
    '''
    6
    0
    9072
    '''

    for sequence in test_data:

        print( Solution().maxProduct(sequence) )
    
    return 



if __name__ == '__main__':

    test_bench()