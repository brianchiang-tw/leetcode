

class Solution:
    def isNumber(self, s: str) -> bool:
        
        try:
            
            float(s)
            return True
        
        except:
            return False


# n : the length of input string

## Time Complexity: O( n )
#
# Although it seems O(1) at forst glimpse, 
# but float(s) does check every character and transform them to floating nubmer if no exception occurs.
# Thus, it is of O( n )

## Space Complexity: O( 1 )
#
# The overhead in space is temporary object for float(s) of O( 1 )



def test_bench():

    test_data = [".", "-+3", "1.23", "1.3e5", "-.", "+.3"]


    # expected output:
    '''
    False
    False
    True
    True
    False
    True
    '''

    for s in test_data:

        print( Solution().isNumber(s) )

    return



if __name__ == '__main__':

    test_bench()