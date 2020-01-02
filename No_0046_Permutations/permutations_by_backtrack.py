'''

Description:

Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

'''


from itertools import permutations
from typing import List

class Solution:
    
    def permute( self, nums ):

        # base case
        if len( nums ) == 0:
            return []

        # base case
        if len( nums ) == 1:
            return [ nums ]

        # Inductive step

        all_permutation = []

        for i in range( len(nums) ):

            for other in self.permute( nums[:i] + nums[ i+1: ] ):
                all_permutation.append( [ nums[i] ] + other )
                
        return all_permutation

    '''
    def permute(self, num):

        if len(num) == 0: return []
        if len(num) == 1: return [num]
        res = []

        for i in range(len(num)):

            for j in self.permute(num[:i] + num[i+1:]):
                res.append( [num[i]] + j )

        return res
    '''


# n : the number of elements of input list

## Time Complexity: O( n! )
#
# The overhead in time is proportional to the number of outcomes, which is of O( n! )

## Space Complexity: O( n! )
#
# The overhead in space is proportional to the number of outcomes, which is of O( n! )




def test_bench():

    test_data = [1,2,3]

    print( Solution().permute(test_data) )

    return



if __name__ == '__main__':

    test_bench()