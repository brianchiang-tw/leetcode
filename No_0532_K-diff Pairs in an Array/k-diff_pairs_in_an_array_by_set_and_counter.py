'''

Description:

Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute difference is k.

Example 1:
Input: [3, 1, 4, 1, 5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.
Example 2:
Input:[1, 2, 3, 4, 5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
Example 3:
Input: [1, 3, 1, 5, 4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).
Note:
The pairs (i, j) and (j, i) count as the same pair.
The length of the array won't exceed 10,000.
All the integers in the given input belong to the range: [-1e7, 1e7].

'''


from collections import Counter
from typing import List
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
        
        if k < 0 or len(nums) == 0:
            # Qucik response if k < 0
            # absolute value must be >= 0, conflicts with k
            
            # Quick response if nums is empty list
            # impossible to find k-pair
            return 0
        
        
        
        # dictionary
        # key   : number
        # value : occurrence
        num_occ_dict = Counter(nums)
        
        # set
        # with unique element in nums
        set_of_k_pair = set()
        
        # check each unique element in nums
        for x in set(nums):
            
            # check x+k exists or not to make k-pair
            if (x+k) in num_occ_dict:
                
                if k != 0:
                    # x and x+k makes one k-pair
                    set_of_k_pair.add( (x, x+k) )
                    
                elif num_occ_dict[x+k] != 1:
                    # 0-pair requires x repeated at least 2 times
                    set_of_k_pair.add( (x, x+k) )
                
        return len(set_of_k_pair)



# n : the length of input list, nums.

## Time Complexity: O( n )
#
# The overhead in time is the for loop iterating on x, which is of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the storage for set_of_k_pair as well as set(nums), which is of O( n ).



def test_bench():

    test_data = [
                    ([3, 1, 4, 1, 5], 2),
                    ([1, 2, 3, 4, 5], 1),
                    ([1, 3, 1, 5, 4], 0)
                ]

    # expected output:
    '''
    2
    4
    1
    '''


    for sequence, k in test_data:

        print( Solution().findPairs(sequence, k) )

    return 



if __name__ == '__main__':

    test_bench()