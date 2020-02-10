'''

Description:

Given an array consists of non-negative integers, your task is to count the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.



Example 1:

Input: [2,2,3,4]

Output: 3
Explanation:
Valid combinations are: 
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3
Note:
The length of the given array won't exceed 1000.
The integers in the given array are in the range of [0, 1000].

'''



from typing import List
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        
        # sort in-place
        # keep numbers in ascending order
        nums.sort()
        
        # counter for valid triplet to make triangle
        valid_triplet = 0
        
        for index_i in range( len(nums)-1, 1, -1):
            
            third_edge = nums[index_i]
            
            index_of_first_edge, index_of_second_edge = 0, index_i - 1
            
            while index_of_first_edge < index_of_second_edge:
                
                first_edge = nums[index_of_first_edge]
                second_edge = nums[index_of_second_edge]
                
                if first_edge + second_edge > third_edge:
                    
                    # valid triplets
                    # first_edge    : from nums[index_of_first_edge] to nums[(index_of_second_edge-1)]
                    # second edge   : nums[index_of_second_edge]
                    # third edge    : nums[index_i]
                    valid_triplet += ( index_of_second_edge - index_of_first_edge )
        
                    # second edge large enough
                    # make it smaller and try next run
                    index_of_second_edge -= 1
                else:
                    # first edge is too small
                    # make it larger and try next run
                    index_of_first_edge += 1
        
        
        
        return valid_triplet



# n : the length of input array, nums.

## Time Complexity: O( n^2 )
#
# The overhead in time includs the cost of timsort of O( n log n ), and
# the cost of nested loops composed of outer for loop and inner while loop, of O( n ^ 2).
#
# It takes O( n^2 ) in total.

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for loop index, sliding window, and counter, which is of O( 1 ).



def test_bench():

    test_data = [ 
                    [2,2,3,4],
                    [4,3,2,2],
                    [3,3,4,5,6,6,7,8,10,9]
                ] 


    # expected output:
    '''
    3
    3
    86
    '''

    for sequence in test_data:

        print( Solution().triangleNumber(sequence))

    return



if __name__ == '__main__':

    test_bench()