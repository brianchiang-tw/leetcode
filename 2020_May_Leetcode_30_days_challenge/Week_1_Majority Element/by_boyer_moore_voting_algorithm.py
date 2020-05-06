'''

Description:

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3



Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2

'''



from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        majority = None
        vote = 0
        
        for number in nums:
            
            if vote == 0:
                # Either starting or vote just go back to zero
                # assign current number as majority
                majority = number
                vote = 1
            
            elif majority == number:
                # current number is majority, add 1 to vote
                vote += 1
            
            else:
                # current numbr is not majority, substract 1 from vote
                vote -= 1
                
        return majority



# n : the length of input List

## Time Complexity: O( n )
#
# The overhead in time is the cost of linear scan, which is of O( n ).

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for vote and majority, which is of O( 1 ).

from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'vote_sequence')
def test_bench():

    test_data = [
                    TestEntry( vote_sequence= [3,2,3] ),
                    TestEntry( vote_sequence= [2,2,1,1,1,2,2] ),
                ]        

    # expected output:
    '''
    3
    2
    '''

    for t in test_data:

        print( Solution().majorityElement( nums = t.vote_sequence) )
    
    return



if __name__ == '__main__':

    test_bench()    