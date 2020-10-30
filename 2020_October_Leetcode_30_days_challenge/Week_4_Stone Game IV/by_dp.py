'''

Description:

Alice and Bob take turns playing a game, with Alice starting first.

Initially, there are n stones in a pile.  On each player's turn, that player makes a move consisting of removing any non-zero square number of stones in the pile.

Also, if a player cannot make a move, he/she loses the game.

Given a positive integer n. Return True if and only if Alice wins the game otherwise return False, assuming both players play optimally.

 

Example 1:

Input: n = 1
Output: true
Explanation: Alice can remove 1 stone winning the game because Bob doesn't have any moves.
Example 2:

Input: n = 2
Output: false
Explanation: Alice can only remove 1 stone, after that Bob removes the last one winning the game (2 -> 1 -> 0).
Example 3:

Input: n = 4
Output: true
Explanation: n is already a perfect square, Alice can win with one move, removing 4 stones (4 -> 0).
Example 4:

Input: n = 7
Output: false
Explanation: Alice can't win the game if Bob plays optimally.
If Alice starts removing 4 stones, Bob will remove 1 stone then Alice should remove only 1 stone and finally Bob removes the last one (7 -> 3 -> 2 -> 1 -> 0). 
If Alice starts removing 1 stone, Bob will remove 4 stones then Alice only can remove 1 stone and finally Bob removes the last one (7 -> 6 -> 2 -> 1 -> 0).
Example 5:

Input: n = 17
Output: false
Explanation: Alice can't win the game if Bob plays optimally.
 

Constraints:

1 <= n <= 10^5


Hint #1  
Use dynamic programming to keep track of winning and losing states. Given some number of stones, Alice can win if she can force Bob onto a losing state.

'''



class Solution:
    def winnerSquareGame(self, n):

        # dynamic programming table for start value from 0 to n
        optimal_play = [ False for _ in range(n+1) ]
        
        # update dynamic programming table for each number in bottom-up order
        for number in range(1, n+1):
            
            # Alice can win with number if there exist a square value i^2 such that optimal_play of number-i^2 cannot win always.
            optimal_play[number] = not all( optimal_play[number-i**2] for i in range(1, int(number**0.5)+1 ))
        
        
        # Check whether Alice can win with start number n
        return optimal_play[n]


# n : the input value

## Time Complexity: O( n sqrt(n) )
#
# The overhead in time is the cost of nested loop, which is of O( n sqrt(n) )

## Space Complexity: O( n )
#
# The overhead in space is the straoge for dynamic programming table, which is of O( n )



import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().winnerSquareGame( n=1 )
        self.assertEqual(result, True)


    def test_case_2( self ):

        result = Solution().winnerSquareGame( n=2 )
        self.assertEqual(result, False)


    def test_case_3( self ):

        result = Solution().winnerSquareGame( n=4 )
        self.assertEqual(result, True)
        

    def test_case_4( self ):

        result = Solution().winnerSquareGame( n=7 )
        self.assertEqual(result, False)


    def test_case_5( self ):

        result = Solution().winnerSquareGame( n=17 )     
        self.assertEqual(result, False)                       



if __name__ == '__main__':

    unittest.main()        