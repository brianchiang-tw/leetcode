'''

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

'''


from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        
        # a dictionary(hash)
        # key   : number
        # value : index
        num_idx_dict = dict()
            
        solution = []
        
        for idx, number in enumerate(nums):
            
            # compute the dual that makes value + dual = target
            dual = target - number
            
            # get the index of dual
            index_of_dual =  num_idx_dict.get( dual, None)
            
            if index_of_dual is not None and index_of_dual != idx:
                # Note: 
                # Descripion asks us not to use the same element twice
            
                # make a list to return solution list
                solution = [idx, index_of_dual]
                
                break

            else:
                # update key value pair ( number, idx) into dictionary
                num_idx_dict[ number ] = idx
                

        # return index of nums that makes the sum equal to target
        return solution






# n : the length of input array

## Time Complexity: O( n )
#
# The overhead in time is the for loop, iterating on nums, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for dictionary, number_dictionary, which is of O( n )
    
    

from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'array target')
def test_bench():

    test_data = [
                    TestEntry( array = [2, 7, 11, 15], target = 9),
                    TestEntry( array =[3, 4, 3, 1], target = 6),
                ]
    for t in test_data:

        print( Solution().twoSum( nums = t.array, target = t.target ) )

    return



if __name__ == "__main__":
    
    test_bench()    
