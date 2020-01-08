'''

Description:

Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

Example 1:
Input: [1,4,3,2]

Output: 4
Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).
Note:
n is a positive integer, which is in the range of [1, 10000].
All the integers in the array will be in the range of [-10000, 10000].


'''


from typing import List
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        
        # Main idea: 
        #
        # Preprocess nums by sorting with ascending order
        #
        # Denote pair as (x,y) 
        # Make the min number x pair with closest one, y, which is larger than itself a liitle bit
        # in order to keep large numbers stand out as much as possible
        
        max_sum_of_min_pair = sum( [ x for x in sorted(nums)[::+2] ] )
            
        return max_sum_of_min_pair
            


# n : the length of input array, nums.

## Time Complexity: O( n log n ) on average, O( n^2 ) on worst case
#
# The overhead in time is the sorting on nums, which is O( n log n ) on average, O( n^2 ) on worst case.


## Space Complexity: O( n )
#
# The nums.sort() is out-of-palce, no need of extra space allocation, of O( n ).
# And another cost in space is looping index and summation variable, which is of O( 1 ).



def test_bench():

    test_data = [
                    [1,4,3,2],
                    [-100, 1, -99, 5],
                    [-100, 5, 3, 1]
                ]

    # expected output:
    '''
    4
    -99
    -97
    '''


    for sequence in test_data:

        print( Solution().arrayPairSum(sequence) )
    
    return 



if __name__ == '__main__':

    test_bench()