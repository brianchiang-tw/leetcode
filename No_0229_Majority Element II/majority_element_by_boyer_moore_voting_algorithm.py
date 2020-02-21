'''

Description:

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:

Input: [3,2,3]
Output: [3]



Example 2:

Input: [1,1,1,3,3,2,2,2]
Output: [1,2]

'''



from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        # a list of majority elements
        majority = []
        
        # threshold for majority validation and verification
        threshold = len(nums) // 3
        
        # Record for possible majority candidates, at most two majority elements is allowed by math-proof.
        candidate = [0, 0]
        
        # Voting for majority candidates
        voting = [0, 0]
        
        ## Step_#1:
        # Find possible majority candidates
        for number in nums:
            
            if number == candidate[0]:
                # up vote to first candidate
                voting[0] += 1
                
            elif number == candidate[1]:
                # up vote to second candidate
                voting[1] += 1
            
            elif not voting[0]:
                # set first candidate
                candidate[0] = number
                voting[0] = 1
                
            elif not voting[1]:
                # set second candidate
                candidate[1] = number
                voting[1] = 1
                
            else:
                # down vote if mis-match
                voting[0] -= 1
                voting[1] -= 1
        
        
        ## Step_#2:
        # Validation:
        voting = [0, 0]
        
        for number in nums:
            
            if number == candidate[0]:
                # update up vote for first candidate
                voting[0] += 1
                
            elif number == candidate[1]:
                # update up vote for second candidate
                voting[1] += 1
        
        
        for i, vote in enumerate(voting):
            
            # Verify majority by threshold
            if vote > threshold:
                majority.append( candidate[i] )
            
            
        return majority
        
        

# n : the length of input array, nums.

## Time Complexity: O( n )
#
# The overhead in time is the for loop, iterating on nums, which is of ( n ),
# and the for loop, iterating on voting, which is of O( 2 ) = O( 1 )
#
# It takes O( n ) in total.


## Space Complexity: O( 1 )
#
# The overhead in space is the storage for majorirt, candidate, and voting, which are of O( 1 )



from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'sequence')
def test_bench():

    test_data = [
                    TestEntry( sequence = [3,2,3] ),
                    TestEntry( sequence = [1,1,1,3,3,2,2,2] ), 
                ]

    # expected output:
    '''
    [3]
    [1, 2]
    '''

    for t in test_data:

        print( Solution().majorityElement(t.sequence) )

    return



if __name__ == '__main__':

    test_bench()
