'''

Description:


Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

'''



from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        size = len(nums)
        
        # helper array, record product of terms on the left hand side
        left_product = [ 1 for i in range(size) ]
        
        # helper array, record product of terms on the right hand side
        right_product = [ 1 for j in range(size) ]
        
        
        for i in range( 1, size ):
            left_product[i] = left_product[i-1] * nums[i-1]
            
        for j in range( size-2, -1, -1):
            right_product[j] = right_product[j+1] * nums[j+1]
            
        return [ left_product[k]*right_product[k] for k in range(size) ]



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

    for sequence in test_data:

        print( Solution().productExceptSelf(sequence) )
    
    return 



if __name__ == '__main__':

    test_bench()

