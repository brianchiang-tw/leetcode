'''

Description:

Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.

 

Example 1:

Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation: 
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1). 
For nums[3]=2 there exist one smaller number than it (1). 
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).



Example 2:

Input: nums = [6,5,4,8]
Output: [2,1,0,3]



Example 3:

Input: nums = [7,7,7,7]
Output: [0,0,0,0]
 

Constraints:

2 <= nums.length <= 500
0 <= nums[i] <= 100

'''



from typing import List
from collections import Counter

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        num_occ_dict, accumlation = Counter(nums), 0
        
        for unique_num in sorted(num_occ_dict):
            
            # update histogram of the number of smaller numbers
            num_occ_dict[unique_num], accumlation = accumlation, num_occ_dict[unique_num]+accumlation
        
        # output by list comprehension
        return [ num_occ_dict[number] for number in nums]



# n : the length of input array, nums
# k : the number of unique elements in input array, k <= n always

## Time Complexity: O( n + k log k)
#
# The overhead in time is the for loop, iterating on num_occ_dict, which is of O( k ), and
# the cost of sorting on num_occ_dict, which is of O( k log k), and
# the cost of output in list comprehension, which is of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the storage for num_occ_dict, which is of O( k ), and 
# the storage for output list comprehesion, which is of O( n ).



from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'sequence')
def test_bench():

    test_data = [
                    TestEntry( sequence = [8,1,2,2,3] ),
                    TestEntry( sequence = [6,5,4,8] ),
                    TestEntry( sequence = [7,7,7,7] )
                ]

    # expected output:
    '''
    [4, 0, 1, 1, 3]
    [2, 1, 0, 3]
    [0, 0, 0, 0]
    '''

    for t in test_data:

        print( Solution().smallerNumbersThanCurrent( nums = t.sequence ) ) 

    return



if __name__ == '__main__':

    test_bench()