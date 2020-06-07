'''

Description:

Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.

 
Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
 

Hint #1  
What can you say about the position of the shortest person?
If the position of the shortest person is i, how many people would be in front of the shortest person?

Hint #2  
Once you fix the position of the shortest person, what can you say about the position of the second shortest person?

'''



from typing import List

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        
        # higher person stand before shorter one
        # if get tie in height, then compare k
        people.sort( key = lambda person:( -person[0],person[1] ) )
        
        reorder = []
        
        # rearrange person by height and parameter k
        for height, k in people:
            
            person = [height, k] 
            
            reorder.insert(k, person)
        
        return reorder



# n : the length of input array, people.

## Time Complexity: O( n log n )
#
# The overhead in time is the cost of sorting, which is of O( n log n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for list of reorder, which is of O( n )



from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'array_of_people')

def test_bench():

    test_data = [
                    TestEntry( array_of_people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]] ),
                    TestEntry( array_of_people = [[5,0], [1,0], [5,1]] ),
                ]

    # expected output:
    '''
    [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]
    [[1, 0], [5, 0], [5, 1]]
    '''

    for t in test_data:
        print( Solution().reconstructQueue( t.array_of_people) )
    
    return



if __name__ == '__main__':

    test_bench()