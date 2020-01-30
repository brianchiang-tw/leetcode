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
        
        size = len(nums)
        
        product_left_to_right = nums
        
        product_right_to_left = nums[::-1]
        
        # update product of two kinds of subarray, one is extends from left to right, the other is from right to left
        for i in range(1, size):

            #print()
            
            # extends from left hand side, if meets 0 then restart in-place by itself.
            product_left_to_right[i] *= (product_left_to_right[i-1] or 1)
            #print( f'left to right: {product_left_to_right}')

            # extends from right hand sizde, if meets 0 then restart in-place by itself
            product_right_to_left[i] *= (product_right_to_left[i-1] or 1)
            #print( f'right to left: {product_right_to_left}')

        return max(max(product_left_to_right), max(product_right_to_left))


    

# n : the length of input list, nums.

## Time Complexity: O( n )
#
# The overhead in time is the for loop iterating on i, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for list, product_left_to_right as well as product_right_to_left, which is of O( 1 ).



def test_bench():

    test_data = [
                    [2,3,-2,4],
                    [-2,0,-1],
                    [-10,5,-3,7,0,6,-8,-9,21],
                    [0,2,3,4,0]
                ]

    # expected output:
    '''
    6
    0
    9072
    24
    '''

    for sequence in test_data:

        print( Solution().maxProduct(sequence) )
    
    return 



if __name__ == '__main__':

    test_bench()