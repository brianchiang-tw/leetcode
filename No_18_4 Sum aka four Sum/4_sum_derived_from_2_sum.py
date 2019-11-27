'''

Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums 
such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

'''


# allow python featre, type hints
from typing import List

class Solution:

    def no_repeated_index(self, tuple_1, tuple_2):

        for e in tuple_1:
            if e in tuple_2:
                return False

        return True



    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        # a container to store solution to four sum
        solution = list()

        # a hasing to store key, value pair
        # key is s
        # value is num1 and num2 tuple, where num1 + num2 = s
        value_hash = dict()

        size_of_input = len(nums)

        # -1 is to avoid boundary crossing and reserve space for index j
        for i in range( size_of_input - 1 ):
            for j in range( i+1, size_of_input ):

                two_sum = nums[i] + nums[j] 
                two_sum_tuple = (i, j)

                dual_value = target - two_sum
                dual_tuple_set = value_hash.get( dual_value, None )

                if dual_tuple_set is not None:
                    
                    for dual_tuple in dual_tuple_set:
                        d_0 = nums[dual_tuple[0]]
                        d_1 = nums[dual_tuple[1]]
                        quadruple = sorted( [ d_0, d_1, nums[i], nums[j] ] )

                        if self.no_repeated_index(two_sum_tuple, dual_tuple) and quadruple not in solution:
                            solution.append( quadruple )


                if two_sum not in value_hash:
                    value_hash[ two_sum ] = set()        

                else:
                    pass

                    
                value_hash[ two_sum ].add( two_sum_tuple )


        return solution


## Time Complexity
# O( N^2 )

# Preprocess of sorting input list takes O( N log N )

# Outer for loop takes O( N ) to iterate index i
# Also, inner for loop takes O( N ) to iterate index j

## Space Complexity
# O( 1 )

# Preprocess of sorting is in-place, O( 1 ), no need of extra space

# In the nested loop, we use variables for index i, j, tuple, two sum
# and a list to store the solution
# These usage are of O( 1 )



def test_bench():

    test_data = [
                ( [1, 0, -1, 0, -2, 2], 0),
                ( [1, 0, -1, 0, -2, 2], 1)
            ]

    for test in test_data:

        three_sum_closet = Solution().fourSum( nums = test[0], target = test[1] )

        print( three_sum_closet )

    return

# expected output:
'''

[[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
[[-2, 0, 1, 2], [-1, 0, 0, 2]]

'''



if __name__ == '__main__':

    test_bench()