'''

Descrtipion:

You are playing the following Bulls and Cows game with your friend: You write down a number and ask your friend to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called "bulls") and how many digits match the secret number but locate in the wrong position (called "cows"). Your friend will use successive guesses and hints to eventually derive the secret number.

Write a function to return a hint according to the secret number and friend's guess, use A to indicate the bulls and B to indicate the cows. 

Please note that both secret number and friend's guess may contain duplicate digits.

Example 1:

Input: secret = "1807", guess = "7810"

Output: "1A3B"

Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.



Example 2:

Input: secret = "1123", guess = "0111"

Output: "1A1B"

Explanation: The 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow.
Note: You may assume that the secret number and your friend's guess only contain digits, and their lengths are always equal.

'''



from collections import defaultdict


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        char_occ_dict = defaultdict(int)
        
        bull, cow = 0, 0
        
        for i in range(len(secret)):
            
            if secret[i] == guess[i]:
                # full match (Bull) of current character
                bull += 1
            
            else:
                # not-full match (Cow) or mismatch
                
                
                if char_occ_dict[ secret[i] ] < 0:
                    # current character has showed up in guess somewhere else
                    cow += 1
                
                # secret produces one occurrence
                char_occ_dict[ secret[i] ]  += 1
                
                
                if char_occ_dict[ guess[i] ] > 0:
                    # current character has showed up in secret somewhere else
                    cow += 1
                
                # guess consumes one occurrence
                char_occ_dict[ guess[i] ]  -= 1
        
        
        return str(bull) + 'A' + str(cow) + 'B'



# n : the character length of input string, secret.

## Time Complexity: O( n )
#
# The overhead in time is the cost of for-loop iteration, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for dictionary, which is of O( n )



import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().getHint( secret = "1807", guess = "7810" )
        self.assertEqual(result, '1A3B')


    def test_case_2( self ):

        result = Solution().getHint( secret = "1123", guess = "0111" )
        self.assertEqual(result, '1A1B')


if __name__ == '__main__':

    unittest.main()