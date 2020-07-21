'''

Description:

Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.



Example 1:

Input: a = "11", b = "1"
Output: "100"



Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

Each string consists only of '0' or '1' characters.
1 <= a.length, b.length <= 10^4
Each string is either "0" or doesn't contain any leading zero.

'''



class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        return bin(int(a, 2) + int(b, 2))[2:]



# n : max(a, b), the larger betwwen a and b.

## Time Complexity: O( log n )
#
# The overhead in time is the cost is the binary addition of a and b, which is of O( log n )

## Space Complexity: O( log n )
#
# The overhead in space is the storage of the result of binary addition, which is of O( log n )



import unittest
class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().addBinary(a = "1010", b = "1011")
        self.assertEqual(result, "10101")



    def test_case_2( self ):
    
        result = Solution().addBinary(a = "11", b = "1")
        self.assertEqual(result, "100")


if __name__ == '__main__':

    unittest.main()        