
from typing import List
class Solution:
    
    def partition(self, arr, left, right):
        
        pivot = arr[right]
        
        i = left-1
        
        for j in range(left, right):
            
            if arr[j] > pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i+1], arr[right] = pivot, arr[i+1]
        return i+1
    
    def quick_select(self, arr, left, right, k):
        
        if left <= right:
            
            mid = self.partition( arr, left, right )
            
            if mid > k-1:
                return self.quick_select( arr, left, mid-1, k)
            elif mid < k-1:
                return self.quick_select( arr, mid+1, right, k)
            else:
                return arr[mid]
            
            
            
    def thirdMax(self, nums: List[int]) -> int:
        
        unique_nums = list(set(nums))
        
        #print( unique_nums )
        
        size = len(unique_nums)
        
        if size == 1:
            return unique_nums[0]
        
        if size == 2:
            if unique_nums[0] > unique_nums[1]:
                return unique_nums[0] 
            else:
                return unique_nums[1]
            
        return self.quick_select(unique_nums, 0, size-1, 3)
            





# n : the size of input list, nums.

## Time Complexity: O( n )
#
# The overhead in time is the heapify() and the while loop iterating on nums, which are of O( n ).

## Space Complexity: O( 1 )
#
# The overhead in space is the record of maximal value, which is of O( 1 ).




def test_bench():

    test_data = [
                    [3, 2, 1],
                    [1, 2],
                    [100],
                    [100,99,99],
                    [100,98,97],
                    [100,99,99,98],
                    [100,99,99,98,97]
                ]

    # expected output:
    '''
    1
    2
    100
    100
    97
    98
    98
    '''


    for sequence in test_data:
        print( Solution().thirdMax(sequence) )

    return 



if __name__ == '__main__':

    test_bench()