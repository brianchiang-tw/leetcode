'''

Description:

The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of the numbers in the set got duplicated to another number in the set, which results in repetition of one number and loss of another number.

Given an array nums representing the data status of this set after the error. Your task is to firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.

Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]


Note:
The given array size will in the range [2, 10000].
The given array's numbers won't have any order.

'''



from typing import List
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        # get the size of input array, nums
        n = len(nums)
        
        # perfect_sum 
        # = n * ( n+1 ) // 2
        # = sum of unique element + missing element
        perfect_sum = n * (n+1) // 2

        # compute the missing element from summation formula
        missing_element = perfect_sum - sum( set(nums) )

        # perfect sum + repeated element = sum of nums + missing element
        # compute the repeated element 
        repeated_element = sum(nums) + missing_element - perfect_sum

        return [ repeated_element, missing_element]



# n : the length of input sequence, nums.

## Time Complexity: O( n )
#
# The overhead in time is the cost of dictionary making, sum( set( nums) ), which are of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for dictionary and set(nums), which are of O( n )



def test_bench():

    test_data = [
                    [1,2,2,4],
                    [2,3,4,1,1],
                    [5,2,3,3,1]
                ]

    # expected output:
    '''
    [2, 3]
    [1, 5]
    [3, 4]    
    '''


    for sequence in test_data:

        print( Solution().findErrorNums(sequence) )
    
    return



if __name__ == '__main__':

    test_bench()