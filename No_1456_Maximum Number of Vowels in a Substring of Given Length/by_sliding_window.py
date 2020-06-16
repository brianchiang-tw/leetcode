'''

Description:

Given a string s and an integer k.

Return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are (a, e, i, o, u).

 

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.



Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.



Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.



Example 4:

Input: s = "rhythms", k = 4
Output: 0
Explanation: We can see that s doesn't have any vowel letters.



Example 5:

Input: s = "tryhard", k = 4
Output: 1
 

Constraints:

1 <= s.length <= 10^5
s consists of lowercase English letters.
1 <= k <= s.length

'''



class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        vowels = ['a','e','i','o','u']
        
        substring = s[:k]
        
        vowel_count = sum( 1 for char in substring if char in vowels )
        
        # record for max vowel count in substring
        max_vowel_count = vowel_count
        
        
        # sliding window of size k
        for tail_index in range(k, len(s)):
            
            head_index = tail_index - k
            head_char, tail_char = s[head_index], s[tail_index]
            
            if head_char in vowels:
                vowel_count -= 1
                
            if tail_char in vowels:
                vowel_count += 1
                
            max_vowel_count = max( max_vowel_count, vowel_count)
            
        
        return max_vowel_count



# n : the length of input string s

## Time Complexity: O( n )
#
# The overhead in time is the cost of loop for sliding window, which is of O( n ).

## Space Complexity: O( k )
#
# The overhead in space is the storage for substring, which is of O( k ).


import unittest
class Testing( unittest.TestCase ):

    def test_case_1(self):

        result = Solution().maxVowels( s = "abciiidef", k = 3 )
        self.assertEqual( result, 3)


    def test_case_2(self):
    
        result = Solution().maxVowels( s = "aeiou", k = 2 )
        self.assertEqual( result, 2)


    def test_case_3(self):
        
        result = Solution().maxVowels( s = "leetcode", k = 3 )
        self.assertEqual( result, 2)


    def test_case_4(self):
        
        result = Solution().maxVowels( s = "rhythms", k = 4 )
        self.assertEqual( result, 0)

        
    def test_case_5(self):
        
        result = Solution().maxVowels( s = "tryhard", k = 4 )
        self.assertEqual( result, 1)        



if __name__ == '__main__':

    unittest.main()