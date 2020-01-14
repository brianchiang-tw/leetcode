'''

Description:

Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000

'''



from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        prev_num = 0
        max_ones_length = 0
        cur_ones_length = 0
        
        for x in nums:
            
            if x == 1:
                # current number is one
                
                if x == prev_num:
                    # consecutive ones, increase ones length by 1
                    cur_ones_length += 1
                    
                else:
                    # not consecutive ones, reset ones length to 1
                    cur_ones_length = 1
                
                # update max consecutive ones length
                max_ones_length = max( max_ones_length, cur_ones_length )
                
            else:
                # current number is zero
                cur_ones_length = 0
            
            # update previous number
            prev_num = x
            
        
        return max_ones_length



# n : the length of input list, nums.

## Time Complexity: O( n )
#
# The overhead in time is the for loop iterating on x, which is of O( n ).

## Space Complexity: O( 1 )
#
# The overhead in storage is the storage for ones' length counter, which is of O( 1 ).



def test_bench():

    test_data = [
                    [1,1,0,1,1,1],
                    [1,0,1,0,1,1],
                    [1,1,0,1,1,1],
                    [1,1,1,1,1,0],
                    [1,1,1,1,1,1]
                ]

    # expected output:
    '''
    3
    2
    3
    5
    6
    '''

    for sequence in test_data:
        print( Solution().findMaxConsecutiveOnes(sequence) )
    
    return 



if __name__ == '__main__':

    test_bench()