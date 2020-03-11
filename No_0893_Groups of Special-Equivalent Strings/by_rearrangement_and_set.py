'''

Description:

You are given an array A of strings.

A move onto S consists of swapping any two even indexed characters of S, or any two odd indexed characters of S.

Two strings S and T are special-equivalent if after any number of moves onto S, S == T.

For example, S = "zzxy" and T = "xyzz" are special-equivalent because we may make the moves "zzxy" -> "xzzy" -> "xyzz" that swap S[0] and S[2], then S[1] and S[3].

Now, a group of special-equivalent strings from A is a non-empty subset of A such that:

Every pair of strings in the group are special equivalent, and;
The group is the largest size possible (ie., there isn't a string S not in the group such that S is special equivalent to every string in the group)
Return the number of groups of special-equivalent strings from A.

 
 
Example 1:

Input: ["abcd","cdab","cbad","xyzz","zzxy","zzyx"]
Output: 3
Explanation: 
One group is ["abcd", "cdab", "cbad"], since they are all pairwise special equivalent, and none of the other strings are all pairwise special equivalent to these.

The other two groups are ["xyzz", "zzxy"] and ["zzyx"].  Note that in particular, "zzxy" is not special equivalent to "zzyx".



Example 2:

Input: ["abc","acb","bac","bca","cab","cba"]
Output: 3
 

Note:

1 <= A.length <= 1000
1 <= A[i].length <= 20
All A[i] have the same length.
All A[i] consist of only lowercase letters.

'''



from typing import List
class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        
        signature = set()
        
        # Use pair of sorted even substring and odd substring as unique key
        
        for idx, s in enumerate(A):
            signature.add( ''.join( sorted( s[::2] ) ) + ''.join( sorted( s[1::2] ) )  )
        
        return len( signature )



# n : the length of input list, A.
# k : the average length of each string in A

## Time Comlexity: O( n * k log k )
#
# The overhead in time is the for loop, iterating on A, which of O( n ), and
# the overhead of substring sorting, which is of O( k log k ).
# It takes O( n * k log k ) in total.

## Space Complexity: O( n * k )
#
# The overhead in space is the storage for set signature, which is of O( n * k )


from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'list_of_string')
def test_bench():

    test_data = [
                    TestEntry( list_of_string = ["abcd","cdab","cbad","xyzz","zzxy","zzyx"] ),
                    TestEntry( list_of_string = ["abc","acb","bac","bca","cab","cba"] ),
                ]
    
    # expected output:
    '''
    3
    3
    '''

    for t in test_data:

        print( Solution().numSpecialEquivGroups( A = t.list_of_string) )
    
    return 



if __name__ == '__main__':

    test_bench()