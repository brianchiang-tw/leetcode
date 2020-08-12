'''

Description:

Given an array of integers arr, and three integers a, b and c. You need to find the number of good triplets.

A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:

0 <= i < j < k < arr.length
|arr[i] - arr[j]| <= a
|arr[j] - arr[k]| <= b
|arr[i] - arr[k]| <= c
Where |x| denotes the absolute value of x.

Return the number of good triplets.

 

Example 1:

Input: arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3
Output: 4
Explanation: There are 4 good triplets: [(3,0,1), (3,0,1), (3,1,1), (0,1,1)].



Example 2:

Input: arr = [1,1,2,2,3], a = 0, b = 0, c = 1
Output: 0
Explanation: No triplet satisfies all conditions.
 

Constraints:

3 <= arr.length <= 100
0 <= arr[i] <= 1000
0 <= a, b, c <= 1000

'''


from typing import List

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        
        size = len(arr)
        
        good_count = 0
        
        for i in range(size-2):
            for j in range(i+1, size-1):
                for k in range(j+1, size):
                    
                    ok_a = abs(arr[i] - arr[j]) <= a
                    ok_b = abs(arr[j] - arr[k]) <= b
                    ok_c = abs(arr[i] - arr[k]) <= c
                    
                    if all((ok_a, ok_b, ok_c)):
                        good_count += 1
                        
                        
        return good_count



# n : the length of input list arr

## Time Complexity: O( n^3 )
#
# The overhead in time is the cost of nested loops, which is of O( n^3 )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for loop index and temporary variable, which is of O( 1 )



import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().countGoodTriplets(arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3)
        self.assertEqual(result, 4)


    def test_case_2( self ):
    
        result = Solution().countGoodTriplets(arr = [1,1,2,2,3], a = 0, b = 0, c = 1)
        self.assertEqual(result, 0)


if __name__ == '__main__':

    unittest.main()