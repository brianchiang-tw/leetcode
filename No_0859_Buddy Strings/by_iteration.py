'''

Description:

Given two strings A and B of lowercase letters, return true if you can swap two letters in A so the result is equal to B, otherwise, return false.

Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at A[i] and A[j]. For example, swapping at indices 0 and 2 in "abcd" results in "cbad".

 

Example 1:

Input: A = "ab", B = "ba"
Output: true
Explanation: You can swap A[0] = 'a' and A[1] = 'b' to get "ba", which is equal to B.



Example 2:

Input: A = "ab", B = "ab"
Output: false
Explanation: The only letters you can swap are A[0] = 'a' and A[1] = 'b', which results in "ba" != B.



Example 3:

Input: A = "aa", B = "aa"
Output: true
Explanation: You can swap A[0] = 'a' and A[1] = 'a' to get "aa", which is equal to B.



Example 4:

Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true



Example 5:

Input: A = "", B = "aa"
Output: false
 

Constraints:

0 <= A.length <= 20000
0 <= B.length <= 20000
A and B consist of lowercase letters.

'''



class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        
        if len(A) != len(B):
            
            # Quick response for different length
            return False
        
        
        if A == B:
            
            # Quick resposne for identical string with repeated characters
            return len(set(A)) < len(A)
        
        
        # Check for character difference
        diff =  [ (char_a, char_b) for char_a, char_b in zip(A, B) if char_a != char_b ]
        
        # They're buddy strings only when two difference character pairs with symmetry exist
        return len(diff) == 2 and ( diff[0] == diff[1][::-1] )



# n : the max character length betwen A and B

## Time Complexity: O( n )
#
# The overhead in time is the cost of for-loop, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for diff, which is of O( n )


import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().buddyStrings(A = "ab", B = "ba")
        self.assertEqual(result, True)


    def test_case_2( self ):

        result = Solution().buddyStrings(A = "ab", B = "ab")
        self.assertEqual(result, False)


    def test_case_3( self ):

        result = Solution().buddyStrings(A = "aa", B = "aa")
        self.assertEqual(result, True)


    def test_case_4( self ):

        result = Solution().buddyStrings(A = "aaaaaaabc", B = "aaaaaaacb")
        self.assertEqual(result, True)


    def test_case_5( self ):

        result = Solution().buddyStrings(A = "", B = "aa")
        self.assertEqual(result, False)



if __name__ == '__main__':

    unittest.main()