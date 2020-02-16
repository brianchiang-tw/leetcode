'''

Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

'''



from collections import deque

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        digits_1 = list( map(int, num1) )
        
        digits_2 = list( map(int, num2) )
        
        digit_length = max( len(digits_1), len(digits_2) )
        
        # a doubly linked list of integer to store summation
        summation = deque()
        
        carry_in = 0
        
        # Add digit by digit, from right to left
        for _ in range(digit_length):
            
            
            LSB_a = digits_1.pop() if digits_1 else 0
            LSB_b = digits_2.pop() if digits_2 else 0
            
            s = LSB_a + LSB_b + carry_in
			
			# update carry in and digit sum
            carry_in, digit_sum = divmod(s, 10)
            
			# append digit sum to summation
            summation.appendleft( digit_sum )
            
            
        # Check last carry in
        if carry_in:
            summation.appendleft( carry_in )
        
        
        # convert list of integer to string
        return ''.join( map(str,summation) )



# m : the value of num1
# n : the value of num2

## Time Complexity: O( log(max(m,n) ) )
#
# The overhead in time is the for loop, iterating on digit_length, which is of O( log(max(m,n) ) ).

## Space Complexity: O( log(max(m,n) ) )
#
# The overhead in space is the storage for summation digit list, summation, which is of O( log(max(m,n) ) ).


def test_bench():

    test_data = [
                    ("0", "0"),
                    ("3", "9"),
                    ("1", "99"),
                    ("6", "189"),
                    ("2", "999")
                ]

    # expected output:
    '''
    0
    12
    100
    195
    1001    
    '''

    for a, b in test_data:

        print( Solution().addStrings(a, b) )
    
    return



if __name__ == '__main__':

    test_bench()