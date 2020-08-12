'''

Description:

Given an array of numbers arr. A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

Return true if the array can be rearranged to form an arithmetic progression, otherwise, return false.

 

Example 1:

Input: arr = [3,5,1]
Output: true
Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2 respectively, between each consecutive elements.



Example 2:

Input: arr = [1,2,4]
Output: false
Explanation: There is no way to reorder the elements to obtain an arithmetic progression.
 

Constraints:

2 <= arr.length <= 1000
-10^6 <= arr[i] <= 10^6

'''


from typing import List

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        
        arr.sort()
        
        diff = set()
        
        for i in range(len(arr)-1):
            
            # add current difference into set
            diff.add(arr[i + 1] - arr[i])
        
        # return True if only one kind of difference exists
        return 1 == len(diff)


import unittest
class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().canMakeArithmeticProgression( arr=[3,5,1] )
        self.assertEqual(result, True)


    def test_case_2( self ):
    
        result = Solution().canMakeArithmeticProgression( arr=[1,2,4] )
        self.assertEqual(result, False)



if __name__ == '__main__':

    unittest.main()