'''

Description:

There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0], and the cost of flying the i-th person to city B is costs[i][1].

Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.

 

Example 1:

Input: [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation: 
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
 

Note:

1 <= costs.length <= 100
It is guaranteed that costs.length is even.
1 <= costs[i][0], costs[i][1] <= 1000


'''



from typing import List

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        # sort by transition coast: cost to A - cost to B
        costs.sort( key = lambda cost: cost[0]-cost[1] )
        
        size = len(costs)
        
        # compute the optimal cost of travel
        return sum( costs[i][0] if i < (size // 2) else costs[i][1] for i in range(size) )



from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'cost_array')


# n : the length of input array, costs.

## Time Complexity: O( n log n )
#
# The overhead in time is the cost of sorting, which is of O( n log n ).

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for temporary variable, which is of O( 1 ).

def test_bench():

    test_data = [
                    TestEntry( cost_array = [[10,20],[30,200],[400,50],[30,20]] ),
                    TestEntry( cost_array = [[70,20],[250,200],[10,50],[5,20]] ),
                ]

    # expected output:
    '''
    110
    235
    '''

    for t in test_data:

        print( Solution().twoCitySchedCost(*t) )
    
    return



if __name__ == '__main__':

    test_bench()