class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        length_of_longest_substr = 0
        left_bound_of_sliding_window = -1
        
        dictionary = dict()
        # key = character
        # value = last occurrence index of character beforehand
        
        for i in range(len(s)):
            
            #print("checking {}".format(s[i]) )
            
            # update right bound of sliding window
            right_bound_of_sliding_window = i
            
            # last occurrence index of current character beforehad
            last_occurrence_pos = dictionary.get(s[i], None)
            
            # check if current character is not first-time occurrence
            if( last_occurrence_pos is not None and last_occurrence_pos > left_bound_of_sliding_window ):
                
                #print("{} is repeated".format(s[i]) )
                
                # update left bound of sliding window
                left_bound_of_sliding_window = last_occurrence_pos
                
            
            # update last occurrence index of current character
            dictionary[s[i]] = right_bound_of_sliding_window
            
            # when right bound increase, substring length extends by one character
            # when left bound increase, substring length shrink by one character
            window_length = right_bound_of_sliding_window - left_bound_of_sliding_window
            
            #print("len of window: {}".format(window_length) )
            
            length_of_longest_substr = max( length_of_longest_substr, window_length)
            
            #print("len of longestsubstr", length_of_longest_substr)
            
                        
        return length_of_longest_substr

        

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