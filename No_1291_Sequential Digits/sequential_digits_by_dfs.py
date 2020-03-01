'''

Description:

An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

 

Example 1:

Input: low = 100, high = 300
Output: [123,234]



Example 2:

Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]
 

Constraints:

10 <= low <= high <= 10^9

'''


from typing import List
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        
        output = []
        
        digit_stack = list( range(1,10) )
        
        while digit_stack:
            
            cur_value = digit_stack.pop()
            
            if high >= cur_value >= low:
                output.append( cur_value )
            
            elif cur_value > high:
                # current value is out of boundary
                # stop growing on this case
                continue
            
            last_digit = int( str(cur_value)[-1] )
            
            if last_digit == 9:
                # last digit is 9 already
                # stop growing on this case
                continue
            
            growing_value = int( str(cur_value) + str(last_digit+1) )
            
            digit_stack.append( growing_value )
            
        return sorted( output )



from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'lowerbound upperbound')
def test_bench():

    test_data = [
                    TestEntry( lowerbound = 100, upperbound = 300),
                    TestEntry( lowerbound = 1000, upperbound = 13000),
                    TestEntry( lowerbound = 10, upperbound = 1000000000),
                ]

    # expected output:
    '''
    [123, 234]
    [1234, 2345, 3456, 4567, 5678, 6789, 12345]
    [12, 23, 34, 45, 56, 67, 78, 89, 123, 234, 345, 456, 567, 678, 789, 1234, 2345, 3456, 4567, 5678, 6789, 12345, 23456, 34567, 45678, 56789, 123456, 234567, 345678, 456789, 1234567, 2345678, 3456789, 12345678, 23456789, 123456789]    
    '''


    for t in test_data:

        print( Solution().sequentialDigits( low = t.lowerbound, high = t.upperbound) )

    return



if __name__ == '__main__':

    test_bench()