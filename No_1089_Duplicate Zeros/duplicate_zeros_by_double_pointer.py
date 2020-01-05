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

'''



'''
Python in-place O( 1 ) space, O( n ) time with double pointers.

Hint:

1. Quick respones on special cases.
2. Maintain a zero counter, and a pair of double pointers.
3. Carry out zero-copy from tail to head.
4. Once all zero-copies are completed, early return to avoid redundant iterations.
'''



from typing import List
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        
        size, zero_counter = len(arr), arr.count(0)

        if zero_counter == 0 or zero_counter == size:
            # Quick response on special case
            return
            
        
        dummy_length = size + zero_counter
        
        in_boundary = lambda j: j<size
        
        
        j = dummy_length-1
        for i in range( size-1, -1, -1):
            
            if zero_counter == 0:
                # all zero-copy is completed
                break
            
            
            if arr[i] != 0:
                
                if in_boundary(j):
                    arr[j] = arr[i]
                    
            else:
                
                # update zero counter
                zero_counter -= 1
                
                if in_boundary(j):
                    arr[j] = 0
                    
                j -= 1
                
                if in_boundary(j):
                    arr[j] = 0
            
            j -= 1
        
        return



# n : the length of input array, arr.

## Time Complexity: O( n )
#
# The overhead in time is the for loop iterating on i, which is of O( n )

## Space Complexity: O( 1 )
#
# The overhead in space is looping variable and double pointers, which is of O( 1 )



def test_bench():

    test_data = [
                    [1,0,2,3,0,4,5,0],
                    [1,2,3],
                    [1,0,0,0,0,0,0,2],
                    [0,0,0,0,0,0,0,0]
                ]

    for sequence in test_data:

        Solution().duplicateZeros( sequence )
        print( sequence ) 

    return 



if __name__ == '__main__':

    test_bench()