class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x <= 1:
            return x
        
        mid = x // 2
        upper_bound = x
        lower_bound = 0
        
        while lower_bound+1 != upper_bound:
            
            trial = mid ** 2
            next_trial = (mid+1)**2
            
            if trial <= x < next_trial:
                return mid
            elif trial > x:
                upper_bound = mid
                mid = ( lower_bound + upper_bound )// 2
            else:
                lower_bound = mid
                mid = ( lower_bound + upper_bound )// 2
                
        return lower_bound



# n : the number of input value

## Time Complexity: O( log n )
#
# The overhead in time is the upper-bound of binary search, which is of O( log n ).

## Space Complexity: O( 1 )
#
# The overhead in space is the variable for mathematical computation, which is of O( 1 )



def test_bench():

    test_data = [0, 1, 80, 63, 48 ]

    # expected output:
    '''
    0
    1
    8
    7
    6
    '''

    for n in test_data:

        print( Solution().mySqrt(n) )

    return 



if __name__ == '__main__':

    test_bench()