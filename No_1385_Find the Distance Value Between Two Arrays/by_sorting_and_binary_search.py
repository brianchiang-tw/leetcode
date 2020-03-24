'''

Description:

Given two integer arrays arr1 and arr2, and the integer d, return the distance value between the two arrays.

The distance value is defined as the number of elements arr1[i] such that there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.

 

Example 1:

Input: arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2
Output: 2

Explanation: 

For arr1[0]=4 we have: 

|4-10|=6 > d=2 
|4-9|=5 > d=2 
|4-1|=3 > d=2 
|4-8|=4 > d=2 

For arr1[1]=5 we have: 

|5-10|=5 > d=2 
|5-9|=4 > d=2 
|5-1|=4 > d=2 
|5-8|=3 > d=2

For arr1[2]=8 we have:

|8-10|=2 <= d=2
|8-9|=1 <= d=2
|8-1|=7 > d=2
|8-8|=0 <= d=2



Example 2:

Input: arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3
Output: 2



Example 3:

Input: arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6
Output: 1
 

Constraints:

1 <= arr1.length, arr2.length <= 500
-10^3 <= arr1[i], arr2[j] <= 10^3
0 <= d <= 100

'''


from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        
        # pre-processing, keep arr2 in ascending order
        arr2.sort()
        
        counter_out_of_range_d = 0
        

        # scan each element in arr1, check it is out of range d or not
        for element in arr1:
            
            left = bisect_left( arr2, element - d )
            right = bisect_right( arr2, element + d )
            
            if left == right:
                
                # if e-d, e+d is at the same index, then element e is out of range d
                counter_out_of_range_d += 1
                
        return counter_out_of_range_d



# m : the length of input list, arr1
# n : the length of input list, arr2

## Time Complexity: O( m log n + n log n) = O( (m+n) log n )
#
# The overhead is the cost of sorting on arr2, which is of O( n log n ),
# and the cost of for loop on arr1 with binary search on arr2, which is of O( m log n).
#
# It takes O( m log n + n log n ) = O( (m+n) log n ) in total


## Space Complexity: O( 1 )
#
# The overhead in space is the storage for temporarily varaible and loop index, which is of O( 1 ).



from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'arr1 arr2 d')

def test_bench():

    test_data = [
                    TestEntry( arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2 ),
                    TestEntry( arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 2 ),
                    TestEntry( arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6 ),
                ]

    # expected output:
    '''
    2
    3
    1    
    '''


    for t in test_data :

        print( Solution().findTheDistanceValue( arr1 = t.arr1, arr2 = t.arr2, d= t.d ) )

    return



if __name__ == '__main__':

    test_bench()