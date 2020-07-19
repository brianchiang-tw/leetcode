'''

Description:

There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

Example 1:

Input: 2, [[1,0]] 
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished   
             course 0. So the correct course order is [0,1] .


             
Example 2:

Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both     
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. 
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.

'''

from typing import List
import collections

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

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
            
            # add current completed course into taking order
            course_taking_order.append( course )
            
            return False
        
        # -------------------------------
        
        # each course maintain a list of its own prerequisites
        requirement = collections.defaultdict( list )
        
        for course, pre_course in prerequisites:
            requirement[course].append( pre_course )
        
        
        # each course maintain a state among {NOT_CHECKED, CHECKING, COMPLETED}
        course_state = [ NOT_CHECKED for _ in range(numCourses) ]
           
        
        course_taking_order = []
        
        no_deadlock = True
        for course_idx in range(0, numCourses):
            
            if has_deadlock(course_idx):
                # deadlock is found, impossible to finish all courses
                no_deadlock = False
        
        
        
        if no_deadlock:
            # we can finish all course with proper order 
            return course_taking_order
        
        else:
            return []
                    

# n : the length of prerequisites

## Time Complexity: O( n )
#
# The overhead in time is the cost of DFS, which is of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the storage for recursion call stack, which is of O( n ).


import unittest
class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().findOrder( numCourses=2, prerequisites=[[1,0]] )
        self.assertEqual( result, [0,1])


    
    def test_case_2( self ):

        result = Solution().findOrder( numCourses=4, prerequisites=[[1,0],[2,0],[3,1],[3,2]] )

        judge = None

        if result == [0,1,2,3] or result == [0,2,1,3]:
            judge = True
        else:
            judge = False

        self.assertEqual( judge, True)



if __name__ == '__main__':

    unittest.main()
