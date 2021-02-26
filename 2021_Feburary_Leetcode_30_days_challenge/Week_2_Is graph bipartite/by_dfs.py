'''

Description:

There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:

There are no self-edges (graph[u] does not contain u).
There are no parallel edges (graph[u] does not contain duplicate values).
If v is in graph[u], then u is in graph[v] (the graph is undirected).
The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.
A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

Return true if and only if it is bipartite.

 

Example 1:


Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
Output: false
Explanation: There is no way to partition the nodes into two independent sets such that every edge connects a node in one and a node in the other.
Example 2:


Input: graph = [[1,3],[0,2],[1,3],[0,2]]
Output: true
Explanation: We can partition the nodes into two sets: {0, 2} and {1, 3}.
 

Constraints:

graph.length == n
1 <= n <= 100
0 <= graph[u].length < n
0 <= graph[u][i] <= n - 1
graph[u] does not contain u.
All the values of graph[u] are unique.
If graph[u] contains v, then graph[v] contains u.

'''

from typing import List
from collections import defaultdict

class Solution():

    def isBipartite(self, graph: List[ List[int]]) -> bool:
        # Constant defined color color drawing to nodes
        NOT_COLORED, BLUE, GREEN = 0, 1, -1

        # ---------------------------------------
        def helper( node_id, color):

            # Draw node_is as color
            color_table[ node_id] = color

            for neighbor in adj_table[ node_id ]:

                if color_table[ neighbor ] == color:
                    # neighbor has the same color of current node_id
                    # Reject due to breaking the definition ot bipartite
                    return False
            
                if color_table[ neighbor ] == NOT_COLORED and ( not helper(neighbor, -color) ):
                    return False
            
            return True

        # ---------------------------------------

        size = len(graph)

        # each node maintain a list of neighbor nodes
        adj_table = defaultdict( list )

        # each node maintain a record for color
        color_table = defaultdict( int )

        # update adj table for each node from input graph
        for node_idx, adj_list in enumerate(graph):

            adj_table[ node_idx ] = adj_list

        
        # Try to draw two nodes with two different colors in DFS, under the definition of bipartite
        for node_idx in range( size ):

            if color_table[ node_idx ] == NOT_COLORED and ( not helper(node_idx, BLUE) ):
                
                # Impossible to make bipartition
                return False 
        
        return True


# V : number of nodes
# E : number of edges 

## Time Complexity: O( V + E )
#
# The overhead in time is the cost of DFS, which is of O( V + E )

## Space Complexity: O( V + E )
#
# The overhead in space is the storage of DFS, which is of O( V + E )


import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().isBipartite( graph=[[1,2,3],[0,2],[0,1,3],[0,2]] )
        self.assertEqual(result, False)

    
    def test_case_2( self ):

        result = Solution().isBipartite( graph= [[1,3],[0,2],[1,3],[0,2]] )
        self.assertEqual(result, True)


if __name__ == '__main__':

    unittest.main()        