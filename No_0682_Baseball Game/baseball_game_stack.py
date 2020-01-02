'''

Description:

You're now a baseball game point recorder.

Given a list of strings, each string can be one of the 4 following types:

Integer (one round's score): Directly represents the number of points you get in this round.
"+" (one round's score): Represents that the points you get in this round are the sum of the last two valid round's points.
"D" (one round's score): Represents that the points you get in this round are the doubled data of the last valid round's points.
"C" (an operation, which isn't a round's score): Represents the last valid round's points you get were invalid and should be removed.
Each round's operation is permanent and could have an impact on the round before and the round after.

You need to return the sum of the points you could get in all the rounds.

Note:
The size of the input list will be between 1 and 1000.
Every integer represented in the list will be between -30000 and 30000.

'''

from typing import List
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        
        score_stack = []
        
        for opcode in ops:
            
            if opcode == '+':
                # +: Summation of last two scores, and push in
                score_stack.append( score_stack[-1] + score_stack[-2] )
            
            elif opcode == 'D':
                # D: Double last score, and push in
                score_stack.append( score_stack[-1]*2 )
                
            elif opcode == 'C':
                # C: Cancel last score, pop top
                score_stack.pop()
                
            else:
                # Integer, direct push int
                score_stack.append( int(opcode) )
                
                
        return sum( score_stack ) 



# n : length of input operation sequence

## Time Complexity: O(n)
#
# The overhead in time is the for loop iterating on ops, which is of O( n ).

## Space Complexity: O(n)
#
# The overhead in space is to maintain a stack for score record, whic his of O( n ).



def test_bench():

    test_data = [
                    ["5","2","C","D","+"],
                    ["5","-2","4","C","D","9","+","+"]
                ]

    # expected output:
    '''
    30
    27
    '''

    for test_sequence in test_data:

        print( Solution().calPoints(test_sequence) )

    return 



if __name__ == '__main__':

    test_bench()
