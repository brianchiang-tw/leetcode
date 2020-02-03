'''

Description:

Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3



Example 2:

Input: [3,4,-1,1]
Output: 2



Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.

'''



from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        
        index, size = 0, len(nums)
        
        # main idea:
        # keep all positive numbers in nums with in-place hash, 
        # such that A[i] = i+1, i from 0 to (size-1)
        while index < size:
            
            # check postive numbers in range
            if nums[index] != index+1 and \
                nums[index] > 0 and nums[index] <= size and \
                nums[index] != nums[ nums[index]-1 ]:
                
                # swap nums[index] and nums[ nums[index]-1 ]
                temp = nums[ nums[index]-1]
                nums[ nums[index]-1] = nums[index]
                nums[index] = temp
                
                
            else:
                index += 1
                
                
        # scan for missing possitive
        for i in range(size):
            
            if nums[i] != i+1:
                return (i+1)
        
        # corner case handle for empty list, or list with numbers in order
        return size+1



# n : the length of input array, nums.

## Time Complexity: O( n )
#
# The overhead is the while loop iterating on index, and for loop iterating on i,
# which are of O( n ).


## Space Complexity: O( 1 )
#
# The overhead in storage is the aux space for element swap, which is of O( 1 ).




def test_bench():

    test_data = [
                    [1,2,0],
                    [3,4,-1,1],
                    [7,8,9,11,12]
                ]

    # expected output:
    '''
    3
    2
    1
    '''


    for sequence in test_data:

        print( Solution().firstMissingPositive(sequence) )
    
    return 



if __name__ == '__main__':

    test_bench()