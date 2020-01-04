'''

Description:

(This problem is an interactive problem.)

You may recall that an array A is a mountain array if and only if:

A.length >= 3
There exists some i with 0 < i < A.length - 1 such that:
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]
Given a mountain array mountainArr, return the minimum index such that mountainArr.get(index) == target.  If such an index doesn't exist, return -1.

You can't access the mountain array directly.  You may only access the array using a MountainArray interface:

MountainArray.get(k) returns the element of the array at index k (0-indexed).
MountainArray.length() returns the length of the array.
Submissions making more than 100 calls to MountainArray.get will be judged Wrong Answer.  Also, any solutions that attempt to circumvent the judge will result in disqualification.

 

Example 1:

Input: array = [1,2,3,4,5,3,1], target = 3
Output: 2
Explanation: 3 exists in the array, at index=2 and index=5. Return the minimum index, which is 2.
Example 2:

Input: array = [0,1,2,4,2,1], target = 3
Output: -1
Explanation: 3 does not exist in the array, so we return -1.
 

Constraints:

3 <= mountain_arr.length() <= 10000
0 <= target <= 10^9
0 <= mountain_arr.get(index) <= 10^9

'''



# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    
    def findPeak(self, mountain_arr) -> int:
        
        left, right = 0, mountain_arr.length()-1
        
        while left < right :
            
            probe = ( left + right ) // 2
            
            if mountain_arr.get(probe) > mountain_arr.get(probe+1):
                right = probe
            else:
                left = probe + 1
                
        return left
    
    

    def findTarget(self, mountain_arr, peak_index, target) -> int:
        
        # Phase_#1: Find Target in uphill
        left, right = 0, peak_index
        
        while left <= right:
            
            probe = ( left + right ) // 2
            
            probe_value = mountain_arr.get( probe )
            
            if probe_value == target:
                return probe
            
            elif probe_value < target:
                left = probe+1
            
            else:
                right = probe-1
        
        
        # Phase_#2: Find Target in downhill
        left, right = peak_index, ( mountain_arr.length()-1 )
        
        while left <= right:
            
            probe = ( left + right ) // 2
            
            probe_value = mountain_arr.get( probe )
            
            if probe_value == target:
                return probe
            
            elif probe_value < target:
                right = probe-1
            
            else:
                left = probe+1
                
        return -1
            
    

    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        
        # Find mountain peak
        peak_index = self.findPeak(mountain_arr)
        
        # Find target in up-hill,then down-hill, or target does not exist in montain
        index_of_target = self.findTarget( mountain_arr, peak_index, target)
        
        return index_of_target



# n : the length of mountain array

## Time Complexity: O( log n )
#
# The overhead in time is the cost of binary search of a list of n, which is of O( n )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for loop index and binary search variable, which is of O( 1 )



class MountainArray:
   
    def __init__(self, arr):

       self.sequence = arr[::]

    def get(self, index: int) -> int:

        return self.sequence[index]

    def length(self) -> int:
        return len(self.sequence)




def test_bench():

    test_data = [
                    ( [1,2,3,4,5,3,1], 3 ),
                    ( [0,1,2,4,2,1], 3 ),
                    ( [1,2,3,4,5,3,1], 2 ),
                    ( [1,5,2], 2 ),
                    ( [1,2,3,5,3], 0 )
                ]

    # expected output:
    '''
    2
    -1
    1
    2
    -1
    '''

    for test_pair in test_data:

        target_index = Solution().findInMountainArray( target = test_pair[1], mountain_arr= MountainArray( test_pair[0] ) )
        print( target_index )

    return 



if __name__ == '__main__':

    test_bench()
