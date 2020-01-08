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
        
        bucket = [0] * 20001
        
        for x in nums:
            bucket[ x + 10000 ] +=1
        
        
        toggle = True
        max_sum_of_min_pair = 0
        i = 0
        while i < 20001:
            if bucket[i] > 0:
                
                
                if toggle:
                    max_sum_of_min_pair += (i-10000)
                    bucket[i] -= 1
                    toggle = False
                else:
                    bucket[i] -= 1
                    toggle = True
                    
            else:      
                i += 1
                    


        return max_sum_of_min_pair
            
            

# n : the length of input array, nums.

## Time Complexity: O( n ).
#
# The overhead in time is the variation of bucket sort, which is O( n ).


## Space Complexity: O( n )
#
# The overhead in space is the bucket array for bucket sorting ,which is of O( n ).



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