'''

Description:

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true



Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?

'''



from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        return Counter(s) == Counter(t)


# m : the length of s
# n : the length of t

## Time Complexity: O( m + n )
#
# The overhead in time is the cost of dictionary building, O( m ) for s and O( n ) for t, which is O( m + n ) totally.


## Space Complexity: O( m + n )
#
# The overhead in space is the storage for dictionary, O( m ) for s and O( n ) for t, which is O( m + n ) totally.



import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().isAnagram( s='anagram', t='nagaram')
        self.assertEqual(result, True)


    def test_case_2( self ):

        result = Solution().isAnagram( s='rat', t='car')
        self.assertEqual(result, False)


if __name__ == '__main__':

    unittest.main()        