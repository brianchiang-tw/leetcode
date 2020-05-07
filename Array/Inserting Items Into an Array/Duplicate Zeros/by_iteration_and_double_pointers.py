'''

Description:

Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.

Do the above modifications to the input array in place, do not return anything from your function.

 

Example 1:

Input: [1,0,2,3,0,4,5,0]
Output: null
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
Example 2:

Input: [1,2,3]
Output: null
Explanation: After calling your function, the input array is modified to: [1,2,3]
 

Note:

1 <= arr.length <= 10000
0 <= arr[i] <= 9



Hint #1  

This is a great introductory problem for understanding and working with the concept of in-place operations. The problem statement clearly states that we are to modify the array in-place. That does not mean we cannot use another array. We just don't have to return anything.



Hint #2  

A better way to solve this would be without using additional space. The only reason the problem statement allows you to make modifications in place is that it hints at avoiding any additional memory.



Hint #3  

The main problem with not using additional memory is that we might override elements due to the zero duplication requirement of the problem statement. How do we get around that?


   Hide Hint #4  
If we had enough space available, we would be able to accommodate all the elements properly. The new length would be the original length of the array plus the number of zeros. Can we use this information somehow to solve the problem?

'''



from typing import List

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        
        size, zero_count = len( arr ), arr.count( 0 )
        
        if zero_count in ( 0, size):
            
            # Quick response for simple case
            return
        
        # -------------------------------------------------
        
        idx_update = size + zero_count - 1
        
        # make sure index is in valid range
        valid_index = lambda idx: idx < size
        
        for idx_origin in reversed( range(size) ):
            
            
            if 0 == zero_count:
                
                # All zero duplication is completed
                break
            
            if arr[ idx_origin ] != 0:
                
                if valid_index(idx_update):
                    arr[ idx_update ]  = arr[ idx_origin ] 
                
                idx_update -= 1
                
            else:
                
                zero_count -= 1
                
                if valid_index(idx_update):
                    arr[ idx_update ]  = arr[ idx_origin ] 
                    
                idx_update -= 1                    

                if valid_index(idx_update):
                    arr[ idx_update ]  = arr[ idx_origin ]

                idx_update -= 1                        



# n : the length of input list, nums

## Time Complexity: O( n )
#
# The overhead in time is the cost of linear scan, which is of O( n )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for loop index and temp variable, which is of O( 1 )

from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'sequence')

def test_bench():

    test_data = [
                    TestEntry( sequence = [1,0,2,3,0,4,5,0] ),
                    TestEntry( sequence = [1,2,3] ),
                ]

    # expected output:
    '''
    [1, 0, 0, 2, 3, 0, 0, 4]
    [1, 2, 3]
    '''

    for t in test_data:

        Solution().duplicateZeros( arr = t.sequence )
        print( t.sequence )

    return



if __name__ == '__main__' :

    test_bench()