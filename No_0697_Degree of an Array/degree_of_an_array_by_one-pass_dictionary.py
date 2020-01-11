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
        
        head_index = {}
        num_occ_dict ={}
        min_len_of_same_degree, max_degree = len(nums), 0
        
        
        for index, number in enumerate( nums):
        
            if number not in head_index:
                head_index[number] = index
            
            num_occ_dict[number] = num_occ_dict.get( number, 0 ) + 1
            
            if num_occ_dict[number] > max_degree:
                # update degree
                max_degree = num_occ_dict[number]
                
                # undate minimal length of degree
                min_len_of_same_degree = index - head_index[number] + 1 
            
            elif num_occ_dict[number] == max_degree:
                
                # update minimal length of degree
                min_len_of_same_degree = min( min_len_of_same_degree, index - head_index[number] + 1 )
        

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

