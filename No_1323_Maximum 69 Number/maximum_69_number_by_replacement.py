'''

Description:

Given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

 

Example 1:

Input: num = 9669
Output: 9969
Explanation: 
Changing the first digit results in 6669.
Changing the second digit results in 9969.
Changing the third digit results in 9699.
Changing the fourth digit results in 9666. 
The maximum number is 9969.



Example 2:

Input: num = 9996
Output: 9999
Explanation: Changing the last digit 6 to 9 results in the maximum number.



Example 3:

Input: num = 9999
Output: 9999
Explanation: It is better not to apply any change.
 

Constraints:

1 <= num <= 10^4
num's digits are 6 or 9.

'''



'''
---
Procedure:
Scan from MSB digit to LSB digit, **replace the leftmost 6 by 9 if 6 exists**.
Otherwise, return original input.

---

Example explanation

Example_#1: 

99**6**9 -> 99**9**9

---

Example_#2:

999**6** -> 999**9**

---

Example_3:

9999 -> 9999

---
'''



class Solution:
    def maximum69Number (self, num: int) -> int:
        
        str_list = list( str(num) )
        
        # scan from MSB digit to LSB digit
        for i, digit in enumerate(str_list):
            
            # replace the leftmost 6 by 9
            if digit == '6':
                str_list[i] = '9'
                
                # early return because we can replace one digit at most
                return ''.join( str_list )
        
        # no 6 in input, return the same
        return num



# n : the value of input num

## Time Complexity: O( log n )
#
# The overhead in time is the for loop iterating on (i, digit), 
# which is of the width of digits in decimal on O( log n )



## Space Complexity: O( log n)
#
# The overhead in space is the stroage for str_list, and string output, which is of O( log n)



def test_bench():
    
    test_data = [9969, 9996, 9999]

    # expected output:
    '''
    9999
    9999
    9999
    '''



    for number_of_69 in test_data:

        print( Solution().maximum69Number(number_of_69) )

    return 



if __name__ == '__main__':

    test_bench()