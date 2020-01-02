'''

Description:

The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

 

Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"

'''


class Solution:
    def countAndSay(self, n: int) -> str:
        
        
        if ( n == 1 ):
            # Base case:
            
            return "1"
        
        else:
            # Inductive step:
            
            # recursively call to get previous count-and-say sequence
            integer_string = self.countAndSay( n-1 )
            
            # "@" act as special ending symbol
            integer_string += "@"
        
            # initialize count_and_say_sequence to empty string
            count_and_say_sequence = str()
            
            # counter of character
            character_count = 1
            
            # -1 is for skipping special ending symbol @
            for i in range( len(integer_string)-1 ):
                
                if integer_string[i] == integer_string[i+1] :
                    
                    # if catch character repetition, increase character_count
                    character_count += 1
                    
                else:
                    
                    # make corresponding count-and-say sequence to current character
                    count_and_say_sequence += str(character_count) + integer_string[i]
                    
                    # reset character_count to 1
                    character_count = 1
                
            
            return count_and_say_sequence
        
## Time Complexity
#
# f(n)  = f(n-1) + f(n-2) + f(n-3) + ... + f(2) + f(1)
#       = (n-1) + (n-2) + (n-3) + ... + 2 + 1
#       = O( n ^ 2)

## Space Complexity

# The growth rate of count-and-say sequence length is about 1.3
# Thus, the space needed to store output sequence is O( 1.3 ^ n)

def test_bench():

    test_n_values = list( range(1, 20) )

    for n in test_n_values :

        count_and_say_sequence = Solution().countAndSay( n )

        print( " n : {}, sequence : {}, length of sequene : {}".format( n, count_and_say_sequence, len(count_and_say_sequence) ) )


    return


# expected output
'''

 n : 1, sequence : 1, length of sequene : 1
 n : 2, sequence : 11, length of sequene : 2
 n : 3, sequence : 21, length of sequene : 2
 n : 4, sequence : 1211, length of sequene : 4
 n : 5, sequence : 111221, length of sequene : 6
 n : 6, sequence : 312211, length of sequene : 6
 n : 7, sequence : 13112221, length of sequene : 8
 n : 8, sequence : 1113213211, length of sequene : 10
 n : 9, sequence : 31131211131221, length of sequene : 14
 n : 10, sequence : 13211311123113112211, length of sequene : 20
 n : 11, sequence : 11131221133112132113212221, length of sequene : 26
 n : 12, sequence : 3113112221232112111312211312113211, length of sequene : 34
 n : 13, sequence : 1321132132111213122112311311222113111221131221, length of sequene : 46
 n : 14, sequence : 11131221131211131231121113112221121321132132211331222113112211, length of sequene : 62
 n : 15, sequence : 311311222113111231131112132112311321322112111312211312111322212311322113212221, length of sequene : 78
 n : 16, sequence : 132113213221133112132113311211131221121321131211132221123113112221131112311332111213211322211312113211, length of sequene : 102      
 n : 17, sequence : 11131221131211132221232112111312212321123113112221121113122113111231133221121321132132211331121321231231121113122113322113111221131221, length of sequene : 134
 n : 18, sequence : 31131122211311123113321112131221123113112211121312211213211321322112311311222113311213212322211211131221131211132221232112111312111213111213211231131122212322211331222113112211, length of sequene : 176
 n : 19, sequence : 1321132132211331121321231231121113112221121321132122311211131122211211131221131211132221121321132132212321121113121112133221123113112221131112311332111213122112311311123112111331121113122112132113213211121332212311322113212221, length of sequene : 226

'''





if __name__ == '__main__':

    test_bench()