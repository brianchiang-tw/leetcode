'''

Description:

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!
Example :

Input: n = 10, pick = 6
Output: 6

'''



# The guess API is already defined for you.
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:
secret_number = -1
def guess(num:int) -> int:

    if secret_number > num:
        return 1
    elif secret_number < num:
        return -1
    else:
        return 0



class Solution:
    def guessNumber(self, n: int) -> int:
        
        lower, upper = 1, n
        
        while lower <= upper:
            
            mid = lower + (upper - lower)//2
            
            query = guess(mid)
            if query == 0:
                # guess number is the same as hidden number
                return mid
            
            elif query == 1:
                # hidden number is higher than guessing
                lower = mid+1
                
            else:
                # hidden number is lower than guessing
                upper = mid-1



# n : the input value

## Time Complexity: O( log n )
#
# The overhead in time is the cost of binary search, which is of O( log n ).

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for looping variable, which is of O( 1 ).



from collections import namedtuple
def test_bench():

    global secret_number
    TestEntry = namedtuple('TestEntry','n hidden_number')
    
    test_data = [ 
                    TestEntry(10, 6),
                    TestEntry(100, 85),
                    TestEntry(100, 36)
    
                ]
    
    # expected output:
    '''
    6
    85
    36
    '''

    for test_input in test_data:
        secret_number = test_input.hidden_number
        print( Solution().guessNumber(test_input.n) )
    
    return 



if __name__ == '__main__':

    test_bench()