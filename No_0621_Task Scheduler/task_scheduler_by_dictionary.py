'''

Description:

Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks. Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.

 

Example:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
 

Note:

The number of tasks is in the range [1, 10000].
The integer n is in the range [0, 100].

'''



'''

Example explanation:

tasks = ["A","A","A","B","B","B"], n = 2

Procedure:

1.
# Build a dictionary for tasks
# key   : task
# value : occurrence of task

max_occ = 3

number_of_taks_of_max_occ = 2 with {'A', 'B'}

2.
#Make (max_occ - 1) = 2 groups, groups size = n+1 = 3
#Fill each group with uniform iterleaving as even as possible

group = '_ _ _' with size = 3

=> make 2 groups with uniform iterleaving 

A B _ A B _

3.
# At last, execute for the last time of max_occ jobs

A B _ A B _ A B


length of task scheduling with cooling = 8

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
        
        # max occurrence of among tasks
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
        


# n : the length of input list, tasks.

## Time Complexity: O( n )
#
# The overhead in time is the dictionary build of task_occ_dict,
# and the computation of number_of_taks_of_max_occ, which are of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the storage for the dictionary, task_occ_dict, which is of O( 1 ).



def test_bench():

    test_data = [
                    (["A","A","A","B","B","B"], 2),
                    (["A","A","A","B","B","B",'C','C','D'] ,2)
                ]
    
    # expected output:
    '''
    8
    9
    '''


    for sequence, n in test_data:

        print( Solution().leastInterval(sequence, n) )

    return 



if __name__ == '__main__':

    test_bench()