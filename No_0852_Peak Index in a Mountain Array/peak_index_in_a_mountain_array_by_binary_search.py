'''

Description:

Let's call an array A a mountain if the following properties hold:

A.length >= 3
There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
Given an array that is definitely a mountain, return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

Example 1:

Input: [0,1,0]
Output: 1
Example 2:

Input: [0,2,1,0]
Output: 1
Note:

3 <= A.length <= 10000
0 <= A[i] <= 10^6
A is a mountain, as defined above.

'''



from typing import List
class Solution:
    
    def findPeak(self, mountain_arr) -> int:
        
        left, right = 0, ( len(mountain_arr)-1 )
        
        while left < right :
            
            probe = ( left + right ) // 2
            
            if mountain_arr[probe] > mountain_arr[(probe+1)] :
                right = probe
            else:
                left = probe + 1
                
        return left
    
    

    def peakIndexInMountainArray(self, A: List[int]) -> int:
        
        # Find mountain peak
        peak_index = self.findPeak( A )
        
        return peak_index



# n : the length of mountain array

## Time Complexity: O( log n )
#
# The overhead in time is the cost of binary search of a list of n, which is of O( n )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for loop index and binary search variable, which is of O( 1 )



def test_bench():

    test_data = [
                     [1,2,3,4,5,3,1],
                     [0,1,2,4,2,1],
                     [1,2,3,4,5,3,1],
                     [1,5,2],
                     [1,2,3,5,3] 
                ]

    # expected output:
    '''
    4
    3
    4
    1
    3
    '''

    for test_seq in test_data:

        peak_index = Solution().peakIndexInMountainArray( A = test_seq )
        print( peak_index )

    return 



if __name__ == '__main__':

    test_bench()
