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
        
        # create a list for output
        product_excluding_self = [ 1 for i in range(size) ]

        
        # Step_#1
        # record product of terms on the left hand side
        
        for i in range( 1, size ):
            product_excluding_self[i] = product_excluding_self[i-1] * nums[i-1]
        
        
        
        # Step_#2
        # Update array elements as the product of ( product of left hand side ) * ( produt of right hand side )
        
        product_of_right_hand_side = 1
        for j in reversed( range( size) ):
            product_excluding_self[j] *= product_of_right_hand_side
            product_of_right_hand_side *= nums[j]
            
            
        return product_excluding_self



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

