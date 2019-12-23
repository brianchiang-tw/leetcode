class Solution:
    def balancedStringSplit(self, s):
        #print( len(s) )

        #for i in range( 1, len(s)+1 ):
            
            #occ_of_L = s[:i].count('L')

            #if occ_of_L * 2 == i:
            #    print("meet at {}".format( i ) )

        return sum(s[:i].count('L') * 2 == i for i in range(1, len(s)+1))



# n : the length in input string

## Time Complexity: O( n )
#
# The overhead in time is the for loop itertaions inside list comprehension, which is of O( n )

## Space Complexity: O( 1 )
#
# The oberhead in space is to maintain variable for counter, which is of O( 1 )



def test_bench():

    test_data = ["RLRRLLRLRL"]

    for s in test_data:

        print( Solution().balancedStringSplit(s) )



if __name__ == '__main__':

    test_bench()