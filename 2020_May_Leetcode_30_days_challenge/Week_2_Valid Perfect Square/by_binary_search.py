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
            # Quick response for base case
            return True
        
        left, right = 0, num//2
        
        # Use binary search to find the square root
        while left <= right:
            
            mid = left + (right-left)//2
            
            square_of_mid = mid**2
            
            if square_of_mid == num:
                return True
            
            elif square_of_mid < num:
                left = mid+1
                
            else:
                right = mid-1
                
        return False



# n : the value of input number, num

## Time Complexity: O( log n )
#
# The overhead in time is the cost of binary search, which is of O( log n ).

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for loop index, which is of O( 1 )



def test_bench():

    test_data = [
                    1,2,3,4,8,9,10,24,25,26,1023,1024,1025
                ]

    # expected output:
    '''
    True
    False
    False
    True
    False
    True
    False
    False
    True
    False
    False
    True
    False
    '''

    for number in test_data:

        print( Solution().isPerfectSquare( num = number ) )

    return



if __name__ == '__main__':

    test_bench()        