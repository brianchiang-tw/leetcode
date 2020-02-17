'''

Description:

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.

'''



from typing import List
class NumArray:

    def __init__(self, nums: List[int]):
        
        self.size = len(nums)
        
        if self.size:
            # build prefix sum table when input nums is valid
            self.prefix_sum = [ 0 for _ in range(self.size) ]

            self.prefix_sum[0] = nums[0]
            
            # prefix_Sum[k] = nums[0] + ... + nums[k]
            # prefix_Sum[k] = prefix_Sum[k-1] + nums[k]
            for k in range(1,self.size):
                self.prefix_sum[k] = self.prefix_sum[k-1] + nums[k]
        

    def sumRange(self, i: int, j: int) -> int:
        
        # reject query with invalid index
        if self.size == 0 or i < 0 or i > j or j >= self.size:
            return 0
        
        # lookup table from prefix_Sum
        if i == 0:
            return self.prefix_sum[j]
        else:
            return self.prefix_sum[j]-self.prefix_sum[i-1]
        
        
        
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)



# n : the length of input array, nums.

## Time Complexity: O( n ) for initialization, O( 1 ) for sumRange() query
# 
# For initialization:
# The overhead in time is the for loop, iterating on nums, which is of O( n ).
#
# For query:
# The overhead in time is the table lookup, which is of O( 1 ).

## Space Complexity: O( n ) for initialization, O(1) for sumRange() query.
#
# For initialization:
# The overhead in space is the storage for table, self.prefix_sum, which is of O( n ).
#
# For query:
# The overhead in space is the buffer for output, which is of O( 1 ).



def test_bench():

    test_data = [
                    ([-2, 0, 3, -5, 2, -1], [(0,2), (2,5), (0,5)]),
                    ([ 3,-8, 7, 11,-6, 10], [(0,3), (1,4), (3,5)])
                ]


    # expected output:
    '''
    1
    -1
    -3

    13
    4
    15   

    '''

    for sequence, list_of_queries in test_data:
        
        obj = NumArray( nums = sequence )

        for query_index in list_of_queries:

            print( obj.sumRange( *query_index ) )

        print()
    return



if __name__ == '__main__':

    test_bench()