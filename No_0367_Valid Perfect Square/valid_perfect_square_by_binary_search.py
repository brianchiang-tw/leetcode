'''

Description:

Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true



Example 2:

Input: 14
Output: false

'''



class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        if num == 1:
            # Corner case handle:
            return True
        
        lower, upper = 1, num//2
        
        while lower <= upper:
            
            mid = (lower + upper) // 2
            square = mid ** 2
            
            if square == num:
                # Accept:
                # num is perfect square
                return True
            elif square > num:
                upper = mid - 1
            else:
                lower = mid + 1

        # Reject:
        # num is not a perfect square
        return False



# n : the input value of num.

## Time Complexity: O( log n )
#
# The overhead in time is the cost of binary search, which is of O( log n ).

## Space Complexity: O( 1 )
#
# The overhead in space is the looping index and temporary arithmetic variable, which is of O( 1 ).


def test_bench():

    #                           expected output:
    test_data = [
                    16,         # True
                    14,         # False
                    24,         # False
                    25,         # True
                    26,         # False
                    35,         # False
                    36,         # True
                    37,         # False
                    1024,       # True
                    2147483647  # False
                ]

    for number in test_data:

        print( Solution().isPerfectSquare(number) )
    
    return 



if __name__ == '__main__':

    test_bench()