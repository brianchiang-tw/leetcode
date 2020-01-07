'''

Description:

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


from collections import Counter
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        secret_list, guess_list = list(secret), list(guess)
        
        i = 0
        
        while i < len(secret_list):
            
            # check perfect match
            if secret_list[i] == guess_list[i]:
                
                del secret_list[i], guess_list[i]
                
                i -= 1
                
            i += 1
            
        
        # perfect match: both letter and index is correct
        num_of_A = len(secret)-len(secret_list)

        # letter match but index is not
        num_of_B = sum( ( Counter(secret_list) & Counter(guess_list) ).values() )
        
        return str(num_of_A) + "A" + str(num_of_B) + "B"


# n : the length of inputs string

## Time Complexity: O( n^2 )
#
# The overhead in time is the while loop itertaing on i of O( n ), and del ...[i] of O( n ).
# It cost O( n^2 ) together.


## Space Complexity: O( n )
#
# The overhead in space is the storage for Counter(...), which is of O( n ).



def test_bench():
    
    test_data = [
                    ("1807", "7810"),
                    ("1123", "0111"),
                    ("1", "1"),
                    ("1", "0"),
                    ("1234567890", "1234567890"),
                    ("1234567890", "0123456789"),
                ]


    # expected output:
    '''
    1A3B
    1A1B
    1A0B
    0A0B
    10A0B
    0A10B
    '''


    for test_pair in test_data:

        print( Solution().getHint( *test_pair ) )
    
    return



if __name__ == '__main__':

    test_bench()