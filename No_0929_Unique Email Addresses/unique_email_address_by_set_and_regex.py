'''

Description:

Every email consists of a local name and a domain name, separated by the @ sign.

For example, in alice@leetcode.com, alice is the local name, and leetcode.com is the domain name.

Besides lowercase letters, these emails may contain '.'s or '+'s.

If you add periods ('.') between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name.  For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.  (Note that this rule does not apply for domain names.)

If you add a plus ('+') in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered, for example m.y+name@email.com will be forwarded to my@email.com.  (Again, this rule does not apply for domain names.)

It is possible to use both of these rules at the same time.

Given a list of emails, we send one email to each address in the list.  How many different addresses actually receive mails? 

 

Example 1:

Input: ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
Output: 2
Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails
 

Note:

1 <= emails[i].length <= 100
1 <= emails.length <= 100
Each emails[i] contains exactly one '@' character.
All local and domain names are non-empty.
Local names do not start with a '+' character.

'''



import re
from typing import List
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        self.regex = r'^([\w\.]+)[\w\.\+]*@([\w\.\+]+)$'
        self.pattern = re.compile( self.regex )
        
        def refine_addr( email: str)-> str:


            parsing = self.pattern.match( email )

            # capture local_name, excluding all characters after '+'
            # eliminate all '.', which is don't care symbol
            local_name = parsing.group(1).replace('.', '')

            # capture domain name
            domain_name = parsing.group(2)

            return f'{local_name}@{domain_name}'
           
        
        return len( set( map(refine_addr, emails) ) )



# m : the maximal length of email address

# n : the length of email list

## Time Complexity: O( m * n )
#
# The map( ... ) takes O( n ), and the refine_addr( email ) takes O( m ).
# It takes O( m * n ) in total.


## Space Complexity: O( n )
#
# The overhead in space is the storage for set(...), which is if O( n )



def test_bench():

    test_data = [
                    ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"],
                    ["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]
                ]

    # expected output:
    '''
    2
    3
    '''


    for email_list in test_data:

        print( Solution().numUniqueEmails(email_list) )

    return



if __name__ == '__main__':

    test_bench()