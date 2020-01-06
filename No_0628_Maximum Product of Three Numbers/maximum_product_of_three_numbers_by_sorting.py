'''

Description:

Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:

Input: [1,2,3]
Output: 6
 

Example 2:

Input: [1,2,3,4]
Output: 24
 

Note:

The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.

'''



from typing import List
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:

        # sort the nums with ascending order        
        nums.sort()
        
        # for possible solution_#1: First three largest positive numbers
        candidate_1 = nums[-1] * nums[-2] * nums[-3]

        # for possible solution_#2: First two smallest negative numbers, whit one largest positive number.
        candidate_2 = nums[-1]*nums[0]*nums[1]

        max_product = max( candidate_1, candidate_2)
        
        return max_product



# n : the length of input array, nums.

## Time Complexity: O( n log n)
#
# The major overhead in time is the sorting, which is of O( n log n )

## Space Complexity: O( 1 )
#
# The major overhead in space is the storage for number product, which is of O( 1 )


def test_bench():

    test_data = [
                    [1,2,3],
                    [-10,-9,0,1,2,3],
                    [-10,-9,-8,11]
                ]

    # expected output:
    '''
    6
    270
    990
    '''


    
    for arr in test_data :

        print( Solution().maximumProduct(arr) )

    return 



if __name__ == '__main__':

    test_bench()

