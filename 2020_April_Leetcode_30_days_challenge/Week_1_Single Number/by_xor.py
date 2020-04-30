'''

Description:

Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1



Example 2:

Input: [4,1,2,1,2]
Output: 4


'''



from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        x = 0
        for number in nums:
            x ^= number
            
        return x



# n : the length of input list, nums.

## Time Complexity: O( n )
#
# The overhead in time is the for loop, which is of O( n ).

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for loop index and temporary variable for XOR, which are of O( 1 )



from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'sequence')
def test_bench():

    test_data = [
                    TestEntry( sequence = [2,2,1] ),
                    TestEntry( sequence = [4,1,2,1,2] ),
                    TestEntry( sequence = [1,1,3,2,3,5,4,4,5] ),
                ]

    # expected output:
    '''
    1
    4
    2
    '''

    for t in test_data:

        print( Solution().singleNumber( nums = t.sequence) )
    
    return



if __name__ == '__main__':

    test_bench()