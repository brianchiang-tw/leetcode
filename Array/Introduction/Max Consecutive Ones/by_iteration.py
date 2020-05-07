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


Hint #1  

You need to think about two things as far as any window is concerned. One is the starting point for the window. How do you detect that a new window of 1s has started? The next part is detecting the ending point for this window. How do you detect the ending point for an existing window? If you figure these two things out, you will be able to detect the windows of consecutive ones. All that remains afterward is to find the longest such window and return the size.

'''



from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        
        max_ones_length = 0
        cur_ones_length = 0
        
        for x in nums:
            
            if x == 1:
                # current number is one
                
                # increase consecutive ones length by 1
                cur_ones_length += 1
                
            else:
                
                # update max consecutive ones length
                max_ones_length = max( max_ones_length, cur_ones_length )

                # current number is zero
                cur_ones_length = 0            
        
        return max_ones_length



# n : the length of input array, nums

## Time Complexity: O( n )
#
# The overhead in time is the cost of linear scan, which is of O( n ).

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for loop index and temporary variable, which is of O( 1 ).


from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'sequence')

def test_bench():

    test_data = [
                    TestEntry( sequence = [1,1,0,1,1,1] ),
                    TestEntry( sequence = [1,0,1,1,1,1] ),
                    TestEntry( sequence = [1,0,1,1,0,1] ),
                ]        


    # expected output:
    '''
    2
    1
    2
    '''

    for t in test_data:

        print( Solution().findMaxConsecutiveOnes( nums = t.sequence) )
    
    return



if __name__ == '__main__':

    test_bench()    