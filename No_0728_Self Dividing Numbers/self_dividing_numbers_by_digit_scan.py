'''

Description:

A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

Example 1:
Input: 
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
Note:

The boundaries of each input argument are 1 <= left <= right <= 10000.

'''


from typing import List
class Solution:
    
    def check_self_divide( self, num:int  )->bool:
    
        str_num = str( num )
        
        if '0' in str_num:
            # excluding numbers with 0 inside
            return False
        
        for digit in str_num:
            if ( num % int(digit) )!= 0:
                return False
            
        return True
    
    
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
    
    
        self_dividing_numbers = []
    
        for number in range(left, right+1):
            
            if self.check_self_divide( number ):
                
                self_dividing_numbers.append( number )
                
        
        return self_dividing_numbers


# n : the input value of right

## Time Complexity: O( n log n)
#
# The outer for loop iterating on number takes O( n ).
# And the innter for loop iterating on digit tales O( log n )
# Thus, the overhead in time is O( n log n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for self-dividing numbers, which is of O( n )




def test_bench():

    test_data = [ (1, 22), (1, 100) ]


    # expected output:
    '''
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22, 24, 33, 36, 44, 48, 55, 66, 77, 88, 99]
    '''

    for test_pair in test_data:
        print( Solution().selfDividingNumbers(*test_pair) )
    
    return 



if __name__ == '__main__':

    test_bench()