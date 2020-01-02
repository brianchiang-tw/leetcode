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
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        
        # permutations return all possible permutations over a iterable object
        return list( map( list, permutations( nums ) ) )



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