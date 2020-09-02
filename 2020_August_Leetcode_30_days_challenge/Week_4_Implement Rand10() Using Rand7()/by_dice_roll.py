'''

Description:

Given the API rand7 which generates a uniform random integer in the range 1 to 7, write a function rand10 which generates a uniform random integer in the range 1 to 10. You can only call the API rand7 and you shouldn't call any other API. Please don't use the system's Math.random().

Notice that Each test case has one argument n, the number of times that your implemented function rand10 will be called while testing. 

Follow up:

What is the expected value for the number of calls to rand7() function?
Could you minimize the number of calls to rand7()?
 

Example 1:

Input: n = 1
Output: [2]
Example 2:

Input: n = 2
Output: [2,8]
Example 3:

Input: n = 3
Output: [3,8,10]
 

Constraints:

1 <= n <= 105

'''


# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        
        
        while True:
		
			# generate a random number from 1 ~ 49 with uniform distribution
            random_num = ( rand7() - 1 ) * 7 + rand7()
            
            if random_num <= 40:
			
			    # map 1 ~ 40 to 1 ~ 10 by modulo operation with offset
                return random_num % 10 + 1


# The output of this challenge is random, therefore local test bench is not proviede here.                