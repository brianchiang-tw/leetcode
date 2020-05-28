'''

Description:

Given an undirected graph, return true if and only if it is bipartite.

Recall that a graph is bipartite if we can split it's set of nodes into two independent subsets A and B such that every edge in the graph has one node in A and another node in B.

The graph is given in the following form: graph[i] is a list of indexes j for which the edge between nodes i and j exists.  Each node is an integer between 0 and graph.length - 1.  There are no self edges or parallel edges: graph[i] does not contain i, and it doesn't contain any element twice.



Example 1:
Input: [[1,3], [0,2], [1,3], [0,2]]
Output: true
Explanation: 
The graph looks like this:
0----1
|    |
|    |
3----2
We can divide the vertices into two groups: {0, 2} and {1, 3}.



Example 2:
Input: [[1,2,3], [0,2], [0,1,3], [0,2]]
Output: false
Explanation: 
The graph looks like this:
0----1
| \  |
|  \ |
3----2
We cannot find a way to divide the set of nodes into two independent subsets.
 

Note:

graph will have length in range [1, 100].
graph[i] will contain integers in range [0, graph.length - 1].
graph[i] will not contain i or duplicate values.
The graph is undirected: if any element j is in graph[i], then i will be in graph[j].

'''


from typing import List
from collections import defaultdict

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        # Constant defined for color drawing to nodes
        NOT_COLORED, BLUE, GREEN = 0, 1, -1
        
        # -------------------------------------------
        
        def helper( node_id, color ):
            
            # Draw node_id as color
            color_table[ node_id ] = color
            
            for neighbor in adj_table[ node_id ]:
                
                if color_table[ neighbor ] == color:
                    # neighbor has the same color of current node_id
                    # Reject due to breaking the definition of bipartite
                    return False
                
                if color_table[ neighbor ] == NOT_COLORED and ( not helper(neighbor, -color) ):
                    # other nodes can not be colored with the definition of bipartite
                    return False
            
            return True
        # --------------------------------------------
        
        size = len(graph)
        
        # each node maintain a list of neighbor nodes
        adj_table = defaultdict( list )
        
        # each node maintain a record for color
        color_table = [ NOT_COLORED for _ in range(size) ]
        
        # update adj table for each node from input graph
        for node_idx, adj_list in enumerate(graph):
            adj_table[ node_idx ] = adj_list
        
        
        
        
        bipartition_with_two_color = True
        
        # Try to draw nodes with two different colors in DFS, under the definition of bipartite
        for node_idx in range(0, size):
            
            if color_table[ node_idx ] == NOT_COLORED and ( not helper(node_idx, BLUE) ):
                    bipartition_with_two_color = False
                    break
        
        
        return bipartition_with_two_color



# V : the number of nodes in graph
# E : the number of edges in graph

## Time Complexity: O( V + E )
#
# The overhead in time is the cost of DFS, which is of O( V + E)

## Space Complexity: O( V + E )
#
# The overhead in space is the storage for recursion call stack, which is of O( V + E )



from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'adjacency_list')

def test_bench():

    test_data = [
                    TestEntry( adjacency_list = [[1,3], [0,2], [1,3], [0,2]] ),
                    TestEntry( adjacency_list = [[1,2,3], [0,2], [0,1,3], [0,2]] ),
                ]


    # expected output:
    '''
    True
    False
    '''

    for t in test_data:
        
        print( Solution().isBipartite( graph = t.adjacency_list) )
    
    return



if __name__ == '__main__':

    test_bench()