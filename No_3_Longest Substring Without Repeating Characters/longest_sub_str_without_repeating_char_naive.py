class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # Boundary case:
        # Longest substring length of NULL string is 0
        if len(s) == 0 :
            return 0
        
        # one character must be longest substring by itself
        max_length_substr_without_repeatition = 1
        
        # search max substr from index 0
        start_index_of_max_substr = 0
        
        for i in range( 0, len(s) ):
            

            
            # substring of s start from i
            str_start_from_i = s[i:]
            
            #print("start from i {}".format(i) )
            #print("substr from i {}".format(str_start_from_i) )
            
            
            # one character must be longest substring by itself
            current_length_substr_without_repeatition = 1
            
            for j in range( 1, len(str_start_from_i) ):
                
                #print("i", i)
                #print("j", j)
                
                #print("checking {}".format( str_start_from_i[j] ) )
                
                if str_start_from_i[j] not in str_start_from_i[0:j]:
                    # if current character has no repetition so far, then current length add 1
                    #print("character {} pass".format(str_start_from_i[j]) )
                    current_length_substr_without_repeatition += 1
                
                else:
                    # if current character has repetition, then stop, check, then go to next iteration of i
                    #print("stop at j = {}".format(j) )
                    break
                
                
                
            if current_length_substr_without_repeatition > max_length_substr_without_repeatition:
                        
                # update max length as well as start index if needed
                
                max_length_substr_without_repeatition = current_length_substr_without_repeatition
                start_index_of_max_substr = i
                
                
        #print("index", start_index_of_max_substr )                 
                        
        return max_length_substr_without_repeatition

def stringToString(input):
    import json

    return json.loads(input)

def main():
    import sys
    import io

    test_string= ["aab", "pwwkew", "", "au"]
    # expected answer:
    '''
    2, 3, 0, 2
    '''

    def readlines():
        #for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
        for line in test_string:
            #yield line.strip('\n')
            yield line

    lines = readlines()
    while True:
        try:
            line = next(lines)
            #s = stringToString(line);
            s = line
            
            ret = Solution().lengthOfLongestSubstring(s)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()