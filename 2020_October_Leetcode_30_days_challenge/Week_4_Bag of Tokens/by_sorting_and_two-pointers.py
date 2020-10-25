'''

Description:

You have an initial power of P, an initial score of 0, and a bag of tokens where tokens[i] is the value of the ith token (0-indexed).

Your goal is to maximize your total score by potentially playing each token in one of two ways:

If your current power is at least tokens[i], you may play the ith token face up, losing tokens[i] power and gaining 1 score.
If your current score is at least 1, you may play the ith token face down, gaining tokens[i] power and losing 1 score.
Each token may be played at most once and in any order. You do not have to play all the tokens.

Return the largest possible score you can achieve after playing any number of tokens.

 

Example 1:

Input: tokens = [100], P = 50
Output: 0
Explanation: Playing the only token in the bag is impossible because you either have too little power or too little score.



Example 2:

Input: tokens = [100,200], P = 150
Output: 1
Explanation: Play the 0th token (100) face up, your power becomes 50 and score becomes 1.
There is no need to play the 1st token since you cannot play it face up to add to your score.



Example 3:

Input: tokens = [100,200,300,400], P = 200
Output: 2
Explanation: Play the tokens in this order to get a score of 2:
1. Play the 0th token (100) face up, your power becomes 100 and score becomes 1.
2. Play the 3rd token (400) face down, your power becomes 500 and score becomes 0.
3. Play the 1st token (200) face up, your power becomes 300 and score becomes 1.
4. Play the 2nd token (300) face up, your power becomes 0 and score becomes 2.
 

Constraints:

0 <= tokens.length <= 1000
0 <= tokens[i], P < 104

'''


from typing import List

class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        
        # keep tokens in ascending order
        tokens.sort()
        
        left, right = 0, len(tokens)-1
        
        score = 0
        best_score = 0
        
        # game loop:
        while left <= right:
            
            if P >= tokens[left]:
                # use power to trade score
                P -= tokens[left]
                left += 1
                
                score += 1
                
                best_score = max(best_score, score)
                
            elif score > 0:
                # use score to trade power
                score -= 1
                
                P += tokens[right]
                right -=1
                
            else:
                # can not play anymore, exit game loop
                break
                
        return best_score
                



# n : the length of tokens

## Time Complexity: O( n log n )
#
# The overhead in time is the cost of sorting, which is of O( n log n )


## Space Complexity: O( 1 )
#
# The overhead in space is the storage for loop index and temporary variable, which is of O( 1 )


import unittest

class Tesing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().bagOfTokensScore( tokens = [100], P = 50 )
        self.assertEqual(result, 0)


    def test_case_2( self ):

        result = Solution().bagOfTokensScore( tokens = [100,200], P = 150 )
        self.assertEqual(result, 1)


    def test_case_3( self ):

        result = Solution().bagOfTokensScore( tokens = [100,200,300,400], P = 200 )
        self.assertEqual(result, 2)


if __name__ == '__main__':

    unittest.main()        
