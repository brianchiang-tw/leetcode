'''

Description:

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

'''



class Solution:
    
    def subsets(self, nums):

        solution = []
        size = len(nums)
        
        def dfs_helper( grow_index, path, all_subset):

            all_subset.append( path )

            for i in range(grow_index, size):
                dfs_helper( i+1, path + [ nums[i] ], all_subset)
        # -----------------------------------------------------------------
        dfs_helper( grow_index = 0, path = [], all_subset = solution)
        return solution



# n : the length of input array, nums.

## Time Complexity: O( n * (2^n) )
#
# The overhead in time is the cost of subset generation, which is of O( n * (2^n) ).

## Space Complexity: O( 2^n )
#
# The overhead in space is the storage for output list, solution, which is of O( 2^n )



from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'elements')
def test_bench():

    test_data = [
                    TestEntry( elements = [] ),
                    TestEntry( elements = [ 1] ),
                    TestEntry( elements = [ 1, 2] ),
                    TestEntry( elements = [ 1, 2, 3] ),
                ]

    for t in test_data:

        print( Solution().subsets( nums = t.elements ) )

    return 



if __name__ == '__main__':

    test_bench()




'''

Demo 


Take nums = [1,2,3] for example.
Inital grow_index = 0, Path = [ ]

DFS( grow_index = 0, path = [ ] )
Append path **[ ]** to solution

→DFS( grow_index= 1, path = [ 1 ] )
Append path **[ 1 ]** to solution

→→DFS( grow_index = 2, path = [ 1, 2 ] )
Append path **[ 1, 2 ]** to solution

→→→DFS( grow_index = 3, path = [ 1, 2, 3 ] )
Append path **[ 1, 2, 3 ]** to solution

→→DFS( grow_index = 3, path = [ 1, 3 ] )
Append path **[ 1, 3 ]** to solution

→DFS( grow_index = 2, path = [ 2 ] )
Append path **[ 2 ]** to solution

→→DFS( grow_index = 3, path = [ 2, 3 ] )
Append path **[ 2, 3 ]** to solution

→DFS( grow_index = 3, path = [ 3 ] )
Append path **[ 3 ]** to solution

Completed.

All subsets = [ [ ], [ 1 ], [ 1, 2 ], [ 1, 2, 3 ], [ 1, 3 ], [ 2 ], [ 2, 3 ], [ 3 ] ]

'''