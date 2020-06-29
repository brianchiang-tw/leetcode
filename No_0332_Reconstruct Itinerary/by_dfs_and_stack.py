'''

Description:

Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:

If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
One must use all the tickets once and only once.



Example 1:

Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]



Example 2:

Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]

Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
             But it is larger in lexical order.

'''


from typing import List
from bisect import insort
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        
        # each ticket maps to one source <-> destination flight
        src_dest_dict = defaultdict(list)
        
        # update fly map
        for src, dst in tickets:
		
			# update fly map with lexical order
            insort(src_dest_dict[src], dst)
        
        # record of traversal path
        traverse_stack = []
        
        def dfs(fly_map, airport):
            
            # keep flying if current journey has next flight
            while fly_map[airport]:
                
                # choose flight destination with lexical order
                next_airport = fly_map[airport][0]
				
				# remove selected flight from fly map
                fly_map[airport].remove(next_airport)
                
                # fly to next airport
                dfs(fly_map, next_airport)
            
            # current journey has no next flight anymore
            traverse_stack.append(airport)
        
        # -------------------------------------------------------
        
        # Start traverl from JFK with all ticket used exactly once (i.e., all edges visited exactly once)
        dfs(fly_map=src_dest_dict, airport="JFK")
        
        return [*reversed(traverse_stack)]


# n : the length of input list, tickets

## Time Complexity: O( n )
#
# The overhead in time is the cost of DFS, which is of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the storage for recursion call stack, which is of O( n ).



import unittest
class Testing( unittest.TestCase ):

    def test_case_1(self):

        result = Solution().findItinerary( tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]] )
        self.assertEqual( result, ["JFK", "MUC", "LHR", "SFO", "SJC"] )



    def test_case_2(self):

        result = Solution().findItinerary( tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]] )
        self.assertEqual( result, ["JFK","ATL","JFK","SFO","ATL","SFO"] )



    def test_case_3(self):
    
        result = Solution().findItinerary( tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]] )
        self.assertEqual( result, ["JFK","NRT","JFK","KUL"] )


if __name__ == '__main__':

    unittest.main()
