'''

Description:

A website domain like "discuss.leetcode.com" consists of various subdomains. At the top level, we have "com", at the next level, we have "leetcode.com", and at the lowest level, "discuss.leetcode.com". When we visit a domain like "discuss.leetcode.com", we will also visit the parent domains "leetcode.com" and "com" implicitly.

Now, call a "count-paired domain" to be a count (representing the number of visits this domain received), followed by a space, followed by the address. An example of a count-paired domain might be "9001 discuss.leetcode.com".

We are given a list cpdomains of count-paired domains. We would like a list of count-paired domains, (in the same format as the input, and in any order), that explicitly counts the number of visits to each subdomain.

Example 1:
Input: 
["9001 discuss.leetcode.com"]
Output: 
["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]
Explanation: 
We only have one website domain: "discuss.leetcode.com". As discussed above, the subdomain "leetcode.com" and "com" will also be visited. So they will all be visited 9001 times.

Example 2:
Input: 
["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
Output: 
["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]
Explanation: 
We will visit "google.mail.com" 900 times, "yahoo.com" 50 times, "intel.mail.com" once and "wiki.org" 5 times. For the subdomains, we will visit "mail.com" 900 + 1 = 901 times, "com" 900 + 50 + 1 = 951 times, and "org" 5 times.

Notes:

The length of cpdomains will not exceed 100. 
The length of each domain name will not exceed 100.
Each address will have either 1 or 2 "." characters.
The input count in any count-paired domain will not exceed 10000.
The answer output can be returned in any order.

'''


from typing import List
class Solution:
    
    def get_sub_domain( self, domain:str):
        
        tokens = domain.split('.', 1)

        if len(tokens) != 1:
            sub_domain = tokens[1]
        else:
            sub_domain = tokens[0]
            
        return sub_domain
    
    
    
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        domain_visit_dict = dict()
        
        # visit each pair: (visit, domain)
        for pair in cpdomains:
            
            visit, domain = map( str, pair.split() )
            
            # update domain's visit count
            domain_visit_dict[ domain ] =  domain_visit_dict.get( domain, 0) + int(visit)
            
            sub_domain = self.get_sub_domain( domain )
            
            
            
            # visit each subdomain
            while sub_domain != domain:
                
                domain = sub_domain
                
                # update domain's visit count
                domain_visit_dict[ domain ] =  domain_visit_dict.get( domain, 0) + int(visit)
                
                sub_domain = self.get_sub_domain( domain )
                
        
        
        
        return [ f'{str(visit)} {dom}' for dom, visit in domain_visit_dict.items() ]



# m : the maximal number of subdomains

# n : the length of input list

## Time Complexity: O( m * n )
#
# The overhead in time is the for loop iterating on pair, which is of ( n ), 
# and the while loop iterating on sub_domainm which if of ( m )
#
# It takes O( m * n ) in total.


## Space Complexity : O( m * n )
#
# The overhead in time is the storage for dictionary, domain_visit_dict, which is of O( m * n )


def test_bench():

    test_data = [
                    ["9001 discuss.leetcode.com"],
                    ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
                ]

    for test_list in test_data:
        print( Solution().subdomainVisits( test_list ) )
    
    return 



if __name__ == '__main__':

    test_bench()