'''

Description:

In a country popular for train travel, you have planned some train travelling one year in advance.  The days of the year that you will travel is given as an array days.  Each day is an integer from 1 to 365.

Train tickets are sold in 3 different ways:

a 1-day pass is sold for costs[0] dollars;
a 7-day pass is sold for costs[1] dollars;
a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.  For example, if we get a 7-day pass on day 2, then we can travel for 7 days: day 2, 3, 4, 5, 6, 7, and 8.

Return the minimum number of dollars you need to travel every day in the given list of days.

 

Example 1:

Input: days = [1,4,6,7,8,20], costs = [2,7,15]
Output: 11
Explanation: 
For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
In total you spent $11 and covered all the days of your travel.
Example 2:

Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
Output: 17
Explanation: 
For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1, 2, ..., 30.
On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
In total you spent $17 and covered all the days of your travel.
 

Note:

1 <= days.length <= 365
1 <= days[i] <= 365
days is in strictly increasing order.
costs.length == 3
1 <= costs[i] <= 1000

'''


from typing import List

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        # index of ticket
        _1day_pass, _7day_pass, _30day_pass = 0, 1, 2
        
        # Predefined constant to represent not-traverling day
        NOT_Traveling_Day = -1
        
        # DP Table, record for minimum cost of ticket to travel
        dp_cost = [NOT_Traveling_Day for _ in range(366)]
        
        
        # base case:
        # no cost before travel
        dp_cost[0] = 0
        
        for day in days:
            
            # initialized to 0 for traverling days
            dp_cost[day] = 0
            
        
        
        # Solve min cost by Dynamic Programming
        for day_i in range(1, 366):
            
            if dp_cost[day_i] == NOT_Traveling_Day:
                
                # today is not traveling day
                # no extra cost
                dp_cost[day_i] = dp_cost[day_i - 1]
            
            
            else:
                
                # today is traveling day
                # compute optimal cost by DP
                
                dp_cost[day_i] = min(   dp_cost[ day_i - 1 ]  + costs[ _1day_pass ],
                                        dp_cost[ max(day_i - 7, 0) ]  + costs[ _7day_pass ],
                                        dp_cost[ max(day_i - 30, 0) ] + costs[ _30day_pass ]     )
        
        
        # Cost on last day of this year is the answer
        return dp_cost[365]



## Time Complexity: O( 366 ) = O( 1 )
#
# The overhead in time is the cost of for-loop iteration, which is of O( 366 ) = O( 1 )

## Space Complexity: O( 366 ) = O( 1 )
#
# The overhead in time is the storage for dynamic programming table, dp_cost, which is of O( 366 ) = O( 1 )


import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().mincostTickets(days=[1,4,6,7,8,20], costs=[2,7,15])
        self.assertEqual(result, 11)
    
    
    def test_case_2( self ):

        result = Solution().mincostTickets(days=[1,2,3,4,5,6,7,8,9,10,30,31], costs=[2,7,15])
        self.assertEqual(result, 17)



if __name__ == '__main__':

    unittest.main()