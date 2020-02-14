'''

Description:

Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into sets of k consecutive numbers
Return True if its possible otherwise return False.

 

Example 1:

Input: nums = [1,2,3,3,4,4,5,6], k = 4
Output: true
Explanation: Array can be divided into [1,2,3,4] and [3,4,5,6].
Example 2:

Input: nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3
Output: true
Explanation: Array can be divided into [1,2,3] , [2,3,4] , [3,4,5] and [9,10,11].
Example 3:

Input: nums = [3,3,2,2,1,1], k = 3
Output: true
Example 4:

Input: nums = [1,2,3,4], k = 3
Output: false
Explanation: Each array should be divided in subarrays of size 3.
 

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
1 <= k <= nums.length

'''



from collections import Counter
from typing import List
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        
        if len(nums)%k != 0:
            # Quick response:
            # Reject because it is impossible to make sets
            return False
        
        if k == 1:
            # Quick response:
            # Accept with trivial solution by making set with each single element itself
            return True
        
        
        # Make number sorted in ascending order
        nums.sort()
        
        # dictionary:
        # key   : number
        # value : occurrence
        num_occ_dict = Counter( nums )
        
        
        # Make consecutive sets of size k from the smallest element
        for n in nums:
            
            occ_for_partition = num_occ_dict[n]
            
            if occ_for_partition == 0:
                continue
                
                
            for i in range(k):
                
                if num_occ_dict[n+i] < occ_for_partition:
                    # Reject:
                    # Either number (n+i) doesn't exist, or
                    # occurrence of (n+i) is not enough to make consecutive sets with k
                    return False
                
                # after making sets, update occurrence
                num_occ_dict[n+i] -= occ_for_partition
                
        return True



# n : the number of elements in nums
# k : the number of unique elements in nums

## Time Complexity: O( n )
#
# The overhead in time is the cost of Timsort, which is of O( n log n).


## Space Complexity: O( k )
#
# The overhead in space is the storage for dictionary, num_occ_dict, which is of O( k ).



def test_bench():

    test_data = [
                    ( [1,2,3,3,4,4,5,6], 4),
                    ( [3,2,1,2,3,4,3,4,5,9,10,11], 3),
                    ( [3,3,2,2,1,1], 3),
                    ( [1,2,3,4],3)
                ]

    for sequence, k in test_data:

        print( Solution().isPossibleDivide(sequence, k) )
    
    return 



if __name__ == '__main__':

    test_bench()