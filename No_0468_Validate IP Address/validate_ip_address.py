import string
from typing import List
class Solution:

    def is_int(self, s:str)-> bool:
        try:
            int(s)
            return True
        except ValueError:
            return False


    def is_hex(self, s:str)-> bool:
        hex_digits = set(string.hexdigits)
        
        return all( (c in hex_digits) for c in s)
    
    
    def in_range( self, num:int )-> bool:
                
        if 255 >= num >= 0:
            return True
        else:
            return False
        
        
    def without_leading_zero_v4( self, s: str)-> bool:
        int_numeric = int(s)
        int_str = str(int_numeric)

        if len(s) == len(int_str):
            return True
        else:
            return False



    def without_leading_zero_v6( self, s: str)-> bool:
        
        hex_numeric = int(s, 16)
        hex_str = str( hex_numeric )
        
        if hex_numeric == 0 and len(s) <= 4:
            # 0000, 000, 00 and 0 are valid
            return True
        
        if len(s) >= 5:
            return False
        else:
            return True
    

    def without_empty_string(self, tokens: List[str])-> bool:

        without_null_string = all( (t != "") for t in tokens )

        return without_null_string
        
    
    def validIPAddress(self, IP: str) -> str:
        
        
        ipv4_candidate_tokens = IP.split(".")
        ipv6_candidate_tokens = IP.split(":")
        is_ipv4 = False
        is_ipv6 = False

        
        
        if len(ipv4_candidate_tokens) == 4:
            
            without_null_string = self.without_empty_string( ipv4_candidate_tokens )

            if without_null_string is not True:
                return "Neither" 

            is_decimal = all( self.is_int(token) for token in ipv4_candidate_tokens  )

            if is_decimal is not True:
                return "Neither"

            is_without_leading_0s = all( self.without_leading_zero_v4(token) for token in ipv4_candidate_tokens )

            if is_without_leading_0s is not True:
                return "Neither"

            is_in_range = all( self.in_range( int(token) ) for token in ipv4_candidate_tokens )
            
            if is_in_range:
                is_ipv4 = True
                return "IPv4"
            else:
                return "Neither"
            
            
        elif len(ipv6_candidate_tokens) == 8:
            
            without_null_string = self.without_empty_string( ipv6_candidate_tokens )

            if without_null_string is not True:
                return "Neither" 

            is_hexadecimal = all( self.is_hex(token) for token in ipv6_candidate_tokens )

            if is_hexadecimal is not True:
                return "Neither"

            without_leading_0s = all( self.without_leading_zero_v6(token) for token in ipv6_candidate_tokens )
            
            if without_leading_0s:
                is_ipv6 = True
                return "IPv6"
            else:
                return "Neither"
            
        else :
            
            return "Neither"
        
        

# N : the length of input string, IP

## Time complexity: O( N )
#
# Major overhead is tokenization and string convertion/convertion of O( N )

## Space complexity: O( N )
#
# Major overhead is the space to store token, which is parsed from input string.


            
def test_bench():

    test_data = [   "172.16.254.1", 
                    "2001:0db8:85a3:0:0:8A2E:0370:7334",
                    "1e1.4.5.6",
                    "01.01.01.01",
                    "2001:0db8:85a3:00000:0:8A2E:0370:7334",
                    "20EE:FGb8:85a3:0:0:8A2E:0370:7334",
                    "1081:db8:85a3:01:-0:8A2E:0370:7334",
                    "2001:db8:85a3:0::8a2E:0370:7334"
                ]

    # expected output:
    '''
    IPv4
    IPv6
    Neither
    Neither
    Neither
    Neither
    Neither
    '''


    for test in test_data:

        judgement = Solution().validIPAddress( test )

        print( judgement )

    return


if __name__ == '__main__':

    test_bench()

