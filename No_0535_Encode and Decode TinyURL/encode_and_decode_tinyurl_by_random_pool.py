from random import choices

class Codec:

    rand_pool = list( "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" )
    
    def __init__(self):
        
        self.url_table = dict()
    
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        url_id = None
        while True:
            url_id = ''.join( choices( Codec.rand_pool,  k = 6) )
        
            if url_id not in self.url_table:
                self.url_table[url_id] = longUrl
                break
        
        return url_id
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        
        return self.url_table[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))



from random import choices

class Codec:

    rand_pool = list( "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" )
    
    def __init__(self):
        
        self.url_table = dict()
    
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        url_id = None
        header = 'http://tinyurl.com/'
        short_url = None
        while True:

            # generate random sequence, of 6 characters, from random pool
            url_id = ''.join( choices( Codec.rand_pool,  k = 6) )
        
            if url_id not in self.url_table:

                # update key-value pair in dictionary, url_table
                self.url_table[url_id] = longUrl

                # generate shout URL
                short_url = header + url_id
                
                break
        
        return url_id
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        
        # paring the url id after 'http://tinyurl.com/'
        url_id = shortUrl[19:]

        # lookup original url by url_id in dictionary
        return self.url_table[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))



# n : the length of input URL

## Time Complexity: O(1)
#
# The overhead in time is the cost of sequence generated from random pool, which is of O( 1 ).

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