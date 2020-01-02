class Solution:
    def reverse(self, x: int) -> int:
        
        # Convert integer to string
        str_int = str(x)
        
        is_negative = False
        
        # Check for '-' minus character
        if str_int[0] == '-':
            
            # delete '-' temporarily
            str_int = str_int[1:]
            is_negative = True
        
        
        # Reverse string of integer
        str_int_reversed = str_int[::-1]
        
        # Convert string to integer
        int_reversed = int(str_int_reversed)
        
        # Check whether it is negative number or not
        if is_negative:
            int_reversed = -1 * int_reversed
        
        # Check for integer overflow of 32 bits
        if int_reversed > 2 ** 31 -1 or int_reversed < -1 * 2 ** 31:
            return 0
        
        return int_reversed



def test_bench():

    test_integers = [123, -123, 120, 2**31]

    # expected output:
    '''
    321
    -321
    21
    0
    '''



    for x in test_integers:

        ret_value = Solution().reverse( x )

        print( ret_value )

    return



if __name__ == "__main__":

    test_bench()