'''

Description:

Given the array nums, obtain a subsequence of the array whose sum of elements is strictly greater than the sum of the non included elements in such subsequence. 

If there are multiple solutions, return the subsequence with minimum size and if there still exist multiple solutions, return the subsequence with the maximum total sum of all its elements. A subsequence of an array can be obtained by erasing some (possibly zero) elements from the array. 

Note that the solution with the given constraints is guaranteed to be unique. Also return the answer sorted in non-increasing order.

 

Example 1:

Input: nums = [4,3,10,9,8]
Output: [10,9] 
Explanation: The subsequences [10,9] and [10,8] are minimal such that the sum of their elements is strictly greater than the sum of elements not included, however, the subsequence [10,9] has the maximum total sum of its elements. 



Example 2:

Input: nums = [4,4,7,6,7]
Output: [7,7,6] 
Explanation: The subsequence [7,7] has the sum of its elements equal to 14 which is not strictly greater than the sum of elements not included (14 = 4 + 4 + 6). Therefore, the subsequence [7,6,7] is the minimal satisfying the conditions. Note the subsequence has to returned in non-decreasing order.  



Example 3:

Input: nums = [6]
Output: [6]
 

Constraints:

1 <= nums.length <= 500
1 <= nums[i] <= 100

'''


from typing import List
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        
        # make nums sorted in descending order
        nums.sort( reverse = True )
        
        summation = sum( nums )
        
        sequence, partial_sum = [], 0
        
        # pick number from largest one, until partial sum is larger than (summation / 2)
        for number in nums:
            
            partial_sum += number
            sequence.append( number )
            
            if partial_sum > summation / 2:
                break
                
        return sequence



# n : the length of input list, nums.

## Time Complexity: O( n log n )
#
# The overhead in time is the cost of sorting, which is of O( n log n )

## Space Complexity: O( n )
#
# The overhead in space is the storaoge for output list, sequence, which is of O( n )



from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'sequence')
def test_bench():

    test_data = [
                    TestEntry( sequence = [4,3,10,9,8] ),
                    TestEntry( sequence = [4,4,7,6,7] ),
                    TestEntry( sequence = [6] ),
                    TestEntry( sequence = [5,4,1,3,2] ),
                    TestEntry( sequence = [1,3,2,4,5] ),
                ]

    # expected output:
    '''
    [10, 9]
    [7, 7, 6]
    [6]
    [5, 4]
    [5, 4]
    '''

    for t in test_data:

        print( Solution().minSubsequence( nums = t.sequence) )
    
    return



if __name__ == '__main__':

    test_bench()