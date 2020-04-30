'''

Description:

Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]

Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.



Example 2:
Input: [0,1,0]

Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000.

'''



from typing import List
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        table = { 0: -1}

        prefix_sum = 0

        max_length = 0

        for idx, number in enumerate( nums ):

            if number == 1:
                prefix_sum += 1
            else:
                prefix_sum -= 1

            if prefix_sum in table:
                max_length = max( max_length, idx - table[prefix_sum] )
            
            else:
                table[prefix_sum] = idx

        return max_length






# n : the length of input list, nums

## Time Complexity: O( n )
#
# The overhead in time is the for loop, which is of O( n )

##Space Complexity: O( n )
#
# The overhead in space is the storage for dictionary, which is of O( n )



from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'sequence')

def test_bench():

    test_data = [
                    TestEntry( sequence = [0,1] ),
                    TestEntry( sequence = [0,1,0] ),
                    TestEntry( sequence = [0,1,0,1] ),
                    TestEntry( sequence = [0,0,1,1,0,1] ),
                ]        

    # expected output:
    '''

    2
    2
    4
    6
    '''

    for t in test_data:

        print( Solution().findMaxLength( nums = t.sequence) )

    return



if __name__ == '__main__':

    test_bench()    