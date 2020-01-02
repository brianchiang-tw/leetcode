'''

Description:

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

'''


class Solution:
    def threeSum( self, nums ) :
        
        # get the length of input list: nums
        length = len(nums)

        # sort input numbers, to keep the increasing order
        nums.sort()

        # container for 3 sum answer storage
        triplet_answer = list()

        # length - 2 is for the valid index i, j ,k within boundary
        # i = index for the first element such that 3 sum = nums[i] + nums[j] + nums[k] = 0
        for i in range(0, length - 2 ):
            
            # skip the repetition of the same element (the limitation of problem description)
            if i > 0 and ( nums[i-1] == nums[i] ):
                pass
                continue
            
            # j :   index for the second element such that 3 sum = nums[i] + nums[j] + nums[k] = 0
            #       start from smallest value after index i

            # k : index for the third  element such that 3 sum = nums[i] + nums[j] + nums[k] = 0
            #       start from largest value after index i
            j , k = i + 1, length -1


            # inner loop to iterate index j, k
            while j < k :

                three_sum = nums[i] + nums[j] + nums[k]

                # check index i, j , k meets the sum value = 0 or not
                if three_sum == 0:

                    # get one triplet satisfy requirement, append to triplet_answer
                    triplet_answer.append( [ nums[i], nums[j], nums[k] ] )

                    # update index j, k for next iteration
                    j += 1
                    k -= 1
                    
                    # skip the repetition of the same element
                    while j < k and ( nums[j] == nums[j-1] ):
                        j += 1

                    # skip the repetition of the same element
                    while j < k and ( nums[k] == nums[k+1] ):
                        k -= 1

                elif three_sum < 0:
                    # sum value is too small, make the second element larger on next iteration
                    # update index j
                    j += 1

                else:
                    # sum value is too big, make the third element smaller on next iteration
                    # update index k
                    k -= 1

        # return the container for 3 sum triplet
        return triplet_answer


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

    test_input = [-1, 0, 1, 2, -1, -4]

    answer_of_three_sum = Solution().threeSum( test_input )
    # expected output:
    '''
    [[-1, -1, 2], [-1, 0, 1]]

    Explanation:
    0 = -1 + -1 + 2
    0 = -1 + 0 + 1
    '''


    print( answer_of_three_sum )



if __name__ == "__main__":

    test_bench()