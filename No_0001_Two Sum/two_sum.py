'''
Description:

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

'''



class Solution:
    def twoSum(self, nums , target) :
        
        
        # a dictionary(hash)
        # key is number
        # value is index of list: nums
        number_dictionary = dict()
        
        for index, number in enumerate(nums):
            
            # put every number into dictionary with index
            number_dictionary[ number ] = index
            
        # a list for index storage for i, index_of_dual that nums[i] + nums[index_of_dual] = target
        solution = list()
        
        for i in range( len(nums) ):
            
            value = nums[i]
            
            # compute the dual that makes value + dual = target
            dual = target - value
            
            index_of_dual =  number_dictionary.get( dual, None)

            if index_of_dual is not None and index_of_dual != i:
                # Note: we can't use the same element twice, thus return empty list
            
                # make a list for solution list
                solution = list([i, index_of_dual])
                
                break

            else:
                # if index_of_dual is None, keeps going to next iteration
                # Problem description says that each input would have exactly one solution
                continue
                

        # return index of nums that makes the sum equal to target
        return solution

    
    
if __name__ == "__main__":
    
    test_bench = Solution() 

    # test case 1
    nums = [2, 7, 11, 15]
    target = 9

    # expected output:
    '''
    [0, 1]
    '''

    result = test_bench.twoSum( nums, target )
    print( result )



    # test case 2
    nums = [3, 3]
    target = 6

    # expected output:
    '''
    [0, 1]
    '''

    result = test_bench.twoSum( nums, target )
    print( result )