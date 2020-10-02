'''

Description:

There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.

Note:

If there exists a solution, it is guaranteed to be unique.
Both input arrays are non-empty and have the same length.
Each element in the input arrays is a non-negative integer.



Example 1:

Input: 
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]

Output: 3

Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.



Example 2:

Input: 
gas  = [2,3,4]
cost = [3,4,3]

Output: -1

Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.

'''


from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        

        if sum(gas) < sum(cost): 
            # Quick rejection:
            # impossible to traverl, because total gas is smaller than total cost
            return -1
        
        n = len(gas)
        fuel_gain = 0
        stationIndex = 0
        
        for i in range(n):
            
            if gas[i] + fuel_gain < cost[i]: 
                
                # fail at current station i, try next one
                stationIndex = i+1
                fuel_gain = 0
                
            else:
                # success at current station, keep moving
                fuel_gain += (gas[i] - cost[i])
                
        return stationIndex        


# n : the length of input array, gas.

## Time Complexity: O( n )
#
# The overhead in time is the cost of for-loop iteration, which is of O( n )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for loop index and temporary variable, which is of O( 1 )



import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().canCompleteCircuit( gas  = [1,2,3,4,5], cost = [3,4,5,1,2] )
        self.assertEqual(result, 3)


    def test_case_2( self ):

        result = Solution().canCompleteCircuit( gas  = [2,3,4], cost = [3,4,3] )
        self.assertEqual(result, -1)


if __name__ == '__main__':

    unittest.main()