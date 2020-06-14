'''

Description:

There are n cities connected by m flights. Each flight starts from city u and arrives at v with a price w.

Now given all the cities and flights, together with starting city src and the destination dst, your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.

Example 1:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
Output: 200
Explanation: 
The graph looks like this:


The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.
Example 2:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0
Output: 500
Explanation: 
The graph looks like this:


The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.
 

Constraints:

The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1.
The size of flights will be in range [0, n * (n - 1) / 2].
The format of each flight will be (src, dst, price).
The price of each flight will be in the range [1, 10000].
k is in the range of [0, n - 1].
There will not be any duplicated flights or self cycles.

'''


from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        
        price_table = [ float('inf') for _ in range(n) ]
        
        # price of source must be 0
        price_table[ src ] = 0
		
        # initialization with 0 transfer
        for source, destination, ticket_price in flights:
            if source == src:
                price_table[destination] = ticket_price
        
        
        # tranfer k times to update price table
        for trasfer in range(0, K):
            
            current_price = [*price_table]
            
            for source, destination, ticket_price in flights:
                
                current_price[destination] = min(current_price[destination], price_table[source] + ticket_price )
            
            # update current price back to price table    
            price_table = current_price
        
        
        if price_table[dst] == float('inf'):
            return -1
        else:
            return price_table[dst]



# k : the value of transfer, of O( n )
# f : the list of flights, of O( n^2 )



## Time Complexity: O( k*f ) = O( n^3 )
#
# The overhead in time is the cost of nested loop, which is of O( n^3 )

## Space Complexity: O( n )
#
# The overhead in space is the storage for temporary list, current_price, which is of O( n )

import unittest
from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'n edges src dest k')



class Testing(unittest.TestCase):

    def test_case_1(self):
        t = TestEntry( n = 3, edges =  [[0,1,100],[1,2,100],[0,2,500]], src = 0, dest = 2, k = 1 )
        result = Solution().findCheapestPrice( *t )

        # expected output: 200
        self.assertEqual(result, 200)

    def test_case_2(self):
        t = TestEntry( n = 3, edges =  [[0,1,100],[1,2,100],[0,2,500]], src = 0, dest = 2, k = 0 )
        result = Solution().findCheapestPrice( *t )

        # expected output: 500
        self.assertEqual(result, 500)


    def test_case_3(self):
        t = TestEntry( n = 4, edges = [[0,1,1],[0,2,5],[1,2,1],[2,3,1]], src = 0, dest = 3, k = 1)
        result = Solution().findCheapestPrice( *t )

        # expected output: 6
        self.assertEqual(result, 6)



if __name__ == '__main__':
    
    unittest.main()