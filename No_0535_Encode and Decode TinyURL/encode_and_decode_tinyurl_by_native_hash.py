'''

Description:

Note: This is a companion problem to the System Design problem: Design TinyURL.
TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

'''



class Codec:
    
    def __init__(self):
        
        self.url_table = dict()
    
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """

        # generate url id by native hash() function
        url_id = hash(longUrl)
        header = 'http://tinyurl.com/'
        
        # generate shour url
        short_url = header + str(url_id)


        self.url_table[url_id] = longUrl
        
        return short_url
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        
        # paring the url id after 'http://tinyurl.com/'
        url_id = int(shortUrl[19:])
        
        # lookup original url by url_id in dictionary
        return self.url_table[url_id]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))



# n : the length of input URL

## Time Complexity: O(n)
#
# The overhead in time is the cost of sequence generated from hash(n), which is of O( n ).

## Space Complexity: O(1)
#
# The overhead in space is the storage for one entry in dictionary, which is of O( 1 )



def test_bench():

    test_data = [
                    'https://www.leetcode.com',
                    'https://www.google.com'
                ]

    coder = Codec()
    for link in test_data:

        short_url = coder.encode( link )
        print( coder.decode(short_url) )
    
    return 



if __name__ == '__main__':

    test_bench()