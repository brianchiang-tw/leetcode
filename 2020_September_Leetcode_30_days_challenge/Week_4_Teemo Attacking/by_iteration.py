'''

Description:

In LOL world, there is a hero called Teemo and his attacking can make his enemy Ashe be in poisoned condition. Now, given the Teemo's attacking ascending time series towards Ashe and the poisoning time duration per Teemo's attacking, you need to output the total time that Ashe is in poisoned condition.

You may assume that Teemo attacks at the very beginning of a specific time point, and makes Ashe be in poisoned condition immediately.



Example 1:

Input: [1,4], 2
Output: 4
Explanation: At time point 1, Teemo starts attacking Ashe and makes Ashe be poisoned immediately. 
This poisoned status will last 2 seconds until the end of time point 2. 
And at time point 4, Teemo attacks Ashe again, and causes Ashe to be in poisoned status for another 2 seconds. 
So you finally need to output 4.
 
 

Example 2:

Input: [1,2], 2
Output: 3
Explanation: At time point 1, Teemo starts attacking Ashe and makes Ashe be poisoned. 
This poisoned status will last 2 seconds until the end of time point 2. 
However, at the beginning of time point 2, Teemo attacks Ashe again who is already in poisoned status. 
Since the poisoned status won't add up together, though the second poisoning attack will still work at time point 2, it will stop at the end of time point 3. 
So you finally need to output 3.
 

Note:

You may assume the length of given time series array won't exceed 10000.
You may assume the numbers in the Teemo's attacking time series and his poisoning time duration per attacking are non-negative integers, which won't exceed 10,000,000.

'''


from typing import List

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        
        output = 0
        n = len(timeSeries)
        
        if n == 0:
            # Quick response for empty attack time-series
            return 0
        
        
        # for the first attack
        output += duration
        
        # scan from second attack to last attack
        for i in range(1, n):
            
            time_gap = timeSeries[i] - timeSeries[i-1]
            
            if time_gap < duration:
                # has overlap between two attacks
                output += time_gap
                
            else:
                # no overlap between two attacks
                output += duration
                
        return output



# n : the length of timeSeries

## Time Complexity: O( n )
#
# The overhead in time is the cost of for-loop iteration, which is of O( n )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for loop index and temporary variable, which is of O( 1 )


import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().findPoisonedDuration( timeSeries=[1,4], duration=2 )
        self.assertEqual(result, 4)


    def test_case_2( self ):

        result = Solution().findPoisonedDuration( timeSeries=[1,2], duration=3 )
        self.assertEqual(result, 4)



if __name__ == '__main__':

    unittest.main()            