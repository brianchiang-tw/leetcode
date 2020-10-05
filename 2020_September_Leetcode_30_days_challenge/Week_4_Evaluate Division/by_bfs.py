'''

Description:

You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

 

Example 1:

Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]



Example 2:

Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]



Example 3:

Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]
 

Constraints:

1 <= equations.length <= 20
equations[i].length == 2
1 <= Ai.length, Bi.length <= 5
values.length == equations.length
0.0 < values[i] <= 20.0
1 <= queries.length <= 20
queries[i].length == 2
1 <= Cj.length, Dj.length <= 5
Ai, Bi, Cj, Dj consist of lower case English letters and digits.

'''


from collections import defaultdict
class Solution:
    def calcEquation(self, equations, values, queries):

        G = defaultdict(dict)

        for (x, y), v in zip(equations, values):
            G[x][y] = v
            G[y][x] = 1/v
            
        def bfs(src, dst):
            if not (src in G and dst in G): return -1.0
            
            q, seen = [(src, 1.0)], set()
            
            # BFS
            for x, v in q:

                if x == dst: 
                    # stop condition
                    return v
                
                seen.add(x)

                # scan each neighbor
                for y in G[x]:
                    if y not in seen: 
                        q.append((y, v*G[x][y]))
                        
            return -1.0

        return [bfs(s, d) for s, d in queries]



# e : the length of equations
# q : the length of queries

## Time Complexity: O( q * e )
#
# The overhead in time is the cost of O( q ) * the cost of BFS = O( q * e)

## Space Complexity: O( e )
#
# The overhead in space is the storage for traversal queue, which is of O( e )


import unittest

class Testing( unittest.TestCase ):

    def test_case_1(self):

        result = Solution().calcEquation( equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]] )
        self.assertEqual(result, [6.00000,0.50000,-1.00000,1.00000,-1.00000] )


    def test_case_2(self):

        result = Solution().calcEquation( equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]] )
        self.assertEqual(result, [3.75000,0.40000,5.00000,0.20000] )


    def test_case_3(self):

        result = Solution().calcEquation( equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]] )
        self.assertEqual(result, [0.50000,2.00000,-1.00000,-1.00000] )



if __name__ == '__main__':

    unittest.main()