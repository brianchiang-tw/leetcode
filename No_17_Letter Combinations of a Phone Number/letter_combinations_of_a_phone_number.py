'''

Description:

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

1 None      2 abc       3 def
4 ghi       5 jkl       6 mno
7 pqrs      8 tuv       9 wxyz
* +         0           #

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

'''



import copy

class Solution:
    
    
    def letterCombinations(self, digits: str):
        
        
        # corner case handling:
        if digits == "":
            return list()
        
        char_array =    [ ['a','b','c'],
                        ['d','e','f'],
                        ['g','h','i'],
                        ['j','k','l'],
                        ['m','n','o'],
                        ['p','q','r','s'],
                        ['t','u','v'],
                        ['w','x','y','z']
                        ]
        

        
        
        letter_combination = list([""])
        
        for char in digits:
            
            index = int(char)
            
            # storage for new_combination for iteration on letter
            new_combination = list()
            
            for letter in char_array[ index - 2 ]:
            
                #print("letter {}".format(letter))
                
                for original_comb in letter_combination:
                    
                    # create the string of combination
                    combination = original_comb + letter

                    #print("add {}".format(combination) )
                    
                    # add to letter_combination container
                    new_combination.append( combination )
                    
                    #print("new_comb : {}".format( new_combination ) )
                    
            # write back to letter_combination        
            letter_combination = copy.deepcopy( new_combination )
                
        
        return letter_combination


# N: The number of digits in the input that maps to 3 letters like 2, 3,4
# M: The number of digits in the input that maps to 4 letters like 7, 9
# Time Complexity:
# O(3**N * 4 ** M) for the iteration count based on combination

# Space Complexity:
# O(3**N * 4 ** M) for the space for letter combination



        
        
def test_bench():

    test_string = "23"

    letter_combination = Solution().letterCombinations( test_string )

    print( letter_combination )
    # expected output:
    '''
    ['ad', 'bd', 'cd', 'ae', 'be', 'ce', 'af', 'bf', 'cf']
    '''


if __name__ == "__main__":

    test_bench()        
        