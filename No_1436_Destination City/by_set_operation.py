'''

Description:

You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.

It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.

 

Example 1:

Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
Output: "Sao Paulo" 
Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".



Example 2:

Input: paths = [["B","C"],["D","B"],["C","A"]]
Output: "A"
Explanation: All possible trips are: 
"D" -> "B" -> "C" -> "A". 
"B" -> "C" -> "A". 
"C" -> "A". 
"A". 
Clearly the destination city is "A".



Example 3:

Input: paths = [["A","Z"]]
Output: "Z"
 

Constraints:

1 <= paths.length <= 100

paths[i].length == 2

1 <= cityAi.length, cityBi.length <= 10

cityAi != cityBi

All strings consist of lowercase and uppercase English letters and the space character.

'''


from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        
        all_cities = set()
        src_cities = set()
        
        # Update all cities and source cities
        for start_city, end_city in paths:
            all_cities.add( start_city )
            all_cities.add( end_city )
            
            src_cities.add( start_city )
        
        # Destination city never shows up in source cities
        # The only element remains in the difference set is the destination city
        return (all_cities - src_cities).pop()



# n : the length of input paths

## Time Complexity: O( n )
#
# The overhead in time is the cost of set building, which is of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the storage for sets, which are of O( n ).


from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'paths')

def test_bench():

    test_data = [
                    TestEntry( paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]] ),
                    TestEntry( paths = [["B","C"],["D","B"],["C","A"]] ),
                    TestEntry( paths = [["A","Z"]] ),
                ]

    # expected output:
    '''
    Sao Paulo
    A
    Z
    '''

    for t in test_data:
        
        print( Solution().destCity( paths = t.paths ) )

    return



if __name__ == '__main__':

    test_bench()