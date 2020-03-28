'''

Description:

Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.

'''



from typing import List
class Solution:
    
    
    def partition(self, nums, left, right):
        
        pivot = nums[left]
        l, r = left+1, right
        
        while l <= r:
            
            if nums[l] < pivot and nums[r] > pivot:
                
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l+1, r-1
            
            if nums[l] >= pivot:
                l += 1
            
            if nums[r] <= pivot:
                r -= 1
        
        
        nums[left], nums[r] = nums[r], nums[left]
        return r

    
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        size = len(nums)
        left, right = 0, size-1
        
        while True:
            
            cur_index = self.partition( nums, left, right)
            
            if cur_index > k-1:
                right = cur_index -1
                
            elif cur_index < k - 1:
                left = cur_index + 1
            
            else:
                return nums[ cur_index ]



# n : the length of input list, nums

## Time Complexity: O( n^2 )
#
# The overhead in time is the cost of partition, which is of O( n ) in average, O( n^2 ) in worst case

## Space Compleixty: O( 1 )
#
# The overhead in time is the loop index, which is of O( 1 )



from collections import namedtuple
TestEntry = namedtuple('TestEnry', 'sequence k')
def test_bench():

    test_data = [
                    TestEntry( sequence = [3,2,1,5,6,4], k = 2),
                    TestEntry( sequence = [3,2,3,1,2,4,5,5,6], k = 4),
                    TestEntry( sequence = [3,2,1,5,6,4], k = 1),
                    TestEntry( sequence = [3,2,1,5,6,4], k = 6),
                ]
    
    # expected output:
    '''
    5
    4
    6
    1
    '''

    for t in test_data:
        print( Solution().findKthLargest( nums = t.sequence, k =t.k) )

    return



if __name__ == '__main__':

    test_bench()