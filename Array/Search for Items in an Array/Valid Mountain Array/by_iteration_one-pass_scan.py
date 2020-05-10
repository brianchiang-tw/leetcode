'''

Description:

Given an array A of integers, return true if and only if it is a valid mountain array.

Recall that A is a mountain array if and only if:

A.length >= 3
There exists some i with 0 < i < A.length - 1 such that:
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]


 
Example 1:

Input: [2,1]
Output: false
Example 2:

Input: [3,5,5]
Output: false
Example 3:

Input: [0,3,2,1]
Output: true
 

Note:

0 <= A.length <= 10000
0 <= A[i] <= 10000 
 

 
Hint #1  

It's very easy to keep track of a monotonically increasing or decreasing ordering of elements. You just need to be able to determine the start of the valley in the mountain and from that point onwards, it should be a valley i.e. no mini-hills after that. 

'''



from typing import List

class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        
        if len(A) < 3 or A[1] <= A[0]:
            # Quick rejection for invalid cases
            return False
        
        increasing = True
        last = A[1]
        
        for cur_num in A[2:]:
            
            if increasing:
            # up-hill

                if cur_num < last:
                    increasing = False
                    
                elif cur_num == last:
                    return False
                
            else:
            # down-hill

                if cur_num >= last:
                    return False
            
            # update current number
            last = cur_num
        
        
        
        if increasing:
            return False
        
        else:
            # Final valid state is decreasing after mountain climbing
            return True



# n : the length of input array, A

## Time Complexity: O( n )
#
# The overhead in time is the cost of linear scan, which is of O( n )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for loop index and temporary flag, which is of O( 1 )


from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'sequence')

def test_bench():

    test_data = [
                    TestEntry( sequence = [2,1] ) ,         # False
                    TestEntry( sequence = [3,5,5] ),        # False
                    TestEntry( sequence = [0,3,2,1] ),      # True
                    TestEntry( sequence = [1,2,3,4] ),      # False
                    TestEntry( sequence = [4,3,2,1] ),      # False
                    TestEntry( sequence = [1,2,3,2,1] ),    # True
                    TestEntry( sequence = [1,3,3,2,1] ),    # False
                    TestEntry( sequence = [1,2,3,3,1] ),    # False
                    TestEntry( sequence = [1,5,3,5,1] ),    # False
                    TestEntry( sequence = [] ),             # corner case, False
                ]

    for t in test_data:

        print( Solution().validMountainArray( A = t.sequence) )
    
    return



if __name__ == '__main__':

    test_bench()