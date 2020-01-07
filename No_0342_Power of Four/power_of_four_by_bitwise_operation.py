'''

Description:

Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

Input: 16
Output: true
Example 2:

Input: 5
Output: false
Follow up: Could you solve it without loops/recursion?

'''



class Solution:
    def isPowerOfFour(self, num):
        
        if num < 1: 
            return False
        
        elif num ==1 : 
            return True
        
        else:
            # Capture all (2^n)^k, by num & (num-1) == 0
            # Then screen out those numbers which are exact power of two by 0xAAAAAAAA mask
            # Finally, we have number of (2^n)^k, where k >= 2
            return num & (num-1) == 0 and num & 0xaaaaaaaa == 0