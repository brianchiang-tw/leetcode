'''

Description:

A frog is crossing a river. The river is divided into x units and at each unit there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.

Given a list of stones' positions (in units) in sorted ascending order, determine if the frog is able to cross the river by landing on the last stone. Initially, the frog is on the first stone and assume the first jump must be 1 unit.

If the frog's last jump was k units, then its next jump must be either k - 1, k, or k + 1 units. Note that the frog can only jump in the forward direction.

Note:

The number of stones is ≥ 2 and is < 1,100.
Each stone's position will be a non-negative integer < 231.
The first stone's position is always 0.



Example 1:

[0,1,3,5,6,8,12,17]

There are a total of 8 stones.
The first stone at the 0th unit, second stone at the 1st unit,
third stone at the 3rd unit, and so on...
The last stone at the 17th unit.

Return true. The frog can jump to the last stone by jumping 
1 unit to the 2nd stone, then 2 units to the 3rd stone, then 
2 units to the 4th stone, then 3 units to the 6th stone, 
4 units to the 7th stone, and 5 units to the 8th stone.



Example 2:

[0,1,2,3,4,8,9,11]

Return false. There is no way to jump to the last stone as 
the gap between the 5th and 6th stone is too large.

'''



from collections import deque
from typing import List
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        
        stone_set = set( stones )
        destination = stones[-1]
        visited = set()
        
        traversal_queue = deque()

        if 1 not in stone_set:
            # Quick response:
            # Reject if first move from 0 to 1 by one step is failed
            return False
        
        visited.add( (1, 1) )
        traversal_queue.append( (1,1) )
        
        # Start BFS traversal with 0->1 with one step as initial condition
        while traversal_queue:
            
            for _ in range(len(traversal_queue)):
                
                cur_stone_index, prev_step = traversal_queue.pop()
                
                if cur_stone_index == destination:
                    return True
                
                for cur_step in {prev_step+1, prev_step, prev_step-1}:
                    
                    if cur_step <= 0:
                        # Frog can only jump in the forward direction
                        continue
                    
                    # compute next jump, and check with correctness and no repetition
                    next_jump = cur_stone_index+cur_step
                    if (2**31 > next_jump > 0) and (next_jump in stone_set) and ( (next_jump, cur_step) not in visited):
                    
                        # update current moving into visited set    
                        visited.add( (next_jump, cur_step) )
                        # add next jump into traversal queue
                        traversal_queue.append( (next_jump, cur_step) )
                        
        return False



# n : the lenth of input array, stones.

## Time Complexity: O( n )
#
# The overhead in time is the cost of BFS traversal on 1D linked list, which is of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the storage for traversal queue, which is of O( n ).



def test_bench():

    test_data = [
                    [0,1,3,5,6,8,12,17],
                    [0,1,2,3,4,8,9,11],
                    [0,2]
                ]
    # expected output:
    '''
    True
    False
    False
    '''
    for stone_sequence in test_data:
        print( Solution().canCross(stone_sequence))
    
    return



if __name__ == '__main__':

    test_bench()