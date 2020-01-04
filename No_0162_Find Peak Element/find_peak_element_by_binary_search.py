'''

A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5 
Explanation: Your function can return either index number 1 where the peak element is 2, 
             or index number 5 where the peak element is 6.
Note:

Your solution should be in logarithmic complexity.

'''



from typing import List
class Solution:
    
    
    def helper(self, nums, left, right):
    
        if left == right:
            # base case:
            return left
        
        mid = ( left + right ) // 2
        
        if nums[mid] > nums[mid+1]:
            return self.helper(nums, left, mid)
        else:
            return self.helper(nums, mid+1, right)
        
    def findPeakElement(self, nums: List[int]) -> int:
        
        return self.helper( nums, 0 , len(nums)-1)



# n : the length of input nums

## Time Complexity: O( log n )
#
# The overhead in time is the cost of binary search, which is of O( log n )

## Space Complexity: O( log n)
#
# The overhead in space is to maintain call stack for recursion on binary search, which is of O( log n)



def test_bench():

    test_data = [
                    [1,2,3,1],
                    [1,2,1,3,5,6,4],
                    [1]
                ]

    # expected output:
    '''
    2
    5
    0
    '''


    for test_sequence in test_data:

        print( Solution().findPeakElement(test_sequence) )

    return 



if __name__ == '__main__':

    test_bench()