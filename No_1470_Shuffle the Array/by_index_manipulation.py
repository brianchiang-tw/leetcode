'''

Description:

Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].

 

Example 1:

Input: nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7] 
Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].



Example 2:

Input: nums = [1,2,3,4,4,3,2,1], n = 4
Output: [1,4,2,3,3,2,4,1]



Example 3:

Input: nums = [1,1,2,2], n = 2
Output: [1,2,1,2]
 

Constraints:

1 <= n <= 500
nums.length == 2n
1 <= nums[i] <= 10^3

'''



from typing import List
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:

        output = []
        
        for i in range(n):
            
            output.append( nums[i] )
            output.append( nums[i+n] )
        
        return output



# n : the value of input parameter, n

## Time Complexity: O( n )
#
# The overhead in time is the cost of for loop iteration, which are of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the storage for output list, which is of O( n ).


import unittest
class Testing( unittest.TestCase ):

    def test_case_1(self):

        result = Solution().shuffle( nums = [2,5,1,3,4,7], n = 3 )
        self.assertEqual(result,  [2,3,5,4,1,7] )



    def test_case_2(self):
    
        result = Solution().shuffle( nums = [1,2,3,4,4,3,2,1], n = 4 )
        self.assertEqual(result,  [1,4,2,3,3,2,4,1] )



    def test_case_3(self):
    
        result = Solution().shuffle( nums = [1,1,2,2], n = 2 )
        self.assertEqual(result, [1,2,1,2] )



if __name__ == '__main__':

    unittest.main()
