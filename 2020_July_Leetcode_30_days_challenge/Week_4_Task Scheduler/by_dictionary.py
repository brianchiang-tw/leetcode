'''

Description:

You are given a char array representing tasks CPU need to do. It contains capital letters A to Z where each letter represents a different task. Tasks could be done without the original order of the array. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

You need to return the least number of units of times that the CPU will take to finish all the given tasks.

 

Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: 
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.



Example 2:

Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation: On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
And so on.



Example 3:

Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
Explanation: 
One possible solution is
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A
 

Constraints:

The number of tasks is in the range [1, 10000].
The integer n is in the range [0, 100].

'''


from collections import Counter
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        if n == 0:
            # Quick response for special case on n = 0
            # no requirement for cooling, just do those jobs in original order
            return len(tasks)
        
        
        # key   : task
        # value : occurrence of tasks 
        task_occ_dict = Counter( tasks )
        
        # max occurrence among tasks
        max_occ = max( task_occ_dict.values() )
        
        # number of tasks with max occurrence
        number_of_taks_of_max_occ = sum( ( 1 for task, occ in task_occ_dict.items() if occ == max_occ ) )
        
        # Make (max_occ-1) groups, each groups size is (n+1) to meet the requirement of cooling
        # Fill each group with uniform iterleaving as even as possible
        
        # At last, execute for the last time of max_occ jobs
        intervl_for_schedule = ( max_occ-1 )*( n+1 ) + number_of_taks_of_max_occ
        
        # Minimal length is original length on best case.
        # Otherswise, it need some cooling intervals in the middle
        return max( len(tasks), intervl_for_schedule)


# N : the length of input tasks

## Time Complexity: O( N )
#
# The overhead in time is the cost of dictionary building, which is of O( N )

## Space Complexity: O( N )
#
# The overhead in space is the storage for dictionary, which is of O( N )
        
import unittest

class Testing(unittest.TestCase):
    
    def test_case_1(self):
        
        result = Solution().leastInterval(tasks = ["A","A","A","B","B","B"], n = 2)
        self.assertEqual(result, 8)
        

if __name__ == '__main__':
    
    unittest.main()
