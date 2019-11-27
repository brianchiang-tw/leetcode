'''

Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

'''

class Solution:
    def threeSumClosest(self, nums, target: int) -> int:

        # preprocess, sort nums to keep nums in increasing order
        nums.sort()

        # a container to store solution of three sum
        three_sum_closet_solution = None

        # i loop from 0 to len(nums)-2
        # -2 is to avoid boundary corssing, and spare space for index j, k
        for i in range( len(nums)-2 ):
            
            if i > 0 and nums[i] == nums[i-1]:
                # skip element repetition
                pass 
                continue
            
            # j start from the smallest element after i
            # k start from the largest element after i
            j, k = i+1, len(nums)-1

            
            # j is index for second element
            # k is index for third element
            while j < k :
                

                # update three_sum on current iteration
                three_sum = nums[i] + nums[j] + nums[k]

                diff = three_sum - target         

                if three_sum_closet_solution == None:
                    # first-time
                    three_sum_closet_solution = three_sum

                else:
                    # non first-time

                    # calculate the difference
                    prev_diff = three_sum_closet_solution - target
                                
                    # update the nearest one
                    if abs(diff) < abs(prev_diff):
                        three_sum_closet_solution = three_sum
                        

                if( diff == 0 ):
                    
                    # diff = 0, perfect match with target
                    # direct return optional three_sum
                    three_sum_closet_solution = three_sum

                    return three_sum_closet_solution
                
                elif diff > 0:
                    
                    # three_sum is too big, let the largest element become smaller
                    k -= 1



                else:
                    # three_sum is too small, let the smallest element become bigger
                    j += 1

        return three_sum_closet_solution



## Time Complexity
# O( N^2 )

# Preprocess of sorting input list takes O( N log N )

# Outer for loop takes O( N ) to iterate index i
# Also, inner while loop takes O( N ) to iterate index j, k
# These two loops takes O( N^2 )


## Space Complexity
# O( 1 )

# Preprocess of sorting is in-place, O( 1 ), no need of extra space

# In the nested loop, we use variables for index i, j, k,
# and a list to store the solution
# These usage are of O( 1 )


def test_bench():

    test_data = [
                    ( [0 , 0, 0], 1),
                    ( [-1, 2, 1, -4], 1)
                ]

    for test in test_data:

        three_sum_closet = Solution().threeSumClosest( nums = test[0], target = test[1] )

        print( three_sum_closet )

# expected output:
'''
0
2

Explaination:
closet three sum = 0 = 0 + 0 + 0 for target = 1
clsoet three sum = 2 = -1 + 1 + 2 for target = 1
'''





if __name__ == "__main__":

    test_bench()