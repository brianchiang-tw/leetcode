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
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        # preprocessing, sort input list to keep increasing order
        nums.sort()

        # a container to store 4 sum quadruple
        solution = list()

        size_of_input = len( nums )

        # size_of_input - 3 is to aviod boundary crossing and reserve space for j, k, m
        for i in range( size_of_input - 3 ):

            # avoid element repetition
            if i > 0 and nums[i-1] == nums[i]:
                pass
                continue

            # size_of_input - 2 is to avoid boundary crossing and reseve space for k, m
            for j in range( i+1, size_of_input - 2):

                # avoid element repetition
                if j > i+1 and nums[j-1] == nums[j]:
                    pass
                    continue
                
                # k start from smallest value after j
                # m start from largest value after j
                k, m = (j+1), (size_of_input-1)

                while k < m:

                    quadruple = [ nums[i], nums[j], nums[k],nums[m] ]
                    four_sum = sum( quadruple )

                    if four_sum == target :

                        solution.append( quadruple )

                        # k move to the right
                        k += 1

                        # avoid element repetition
                        while k < m and nums[k-1] == nums[k]:
                            k += 1


                        # m move to the left
                        m -= 1

                        # avoid element repetition
                        while k < m and nums[m+1] == nums[m]:
                            m -= 1
                    
                    elif four_sum > target:

                        # four_sum is larger than target
                        # make the larger element become smaller by moving m to the left
                        m -= 1

                        # avoid element repetition
                        while k < m and nums[m+1] == nums[m]:
                            m -= 1

                    else:

                        # four_sum is smaller than target
                        # make the smaller element becomer bigger by moving k to the right
                        k += 1

                        # avoid element repetition
                        while k < m and nums[k-1] == nums[k]:
                            k += 1

        return solution


## Time Complexity
# O( N^3 )

# Preprocess of sorting input list takes O( N log N )

# Outer for loop takes O( N ) to iterate index i
# Also, inner for loop takes O( N ) to iterate index j
# Next, while loop takes O( N ) to iterate index k, m
# These three loops takes O( N^3 )


## Space Complexity
# O( 1 )

# Preprocess of sorting is in-place, O( 1 ), no need of extra space

# In the nested loop, we use variables for index i, j, k, m
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