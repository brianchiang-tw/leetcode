'''

Description:

Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

Example 1:
Input: [4,2,3]
Output: True
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
Example 2:
Input: [4,2,1]
Output: False
Explanation: You can't get a non-decreasing array by modify at most one element.
Note: The n belongs to [1, 10,000].

'''

# allow python feature: type hint
from typing import List

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        
        
        # Corner case handling
        if len(nums) == 0 or len(nums) == 1:
            return True
        
        
        inversion_count = 0
        
        size_of_nums = len( nums )
        
        # sacn each element, and compare to neighbor
        for i in range( size_of_nums - 1 ):
            
            if nums[i] > nums[i+1]:
                
                if inversion_count >= 1:
                    return False
                
                inversion_count += 1
                
                # adjust to keep non-decreasing order
                if (i-1) < 0 or nums[i-1] <= nums[i+1] :
                    nums[i] = nums[i+1]
                else:
                    nums[i+1] = nums[i]
            
                    
        
        if inversion_count <= 1:
            return True
        else:
            return False
                    


def test_bench():

    test_data = [
                    [4, 2, 3],
                    [4, 2, 1],
                    [],
                    [1],
                    [3,2,1,6]
                ]

    # expected output:
    '''
    True
    False
    True
    True
    False
    '''


    for test in test_data:
        is_non_decreasing = Solution().checkPossibility( test )

        print( is_non_decreasing )

    return



if __name__ == '__main__':

    test_bench()