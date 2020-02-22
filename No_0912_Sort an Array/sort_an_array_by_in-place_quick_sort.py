'''

Description:

Given an array of integers nums, sort the array in ascending order.

 

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
 

Constraints:

1 <= nums.length <= 50000
-50000 <= nums[i] <= 50000

'''



from typing import List
class Solution:
    
    def already_sorted( self, nums, left, right ) -> bool:
        
        return left == right or all( (nums[i] <= nums[i+1]) for i in range( left, right ) )
    
    
    
    def partition(self, nums: List[int], left: int, right: int) -> int:
    
        i = left - 1
        
        pivot = nums[right]
        
        for j in range(left, right):
            
            if nums[j] <= pivot:
                
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
                
        nums[i+1], nums[right] = pivot, nums[i+1]
        
        return (i+1)
    
    
    
    def quick_sort(self, nums: List[int], left: int, right: int) -> List[int]:
        
        # Divide and conquer
        
        if left < right :
        
            # Divide
            mid = self.partition( nums, left, right)
            
            # Conquer
            self.quick_sort( nums, left, mid-1)
            self.quick_sort( nums, mid+1, right)
            
        
            
    def sortArray(self, nums: List[int]) -> List[int]:
        
        self.quick_sort( nums, 0, len(nums)-1 )
        return nums



# n : the length of input list, nums.

## Time Complexity: O( n log n ) on average, O( n^2 ) on worst case.
#
# The time complexity is the same as QuickSort

## Space Complexity: O( n log n ) on average, O( n^2 ) on worst case.
# This version on list comprehension is out-of-place.
# The time complexity is the same as QuickSort



def test_bench():
    
    test_data = [35, 42, 17, 6, 18, 45, 26, 84, 60, 63, 4, 47, 76, 87, 83, 14, 21, 56, 90, 91, 72, 9, 20, 70, 100, 46, 78, 37, 98, 62, 99, 67, 29, 94, 74, 88, 53, 1, 93, 52, 10, 79, 2, 92, 86, 5, 40, 75, 95, 64, 38, 22, 59, 58, 31, 15, 7, 97, 73, 82, 57, 80, 36, 85, 34, 43, 49, 69, 33, 28, 96, 13, 55, 30, 23, 48, 32, 50, 65, 89, 54, 11, 16, 77, 61, 25, 44, 24, 41, 71, 81, 68, 
12, 51, 27, 8, 66, 19, 3, 39]

    # expected output:
    '''
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
    21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 
    41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 
    61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 
    81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
    '''
    Solution().quick_sort(test_data, 0 , len(test_data)-1 )
    print( test_data )

    return 



if __name__ == '__main__':

    test_bench()
