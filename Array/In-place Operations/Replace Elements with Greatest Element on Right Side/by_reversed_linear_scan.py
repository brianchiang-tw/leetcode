'''

Description:

Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.

 

Example 1:

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
 

Constraints:

1 <= arr.length <= 10^4
1 <= arr[i] <= 10^5



Hint #1  

Loop through the array starting from the end.



Hint #2  

Keep the maximum value seen so far.

'''



from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        
        size = len(arr)
        right_hand_max = -1
        
        for i in range( size-1, -1, -1):
    
            arr[i], right_hand_max = right_hand_max, max( right_hand_max, arr[i])
        
        return arr



# n : the length of input list, arr

## Time Complexity: O( n )
#
# The overhead in time is the cost of reversed linaer scan, which is of O( n ).

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for loop index and temporary variable, which is of O( 1 ).


from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'sequence')

def test_bench():

    test_data = [
                    TestEntry( sequence = [17,18,5,4,6,1] ),
                    TestEntry( sequence = [10,7,9,5,8,2] ),
                ]
    
    # expected output:
    '''
    [18, 6, 6, 6, 1, -1]
    [9, 9, 8, 8, 2, -1]
    '''

    for t in test_data:
        
        Solution().replaceElements( arr = t.sequence)
        print( t.sequence )
    
    return



if __name__ == '__main__':

    test_bench()
