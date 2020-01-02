'''

Description:

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: 3
Output: "III"
Example 2:

Input: 4
Output: "IV"
Example 3:

Input: 9
Output: "IX"
Example 4:

Input: 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.
Example 5:

Input: 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

'''



class Solution:
    def intToRoman(self, num: int) -> str:
        
        counter = 0
        ones, tens, hundreds, thousands = None, None, None, None

        
        while( num != 0):
            
            digit = num % 10
            
            if counter == 0:
                ones = digit
                
            elif counter == 1:
                tens = digit
            
            elif counter == 2:
                hundreds = digit
                
            elif counter == 3:
                thousands = digit
                
                
            # next run
            counter += 1
            num = num // 10
        
        
        
        # message for tracing and debugging
        # print("{} {} {} {}".format(thousands, hundreds, tens, ones) )
        
        
        # str_roman store the roman number representation
        str_roman = str()
        
        if thousands is not None:
        
            roman_thousands = "M"
            
            str_roman += (roman_thousands * thousands)
        
        
        
        if hundreds is not None:
        
            roman_100 = "C"
            roman_500 = "D"
            roman_400 = "CD"
            roman_900 = "CM"
        
            if 3 >= hundreds >= 1 :
                
                str_roman += roman_100*hundreds
            
            elif 4 == hundreds :
                
                str_roman += roman_400
            
            elif 5 == hundreds :
                
                str_roman += roman_500
            
            elif 8 >= hundreds >= 6:
                
                offset = hundreds-5
                str_roman += ( roman_500 + roman_100*offset )
                
            elif 9 == hundreds:
                
                str_roman += roman_900
                
                
                
        if tens is not None:
            
            roman_10 = "X"
            roman_50 = "L"
            roman_40 = "XL"
            roman_90 = "XC"
            
            if 3 >= tens >= 1 :
                
                str_roman += roman_10*tens
            
            elif 4 == tens :
                
                str_roman += roman_40
            
            elif 5 == tens :
                
                str_roman += roman_50
            
            elif 8 >= tens >= 6:
                
                offset = tens-5
                str_roman += ( roman_50 + roman_10*offset )
                
            elif 9 == tens:
                
                str_roman += roman_90
                
        
        
        if ones is not None:
            
            roman_1 = "I"
            roman_5 = "V"
            roman_4 = "IV"
            roman_9 = "IX"
            
            if 3 >= ones >= 1 :
                
                str_roman += roman_1*ones
            
            elif 4 == ones :
                
                str_roman += roman_4
            
            elif 5 == ones :
                
                str_roman += roman_5
            
            elif 8 >= ones >= 6:
                
                offset = ones-5
                str_roman += ( roman_5 + roman_1*offset )
                
            elif 9 == ones:
                
                str_roman += roman_9
            
        return str_roman



def test_bench():

    test_numbers = [4, 9, 10, 8, 68, 468, 2468]

    "expected output"
    '''
    IV
    IX
    X
    VIII
    LXVIII
    CDLXVIII
    MMCDLXVIII
    '''


    for x in test_numbers:

        roman_notation = Solution().intToRoman( x )

        print( roman_notation )

    return



if __name__ == "__main__":

    test_bench()