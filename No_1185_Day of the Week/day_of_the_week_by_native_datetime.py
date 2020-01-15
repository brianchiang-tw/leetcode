'''

Description:

Given a date, return the corresponding day of the week for that date.

The input is given as three integers representing the day, month and year respectively.

Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.

 

Example 1:

Input: day = 31, month = 8, year = 2019
Output: "Saturday"
Example 2:

Input: day = 18, month = 7, year = 1999
Output: "Sunday"
Example 3:

Input: day = 15, month = 8, year = 1993
Output: "Sunday"
 

Constraints:

The given dates are valid dates between the years 1971 and 2100.

'''



from datetime import datetime
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:

        # index mapping: 0          1           2           3           4           5       6        
        weekday_name= ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        
        # datetime is a class, whose constructor can output corrsponding date-time object
        #
        # for example:
        # datetime(2020, 1, 15) = '2020-01-15 00:00:00'

        # And its strftime('%w') can convert a date-time object into a index string of weekday, start from Sunday as 0
        #
        # for example:
        # datetime(2020, 1, 15).strftime('%w') = '3'

        # Finally, use int( ... ) to carry out explicit type conversion fron str to integer as weekday index
        return weekday_name[ int( datetime(year, month, day).strftime('%w') ) ]



# d, m ,y : input value for day, month, and year

## Time Complexity: O( 1 )
#
# The overhead in time is the weekday conversion, the same as Zeller's congruence, which is of O( 1 ).

## Space Complexity: O( 1) 
#
# The overhead in space is the storage for list weekday_name and other temp date-time object, which is of O( 1 )



def test_bench():

    test_data = [ 
                    (31, 8, 2019),
                    (18, 7, 1999),
                    (15, 8, 1993)
                ]

    # expected output:
    '''
    Saturday
    Sunday
    Sunday
    '''


    for dd_mm_yyyy in test_data:

        print( Solution().dayOfTheWeek(*dd_mm_yyyy) )
    
    return 



if __name__ == '__main__':

    test_bench()