'''

Description:

On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
Note:
cost will have a length in the range [2, 1000].
Every cost[i] will be an integer in the range [0, 999].

'''


from typing import List
class Solution:
    
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # +1 for destination with cost 0
        size = len(cost)+1
        min_cost = [None] * ( size )
        
        min_cost[0] = cost[0]
        min_cost[1] = cost[1]
        
        for i in range(2, size):
            
            if i != size-1:
                min_cost[i] = min( min_cost[i-1], min_cost[i-2] ) + cost[i] 
            else:
                min_cost[i] = min( min_cost[i-1], min_cost[i-2] )
            
        return min_cost[size-1]



# n : the length of input cost list

## Time Complexity: O( n )
#
# The overhead in time is the for loop iterating from 2 to size, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is to maintain a min-cost table, which is of O( n )



def test_bench():

    test_data = [
                    [10, 15, 20],
                    [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
                ]


    # expected output:
    '''
    15
    6
    '''

    for cost_table in test_data:

        print( Solution().minCostClimbingStairs(cost_table) )

    return 



if __name__ == '__main__':

    test_bench()