'''

Description:

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
 

Constraints:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.

1 <= numCourses <= 10^5

Hint #1  
This problem is equivalent to finding if a cycle exists in a directed graph. If a cycle exists, no topological ordering exists and therefore it will be impossible to take all courses.

Hint #2  
Topological Sort via DFS - A great video tutorial (21 minutes) on Coursera explaining the basic concepts of Topological Sort.

Hint #3  
Topological sort could also be done via BFS.

'''



from collections import defaultdict
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
		# Constant defined for course state
        NOT_CHECKED, CHECKING, COMPLETED = 0, 1, 2
        
        # -------------------------------
        
        def has_deadlock( course )->bool:
            
            if course_state[course] == CHECKING:
                # There is a cycle(i.e., deadlock ) in prerequisites
                return True
            
            elif course_state[course] == COMPLETED:
                # current course has been checked and marked as completed
                return False
            
            
            
            # update current course as checking
            course_state[course] = CHECKING
            
            # check pre_course in DFS and detect whether there is deadlock
            for pre_course in requirement[course]:
                
                if has_deadlock( pre_course ):
                    # deadlock is found, impossible to finish all courses
                    return True
                
                                
            # update current course as completed
            course_state[course] = COMPLETED
            
            return False
        
        # -------------------------------
        
        # each course maintain a list of its own prerequisites
        requirement = defaultdict( list )
        
        for course, pre_course in prerequisites:
            requirement[course].append( pre_course )
        
        
        # each course maintain a state among {NOT_CHECKED, CHECKING, COMPLETED}
		# Initial state is NOT_CHECKED 
        course_state = [ NOT_CHECKED for _ in range(numCourses) ]
           
        # Launch cycle (i.e., deadlock ) detection in DFS
        for course_idx in range(0, numCourses):
            
            if has_deadlock(course_idx):
                # deadlock is found, impossible to finish all courses
                return False
        
        # we can finish all course with required order 
        return True



# V : the number of course
# E : the length of prerequisites

## Time Complexity: O( V + E )
#
# The overhead in time is the cost of DFS, which is of O( V + E )

## Space Complexity: O( V + E )
#
# The overhead in space is the storage for recursion call stack, which is of O( V + E )


from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'num_of_course prerequisites')

def test_bench():

    test_data = [
                    TestEntry( num_of_course = 2, prerequisites = [[1,0]] ),
                    TestEntry( num_of_course = 2, prerequisites = [[1,0],[0,1]] ),
                ]

    # expected output:
    '''
    True
    False
    '''

    for t in test_data:

        print( Solution().canFinish( *t ) )
    
    return



if __name__ == '__main__':

    test_bench()