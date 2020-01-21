'''

Description:

Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach to any index with value 0.

Notice that you can not jump outside of the array at any time.

 

Example 1:

Input: arr = [4,2,3,0,3,1,2], start = 5
Output: true
Explanation: 
All possible ways to reach at index 3 with value 0 are: 
index 5 -> index 4 -> index 1 -> index 3 
index 5 -> index 6 -> index 4 -> index 1 -> index 3 
Example 2:

Input: arr = [4,2,3,0,3,1,2], start = 0
Output: true 
Explanation: 
One possible way to reach at index 3 with value 0 is: 
index 0 -> index 4 -> index 1 -> index 3
Example 3:

Input: arr = [3,0,2,1,2], start = 2
Output: false
Explanation: There is no way to reach at index 1 with value 0.
 

Constraints:

1 <= arr.length <= 5 * 10^4
0 <= arr[i] < arr.length
0 <= start < arr.length

'''



from collections import deque
from typing import List
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        
        if arr[start] == 0:
            # Quick response if start == destination
            return True
        
        # Level-order traversal queue
        traversal_queue = deque( [start] )
        
        # set of visited index, in order to avoid repeated visit
        visited_set = set( {start} )
        
        arr_size = len(arr)
        
        # keep level-order traversal if queue is not empty
        while (traversal_queue):

            size_of_q = len(traversal_queue)
            
            # all index of current level jump once
            for _ in range(size_of_q):
                
                # get current index ( source )
                current_index = traversal_queue.popleft()
                #print(f'pop cuurent index from traversal queue: {current_index}')
                
                # get jump distance
                jump_distance = arr[current_index]
                #print(f'jump distance = {jump_distance}')

                # try jump left and jump right
                for offset in ( -jump_distance, jump_distance):
                    
                    # compute index of next jump 
                    next_jump = current_index + offset
                    
                    # check next_jump is within array, and next_jump is not visited
                    if arr_size > next_jump >= 0 and next_jump not in visited_set:
                        #print( f'check next jump: arr[{next_jump}]')
                        
                        if arr[next_jump] == 0:
                            # check if we reach destination
                            #print( f'next jump arr[{next_jump}] reach destination with value 0')
                            return True

                        else:
                            # otherwise, add next_jump as source of next_level, push into traversal queue
                            #print(f'set next jump arr[{next_jump}] as visited.')
                            #print(f'push next jump arr[{next_jump}] into traversal queue for next level.')
                            visited_set.add(next_jump)
                            traversal_queue.append(next_jump)
        
        
        # if queue is empty and we haven't met destination, then there is no jump path from start index to destination of value 0
        return False



# n : the length of input list, arr.

## Time Complexity: O( n )
#
# The overhead in time is the cost of level-order-traversal, which is of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the storage for traversal queue as well as visited set, which is of O( n ).



def test_bench():

    test_data = [
                    ([4,2,3,0,3,1,2], 5),
                    ([4,2,3,0,3,1,2], 0),
                    ([3,0,2,1,2], 2)
                ]

    # expected output:
    '''
    True
    True
    False    
    '''

    for sequence, start_index in test_data:
        print( Solution().canReach(sequence, start_index ) )

    return 

 

if __name__ == '__main__':

    test_bench()