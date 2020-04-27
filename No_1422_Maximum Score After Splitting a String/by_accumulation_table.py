'''

Description:

Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).

The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.

 

Example 1:

Input: s = "011101"
Output: 5 
Explanation: 
All possible ways of splitting s into two non-empty substrings are:
left = "0" and right = "11101", score = 1 + 4 = 5 
left = "01" and right = "1101", score = 1 + 3 = 4 
left = "011" and right = "101", score = 1 + 2 = 3 
left = "0111" and right = "01", score = 1 + 1 = 2 
left = "01110" and right = "1", score = 2 + 1 = 3



Example 2:

Input: s = "00111"
Output: 5
Explanation: When left = "00" and right = "111", we get the maximum score = 2 + 3 = 5



Example 3:

Input: s = "1111"
Output: 3

'''



from collections import deque

class Solution:
    def maxScore(self, s: str) -> int:
        
        size = len(s)
        
        # ---------------------------------------------
        # Build prefix accumulation table for leading 0s
        prefix_zero = [ 1 ] if s[0] == '0' else [ 0 ]
        
        for i in range(1,size):
            if s[i] == '0':
                cur_zero_accumulation = prefix_zero[-1] + 1
            else:
                cur_zero_accumulation = prefix_zero[-1]
            
            prefix_zero.append( cur_zero_accumulation )
        
        
        
        # ---------------------------------------------
        # Build postfix accumulation table for trailing 1s
        postfix_one = deque([ 1 ]) if s[-1] == '1' else deque([ 0 ])
        
        for j in reversed( range(0, size-1) ):
            if s[j] == '1':
                cur_one_accumulation = postfix_one[0] + 1 
            else:
                cur_one_accumulation = postfix_one[0]
            
            postfix_one.appendleft( cur_one_accumulation )
            
        
        
        # ---------------------------------------------
        # Update max score by linear scan and look-up table
        
        max_score = 0
        for split_idx in range(0, size-1):
            cur_score_of_split = prefix_zero[split_idx] + postfix_one[split_idx+1]
            max_score = max( max_score,  cur_score_of_split)
            
        return max_score



# n : the character length of input string, s.

## Time Complexity: O( n )
#
# The overhead in time is the cost of for loop of linear scan, which is of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the storage for table, prefix_zero as well as postfix_one, which are of O( n ).


from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'string')
def test_bench():

    test_data = [
                    TestEntry( string = "011101"),
                    TestEntry( string = "00111"),
                    TestEntry( string = "1111"),
                    TestEntry( string = "1010"),
                    TestEntry( string = "1101"),
                    TestEntry( string = "01"),
                    TestEntry( string = "10"),
                    TestEntry( string = "11"),
                    TestEntry( string = "00"),
                ]

    # expected output:
    '''
    5
    5
    3
    2
    2
    2
    0
    1
    1
    '''

    for t in test_data:
        print( Solution().maxScore( s = t.string) )

    return



if __name__ == '__main__':

    test_bench()