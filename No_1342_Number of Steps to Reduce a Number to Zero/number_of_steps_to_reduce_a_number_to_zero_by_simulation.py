'''

Description:

Given a non-negative integer num, return the number of steps to reduce it to zero. If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

 

Example 1:

Input: num = 14
Output: 6
Explanation: 
Step 1) 14 is even; divide by 2 and obtain 7. 
Step 2) 7 is odd; subtract 1 and obtain 6.
Step 3) 6 is even; divide by 2 and obtain 3. 
Step 4) 3 is odd; subtract 1 and obtain 2. 
Step 5) 2 is even; divide by 2 and obtain 1. 
Step 6) 1 is odd; subtract 1 and obtain 0.



Example 2:

Input: num = 8
Output: 4
Explanation: 
Step 1) 8 is even; divide by 2 and obtain 4. 
Step 2) 4 is even; divide by 2 and obtain 2. 
Step 3) 2 is even; divide by 2 and obtain 1. 
Step 4) 1 is odd; subtract 1 and obtain 0.



Example 3:

Input: num = 123
Output: 12
 

Constraints:

0 <= num <= 10^6

'''



class Solution:

    def numberOfSteps (self, num: int) -> int:
        
        
        step = 0
        while num != 0 :
            
            step += 1
            
            if num & 1 == 1:
                # odd number, subtract by 1
                num -= 1

            else:
                # even number, divide by 2 <=> right shift one bit
                num >>= 1
        
        return step



# n : the value of input num

## Time Complexity: O( log n )
#
# The overhead in time is the while loop iterating on num, which is of O( log n )

## Space Complexity: O( 1 )
# 
# The overhead in space is the storage for counter step.


def test_bench():

    test_data = [14, 8, 123]

    # expected output:
    '''
    6
    4
    12
    '''

    for n in test_data:

        print( Solution().numberOfSteps(n) )

    return 



if __name__ == '__main__':

    test_bench()