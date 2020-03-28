'''

Description:

Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.

'''



from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        nums.sort( reverse = True )
        
        return nums[k-1]






# n : the length of input list, nums

## Time Complexity: O( n log n )
#
# The overhead in time is the cost of timsort in python, which is of O( n log n).

## Space Compleixty: O( 1 )
#
# The overhead in time is the loop index, which is of O( 1 )



from collections import namedtuple
TestEntry = namedtuple('TestEnry', 'sequence k')
def test_bench():

    test_data = [
                    TestEntry( sequence = [3,2,1,5,6,4], k = 2),
                    TestEntry( sequence = [3,2,3,1,2,4,5,5,6], k = 4),
                    TestEntry( sequence = [3,2,1,5,6,4], k = 1),
                    TestEntry( sequence = [3,2,1,5,6,4], k = 6),
                ]
    
    # expected output:
    '''
    5
    4
    6
    1
    '''

    for t in test_data:
        print( Solution().findKthLargest( nums = t.sequence, k =t.k) )

    return



if __name__ == '__main__':

    test_bench()