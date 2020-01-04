'''

Description:

Given an array of 4 digits, return the largest 24 hour time that can be made.

The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has elapsed since midnight.

Return the answer as a string of length 5.  If no valid time can be made, return an empty string.

 

Example 1:

Input: [1,2,3,4]
Output: "23:41"
Example 2:

Input: [5,5,5,5]
Output: ""
 

Note:

A.length == 4
0 <= A[i] <= 9

'''


from typing import List
from itertools import permutations

class Solution:
    
    def to_24_time( self, hr, min):
        
        return '{0:02d}'.format( hr ) + ':' + '{0:02d}'.format( min )
    


    def largestTimeFromDigits(self, A: List[int]) -> str:
        
        hr = -1
        min = -1
        

        # try-and-judge strategy
        for p in permutations(A):
            
            hr_trial = 10*p[0] + p[1]
            min_trial = 10*p[2] + p[3]
            
            
            if 23 >= hr_trial >= 0 and 59 >= min_trial >= 0:
                
                if hr_trial > hr or ( hr_trial == hr and min_trial > min ):
                    hr = hr_trial
                    min = min_trial
        
        if hr == -1:
            return ""
        else:
            return self.to_24_time(hr, min)


# n : the length of input digits, always = 4, defined by description.

## Time Complexity : O( 4! ) = O( 1 )
#
# The time cost of try-and-judge strategy is O( 4! ) = O( 1 )
# Note: n = 4 is defined by problem description.


## Space Complexity : O( 4! ) = O( 1 )
#
# The overhead in space is the storage for different trial, which is of O( 4! ) = O( 1 )



def test_bench():

    test_data = [
                    [1,2,3,4],
                    [5,5,5,5],
                    [2,0,6,6]
                ]

    # expected output:
    # Note: the second output for test case is empty string ""
    '''
    23:41

    06:26
    '''


    for test_digits in test_data:

        print(Solution().largestTimeFromDigits(test_digits) )

    return 



if __name__ == '__main__':

    test_bench()