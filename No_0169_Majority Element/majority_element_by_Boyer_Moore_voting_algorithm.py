'''

Descption:

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
        
        majority_candidate = 0
        candidate_voting = 0
        
        
        # Find majority by Boyer-Moore majority vote algorithm
        for number in nums:
            
            if not candidate_voting:
                # Setup candidate if voting is zero
                majority_candidate = number
                candidate_voting = 1
                
            else:
                if number == majority_candidate:
                    # Accumulate voting if match
                    candidate_voting += 1
                else:
                    # Decrease by 1 if mis-match
                    candidate_voting -= 1
                    
        return majority_candidate



# n : the length of input array nums

## Time Complexity: O( n )
#
# The overhead in time is the loop, iterating on input array, nums, which is of O( n ).

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for majority_candidate and candidate_voting, which is of O( 1 ).



from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'sequence')
def test_bench():

    test_data = [
                    TestEntry( sequence = [3,2,3]),
                    TestEntry( sequence = [2,2,1,1,1,2,2]),
                ]

    # expected output:
    '''
    3
    2
    '''

    for t in test_data:

        print( Solution().majorityElement(t.sequence) )

    return 



if __name__ == '__main__':

    test_bench()