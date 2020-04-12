'''

Description:

HTML entity parser is the parser that takes HTML code as input and replace all the entities of the special characters by the characters itself.

The special characters and their entities for HTML are:

Quotation Mark: the entity is &quot; and symbol character is ".
Single Quote Mark: the entity is &apos; and symbol character is '.
Ampersand: the entity is &amp; and symbol character is &.
Greater Than Sign: the entity is &gt; and symbol character is >.
Less Than Sign: the entity is &lt; and symbol character is <.
Slash: the entity is &frasl; and symbol character is /.
Given the input text string to the HTML parser, you have to implement the entity parser.

Return the text after replacing the entities by the special characters.

 

Example 1:

Input: text = "&amp; is an HTML entity but &ambassador; is not."
Output: "& is an HTML entity but &ambassador; is not."
Explanation: The parser will replace the &amp; entity by &



Example 2:

Input: text = "and I quote: &quot;...&quot;"
Output: "and I quote: \"...\""



Example 3:

Input: text = "Stay home! Practice on Leetcode :)"
Output: "Stay home! Practice on Leetcode :)"



Example 4:

Input: text = "x &gt; y &amp;&amp; x &lt; y is always false"
Output: "x > y && x < y is always false"



Example 5:

Input: text = "leetcode.com&frasl;problemset&frasl;all"
Output: "leetcode.com/problemset/all"
 

Constraints:

1 <= text.length <= 10^5
The string may contain any possible characters out of all the 256 ASCII characters.

'''


import re
class Solution:
    def entityParser(self, text: str) -> str:
        
        html_symbol = [ '&quot;', '&apos;', '&gt;', '&lt;', '&frasl;', '&amp;']
        formal_symbol = [ '"', "'", '>', '<', '/', '&']
                
        for html_sym, formal_sym in zip(html_symbol, formal_symbol):
            text = re.sub( html_sym , formal_sym, text )
        
        return text



# n : the character length of input, text.

## Time Complexity: O( n )
#
# The overhead in time is the cost of string replacement, which is of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the storage for output string, which is of O( n ).

from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'text')
def test_bench():

    test_data = [
                    TestEntry( text = "&amp; is an HTML entity but &ambassador; is not." ),
                    TestEntry( text = "and I quote: &quot;...&quot;" ),
                    TestEntry( text = "Stay home! Practice on Leetcode :)" ),
                    TestEntry( text = "x &gt; y &amp;&amp; x &lt; y is always false" ),
                    TestEntry( text = "leetcode.com&frasl;problemset&frasl;all" ),
                ]


    # expected output:
    '''
    & is an HTML entity but &ambassador; is not.
    and I quote: "..."
    Stay home! Practice on Leetcode :)
    x > y && x < y is always false
    leetcode.com/problemset/all
    '''

    for t in test_data:

        print( Solution().entityParser( text = t.text) )
    
    return



if __name__ == '__main__':

    test_bench()