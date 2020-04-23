'''

Description:

Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

'''



from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        size = len( nums )

        product_arr = [ 1 for _ in range(size) ]

        # update left-hand side product except self
        for i in range( 1, size):
            product_arr[i] = product_arr[i-1] * nums[i-1]

        # update right-hand side product excpet self
        right_product = 1

        for j in reversed( range( size ) ):
            product_arr[j] *= right_product
            right_product *= nums[j]

        return product_arr






# n : the length of input list, nums

## Time Complexity: O( 1 )
#
# The overhead in time is the for loop iterating on i and j, which are of O( n ).


## Space Complexity: O( n )
#
# The overhead in space is the storage for list, left_product as well as right_product, which are of O( n ).



def test_bench():

    test_data = [
                    [1,2,3,4],
                    [1,5,2,4,3],
                    [10,20,5,7,3,9,2,6,11]
                ]

    # expected output:
    '''
    [24, 12, 8, 6]
    [120, 24, 60, 30, 40]
    [2494800, 1247400, 4989600, 3564000, 8316000, 2772000, 12474000, 4158000, 2268000]
    '''

    for sequence in test_data:

        print( Solution().productExceptSelf(sequence) )
    
    return 



if __name__ == '__main__':

    test_bench()        
