'''

Description:

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true



Example 2:

Input: "race a car"
Output: false
 

Constraints:

s consists only of printable ASCII characters.

'''



class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        letters = [ char.lower() for char in s if char.isalnum() ]
        
        return letters == letters[::-1]


# n : the character length of input string

## Time Complexity: O( n )
#
# The overhead in time is the cost of list comprehension, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for list, which is of O( n )


import unittest
class Testing(unittest.TestCase):

    def test_case_1(self):

        result = Solution().isPalindrome(s="A man, a plan, a canal: Panama")
        self.assertEqual(result, True)


    def test_case_2(self):

        result = Solution().isPalindrome(s="race a car")
        self.assertEqual(result, False)


if __name__ == '__main__':

    unittest.main()