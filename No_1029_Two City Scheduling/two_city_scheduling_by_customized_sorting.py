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



'''
Example explanation:
costs = [ [10,20], [30,200], [400,50], [30,20] ]

Step_#1:
Define change_cost for person i = costs[i][0] - costs[i][1] 

change_cost = [ -10, -170, 350, 10]

If change_cost is > 0 or relative large than others, then person i should go city B to minimize the overall cost of travel
If change_cost is < 0 or relative small than others, then person i should go city A to minimize the overall cost of travel



Step_#2:
Sort input by change_cost with ascending order.

costs = [ [30,200], [10,20], [30,20], [400,50] ]



Step_#3:
Those N people on the head should go to city A, 
while other N people on the tail should to to city B.

decision = [ go A, go A, go B, go B ]



Step_#4:
Compute the minumum cost.
minimum cost to fly = 30 + 10 + 20 + 50 = 110
'''


from typing import List
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        
        # customized sorting with key = change_cost, on ascending order
        costs.sort( key = lambda x:x[0]-x[1])
        
        size = len(costs)
        
        # Those N people on the head should go to city A
        cost_of_go_to_A = sum ( [ costs[i][0] for i in range(size//2) ] )
        
        # Other N people on the tail should to to city B.
        cost_of_go_to_B = sum( [ costs[i][1] for i in range(size//2, size) ] )
        
        return cost_of_go_to_A + cost_of_go_to_B



# n : the length of input list, costs.

## Time Complexity: O( n log n ) on average, O( n ^ 2 ) on worst case
#
# The overhead in time is the cost of sorting, 
# which is O( n log n ) on average, O( n ^ 2 ) on worst case.


## Space Complexity: O( n )
#
# The overhead in space is the storage for list, cost_of_go_to_A and cost_of_go_to_A,
# which are of O( n )



def test_bench():

    test_data = [
                    [[10,20],[30,200],[400,50],[30,20]],
                    [[90,20],[70,30],[60,80],[40,50]]
                ]

    # expected output:
    '''
    110
    150
    '''

    for sequence in test_data:

        print( Solution().twoCitySchedCost(sequence) )
    
    return 



if __name__ == '__main__':

    test_bench()