'''

Description:

Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6
Note:

nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.

'''



from collections import Counter
from typing import List
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        
        num_occ_dict = Counter( nums )
        
        max_occ = max( list( num_occ_dict.values() ) )
        
        num_start_end_dict = dict()
        
        
        # update (start, end) index for each number
        for index, x in enumerate(nums):
            
            if x not in num_start_end_dict:
                # update start index, and initialize end index for number x
                num_start_end_dict[x] = [ index, index]
            else:
                # update end index for number x
                start_index = num_start_end_dict[x][0]
                num_start_end_dict[x] = [ start_index, index]
                
        
        
        min_len_of_same_degree = len( nums )
        
		# compute minimal length of subarray with degree max_occ
        for num, occ in num_occ_dict.items():
            
            if occ == max_occ:
                
                end_index = num_start_end_dict[num][1]
                start_index = num_start_end_dict[num][0]
                
                # update minimal length of subarray with degree max_occ
                min_len_of_same_degree = min( min_len_of_same_degree, end_index - start_index + 1)
                
        

        return min_len_of_same_degree



# n : the length of input nums:

## Time Complexity: O( n )
#
# The overhead in time is the for loop iterating on (index, number), which is of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the storage for dictionary, head_index as well as num_occ_dict, which is of O( n ).



def test_bench():

    test_data = [
                    [1, 2, 2, 3, 1],
                    [1, 2, 2, 3, 1, 4, 2]
                ]
    
    # expected output:
    '''
    2
    6
    '''


    for sequence in test_data:

        print( Solution().findShortestSubArray(sequence) )

    return 



if __name__ == '__main__':

    test_bench()

