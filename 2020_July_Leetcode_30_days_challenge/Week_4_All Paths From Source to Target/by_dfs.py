'''

Description:

Given a directed, acyclic graph of N nodes.  Find all possible paths from node 0 to node N-1, and return them in any order.

The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.  graph[i] is a list of all nodes j for which the edge (i, j) exists.


Example:

Input: [[1,2], [3], [3], []] 
Output: [[0,1,3],[0,2,3]] 

Explanation: The graph looks like this:
0--->1
|    |
v    v
2--->3
There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.



Note:

The number of nodes in the graph will be in the range [2, 15].
You can print different paths in any order, but you should keep the order of nodes inside one path.

'''


from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        self.dest = len(graph)-1

        self.path = []

        # ------------------------------------------------------
        def dfs(node_index, tracking):

            if node_index == self.dest:
                self.path.append( tracking + [node_index] )
            
            for neighbor_idx in graph[node_index]:
                dfs(neighbor_idx, tracking + [node_index] )

        # ------------------------------------------------------

        dfs( node_index=0, tracking=[] )

        return self.path


# V: the number of vertices in graph
# E: the number of edges in graph

## Time Complexity: O( V + E )
#
# The overhead in time is the cost of DFS, which is of O( V + E )

## Space Complexity: O( V + E　)
#
# The overhead in space is the storage of recursion depth, which is of O( V + E )




import unittest
class Testing(unittest.TestCase):

    def test_case_1( self ):

        result = Solution().allPathsSourceTarget( graph= [[1,2], [3], [3], []] )
        self.assertCountEqual(result, [[0,1,3],[0,2,3]] )



if __name__ == '__main__':

    unittest.main()