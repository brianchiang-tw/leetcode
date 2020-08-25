class Solution:
    def mySqrt(self, x: int) -> int:
        
        left, right = 0, x
        
        while left <= right:
            
            mid = left + (right - left) // 2
            square = mid ** 2
            
            if square <= x:
                left = mid + 1
            
            elif square > x :
                right = mid -1
            
        
        return left-1



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