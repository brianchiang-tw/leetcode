'''

Description:

X is a good number if after rotating each digit individually by 180 degrees, we get a valid number that is different from X.  Each digit must be rotated - we cannot choose to leave it alone.

A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves; 2 and 5 rotate to each other; 6 and 9 rotate to each other, and the rest of the numbers do not rotate to any other number and become invalid.

Now given a positive number N, how many numbers X from 1 to N are good?

Example:
Input: 10
Output: 4
Explanation: 
There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.
Note:

N  will be in range [1, 10000].

'''


class Solution:
    def rotatedDigits(self, N: int) -> int:
        
        counter = 0
        for i in range(1, N+1):
            
            # convert number i to digit character array
            str_num_list = list( str(i) )
            
            # flag for good number judgement
            is_good_number = False
            
            for digit in str_num_list:
                
                if digit in {'3','4','7'}:
                    # invalid number after rotation
                    is_good_number = False
                    break
                elif digit in {'2','5','6','9'}:
                    is_good_number = True
                    
                    
            if is_good_number:
                # update conter for good number
                counter += 1
                    
            
        return counter



# n : input value of N

## Time Complexity: O( n log n )
#
# The overhead in time is the outer for loop and inner for loop.
# The outer for loop, iterating on i, takes O( n )
# The inner for loop, iterating on digit, takes O( log n )
# It takes O( n log n ) in total

## Space Complexity: O( log n )
#
# The overhead in space is the storage for buffer, str_num_list, which is of O( log n )


def test_bench():

    test_data = [10,20,30,50,100]

    # expected output:
    '''
    4
    9
    15
    16
    40
    '''


    for n in test_data:

        print( Solution().rotatedDigits(n) )
    
    return 



if __name__ == '__main__':

    test_bench()