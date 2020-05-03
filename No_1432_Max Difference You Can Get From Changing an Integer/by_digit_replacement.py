'''

Description:

You are given an integer num. You will apply the following steps exactly two times:

Pick a digit x (0 <= x <= 9).
Pick another digit y (0 <= y <= 9). The digit y can be equal to x.
Replace all the occurrences of x in the decimal representation of num by y.
The new integer cannot have any leading zeros, also the new integer cannot be 0.
Let a and b be the results of applying the operations to num the first and second times, respectively.

Return the max difference between a and b.

 

Example 1:

Input: num = 555
Output: 888
Explanation: The first time pick x = 5 and y = 9 and store the new integer in a.
The second time pick x = 5 and y = 1 and store the new integer in b.
We have now a = 999 and b = 111 and max difference = 888



Example 2:

Input: num = 9
Output: 8
Explanation: The first time pick x = 9 and y = 9 and store the new integer in a.
The second time pick x = 9 and y = 1 and store the new integer in b.
We have now a = 9 and b = 1 and max difference = 8



Example 3:

Input: num = 123456
Output: 820000



Example 4:

Input: num = 10000
Output: 80000



Example 5:

Input: num = 9288
Output: 8700
 

Constraints:

1 <= num <= 10^8

'''



class Solution:
    def maxDiff(self, num: int) -> int:
        
        num_string = str(num)
        
        def apply_transform( src_char: str, dest_char: str, s: str):
        
            return int( s.replace( src_char, dest_char ) )
        
        # -----------------------------------------------------------
        
        # digit replacement for maximum number
        
        max_num = num
        
        for char in num_string:
            if char < '9':
                max_num = apply_transform( char, '9', num_string ) 
                break
        
        # -----------------------------------------------------------
        
        # digit replacement for minimum number
        
        min_num = num
        
        if num_string[0] > '1':
            # leading digit cannot be zero
            min_num = apply_transform( num_string[0], '1', num_string )
        
        else:
            for char in num_string[1:]:
                if char > '1':
                    min_num = apply_transform( char, '0', num_string )
                    break
        
        return max_num - min_num



# n : the value of input number

## Time Complexity: O( log n )
#
# The overhead in time is the cost of digit replacement, which is of O( log n ).

## Space Complexity: O( log n )
#
# The overhead in space is the storage for output number, which is of O( log n ).


from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'number')
def test_bench():

    test_data = [
                    TestEntry( number = 555 ),
                    TestEntry( number = 9 ),
                    TestEntry( number = 123456 ),
                    TestEntry( number = 10000 ),
                    TestEntry( number = 9288 ),
                ]

    # expected output:
    '''
    888
    8
    820000
    80000
    8700
    '''

    for t in test_data:

        print( Solution().maxDiff( num = t.number) )
    
    return



if __name__ == '__main__':

    test_bench()