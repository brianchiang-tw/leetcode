'''

Description:

Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements. 

Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

a, b are from arr
a < b
b - a equals to the minimum absolute difference of any two elements in arr
 

Example 1:

Input: arr = [4,2,1,3]
Output: [[1,2],[2,3],[3,4]]
Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.
Example 2:

Input: arr = [1,3,6,10,15]
Output: [[1,3]]
Example 3:

Input: arr = [3,8,-10,23,19,-4,-14,27]
Output: [[-14,-10],[19,23],[23,27]]
 

Constraints:

2 <= arr.length <= 10^5
-10^6 <= arr[i] <= 10^6

'''



from typing import List
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        
        size = len(arr)
        if size == 2:
            # Quick response for array size = 2
            return [ [min(arr), max(arr)] ]
        
        # pre-processing sorting
        arr.sort()
        
        # storage for min-abs-diff pairs
        list_of_pairs = []
        
        min_abs_diff = 2 * 10**6 + 1
        
        # visit each pair
        for i in range(size-1):
            cur_abs_diff = abs( arr[i] - arr[i+1] )
            
            if cur_abs_diff <= min_abs_diff:
                
                if cur_abs_diff < min_abs_diff:
                    # update minimum absolute difference
                    min_abs_diff = cur_abs_diff

                    # discard old list
                    list_of_pairs.clear()

                
                # append current pair to list
                list_of_pairs.append( [ arr[i], arr[i+1] ] )

                
        return list_of_pairs



# n : the length of input list, arr.

## Time Complexity: O( n )
#
# The overhead in time is the for loop iterating on i, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for list_of_pairs, which is of O( n )


def test_bench():

    test_data = [
                    [4,2,1,3],
                    [1,3,6,10,15],
                    [3,8,-10,23,19,-4,-14,27]
                ]

    # expected output:
    '''
    [[1, 2], [2, 3], [3, 4]]
    [[1, 3]]
    [[-14, -10], [19, 23], [23, 27]]
    '''

    for sequence in test_data:

        print( Solution().minimumAbsDifference(sequence) ) 
    
    return 



if __name__ == '__main__':

    test_bench()