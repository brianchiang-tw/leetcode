'''

Description:

Given an integer array arr, and an integer target, return the number of tuples i, j, k such that i < j < k and arr[i] + arr[j] + arr[k] == target.

As the answer can be very large, return it modulo 109 + 7.

 

Example 1:

Input: arr = [1,1,2,2,3,3,4,4,5,5], target = 8
Output: 20
Explanation: 
Enumerating by the values (arr[i], arr[j], arr[k]):
(1, 2, 5) occurs 8 times;
(1, 3, 4) occurs 8 times;
(2, 2, 4) occurs 2 times;
(2, 3, 3) occurs 2 times.



Example 2:

Input: arr = [1,1,2,2,2,2], target = 5
Output: 12
Explanation: 
arr[i] = 1, arr[j] = arr[k] = 2 occurs 12 times:
We choose one 1 from [1,1] in 2 ways,
and two 2s from [2,2,2,2] in 6 ways.
 

Constraints:

3 <= arr.length <= 3000
0 <= arr[i] <= 100
0 <= target <= 300

'''

from typing import List
from collections import Counter

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        
        ## dictionary
        # key : distinct number
        # value : occurrence of distinct number
        counts = Counter(arr)
        
        # total method count, and modulo constant
        result, constant = 0, (10 ** 9 + 7)
        
        
        # find the method count where i + j + k = target
        # all numbers are bounded in interval [0, 100]
        
        for i in range(101):
            
            if counts[i] == 0:
                
                # number i doesn't show up in input array
                continue
                
            j, k = i, 100
            
            # find j, k with two-pointers
            while j <= k:
                
                if j + k > target - i:
				
					# j + k is too large, try to make it smaller
                    k -= 1
                    
                elif j + k < target - i:
				
					# j + k is too small, try to make it larger
                    j += 1
                    
                else:
                    
                    # update result with different combination cases
                    
                    if i == j == k:
                        
                        # all repeated: (i, j, k) = (i, i, i)
                        result += counts[i] * (counts[i] - 1) * (counts[i] - 2) // 6
                        
                    elif i == j:
                        # i, j repeated: (i, j, k) = (i, i, k)
                        result += counts[i] * (counts[i] - 1) * counts[k] // 2
                        
                    elif j == k:
                        # i, k repeated: (i, j, k) = (i, j, j)
                        result += counts[i] * counts[j] * (counts[j] - 1) // 2
                        
                    else:
                        # all distinct: (i, j, k)
                        result += counts[i] * counts[j] * counts[k]
                    
                    
                    # update two pointers for j, k
                    j += 1
                    k -= 1
                    
        return result % constant



## n : the length of inpu array 

## Time Compleity: O( n )
#
# The overhead in time is the cost of nested loop with O( n ) * O( 100 ) = O( n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for dictionary, which is of O( n )


import unittest

class Testing( unittest.TestCase ):

    def setUp(self) -> None:
        self.solver = Solution().threeSumMulti

    def test_case_1( self ):

        result = self.solver( arr = [1,1,2,2,3,3,4,4,5,5], target = 8)
        self.assertEqual(result, 20)


    def test_case_1( self ):

        result = self.solver( arr = [1,1,2,2,2,2], target = 5)
        self.assertEqual(result, 12)


if __name__ == '__main__':

    unittest.main()