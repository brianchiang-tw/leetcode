'''

Description:

Given two version numbers, version1 and version2, compare them.

Version numbers consist of one or more revisions joined by a dot '.'. Each revision consists of digits and may contain leading zeros. Every revision contains at least one character. Revisions are 0-indexed from left to right, with the leftmost revision being revision 0, the next revision being revision 1, and so on. For example 2.5.33 and 0.1 are valid version numbers.

To compare version numbers, compare their revisions in left-to-right order. Revisions are compared using their integer value ignoring any leading zeros. This means that revisions 1 and 001 are considered equal. If a version number does not specify a revision at an index, then treat the revision as 0. For example, version 1.0 is less than version 1.1 because their revision 0s are the same, but their revision 1s are 0 and 1 respectively, and 0 < 1.

Return the following:

If version1 < version2, return -1.
If version1 > version2, return 1.
Otherwise, return 0.
 

Example 1:

Input: version1 = "1.01", version2 = "1.001"
Output: 0
Explanation: Ignoring leading zeroes, both "01" and "001" represent the same integer "1".



Example 2:

Input: version1 = "1.0", version2 = "1.0.0"
Output: 0
Explanation: version1 does not specify revision 2, which means it is treated as "0".



Example 3:

Input: version1 = "0.1", version2 = "1.1"
Output: -1
Explanation: version1's revision 0 is "0", while version2's revision 0 is "1". 0 < 1, so version1 < version2.



Example 4:

Input: version1 = "1.0.1", version2 = "1"
Output: 1



Example 5:

Input: version1 = "7.5.2.4", version2 = "7.5.3"
Output: -1
 

Constraints:

1 <= version1.length, version2.length <= 500
version1 and version2 only contain digits and '.'.
version1 and version2 are valid version numbers.
All the given revisions in version1 and version2 can be stored in a 32-bit integer.

'''



from itertools import zip_longest

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        # spilt token with '.' as separator
        ver_1, ver_2 = version1.split('.'), version2.split('.')
        
        vernum_1, vernum_2 = 0, 0
        
        # compute version number in base 10
        for v1, v2 in zip_longest(ver_1, ver_2, fillvalue = '0'):
            
            vernum_1, vernum_2 = 10*vernum_1 + int(v1), 10*vernum_2 + int(v2)
            
        
        
        if vernum_1 > vernum_2:
            return 1
        
        elif vernum_1 < vernum_2:
            return -1
        
        else:
            return 0



# m : character length of input string version1
# n : character length of input string version2

## Time Complexity: O( m + n )
#
# The overhead in time is the cost of token parsin, which is of O( m + n )

## Space Complexity: O( m + n )
#
# The overhead in space is the storage for tokens, which is of O( m + n )

import unittest
class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().compareVersion(version1 = "1.01", version2 = "1.001")
        self.assertEqual(result, 0)


    def test_case_2( self ):

        result = Solution().compareVersion(version1 = "1.0", version2 = "1.0.0")
        self.assertEqual(result, 0)


    def test_case_3( self ):

        result = Solution().compareVersion(version1 = "0.1", version2 = "1.1")
        self.assertEqual(result, -1)


    def test_case_4( self ):

        result = Solution().compareVersion(version1 = "1.0.1", version2 = "1")
        self.assertEqual(result, 1)


    def test_case_5( self ):

        result = Solution().compareVersion(version1 = "7.5.2.4", version2 = "7.5.3")
        self.assertEqual(result, -1)        


if __name__ == '__main__':

    unittest.main()
        