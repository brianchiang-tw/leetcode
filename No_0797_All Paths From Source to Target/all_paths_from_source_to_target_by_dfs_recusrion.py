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
        
        # last index is the destination
        self.dest = len(graph)-1

        # record of all paths from start to destination
        self.path = []
        
        # DFS traversal
        def dfs( node_index, tracking ):
            
            # Base case:
            # Destination is reached
            if node_index == self.dest:
                self.path.append( tracking + [node_index] )
                return
            
            # Visit each neighbor
            for neighbor_index in graph[node_index]:
                dfs( neighbor_index, tracking + [node_index] )
            
        
        # start from node_#0
        dfs( 0, [] )
        
        return self.path

    




# n : the number of nodes in graph

## Time Complexity: O( n^2 * 2^n )
#
# There are O(n^2) edge at most in directed, acyclic graph.
# And there are 2^n possible choice of n nodes.
#
# It takes O( n^2 * 2^n ) in total.


## Space Complexity: O( n * 2^n )
#
# There are at most O(n) possible path from source to destination, in directed acyclic graph.
# And there are 2^n possible choice of n nodes.
#
# It takes O( n * 2^n ) in total.


def test_bench():

    test_data = [
                    [[1,2], [3], [3], []] 
                ]

    # expected output:
    '''
    [[0, 2, 3], [0, 1, 3]]
    '''
    for adjacency_list in test_data:

        print( Solution().allPathsSourceTarget(adjacency_list) )

    return 



if __name__ == '__main__':

    test_bench()