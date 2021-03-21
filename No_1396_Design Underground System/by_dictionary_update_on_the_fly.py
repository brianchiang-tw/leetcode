'''

Description:

Implement the UndergroundSystem class:



void checkIn(int id, string stationName, int t)

A customer with a card id equal to id, gets in the station stationName at time t.
A customer can only be checked into one place at a time.



void checkOut(int id, string stationName, int t)

A customer with a card id equal to id, gets out from the station stationName at time t.



double getAverageTime(string startStation, string endStation)

Returns the average time to travel between the startStation and the endStation.
The average time is computed from all the previous traveling from startStation to endStation that happened directly.
Call to getAverageTime is always valid.

You can assume all calls to checkIn and checkOut methods are consistent. If a customer gets in at time t1 at some station, they get out at time t2 with t2 > t1. All events happen in chronological order.

 

Example 1:

Input
["UndergroundSystem","checkIn","checkIn","checkIn","checkOut","checkOut","checkOut","getAverageTime","getAverageTime","checkIn","getAverageTime","checkOut","getAverageTime"]
[[],[45,"Leyton",3],[32,"Paradise",8],[27,"Leyton",10],[45,"Waterloo",15],[27,"Waterloo",20],[32,"Cambridge",22],["Paradise","Cambridge"],["Leyton","Waterloo"],[10,"Leyton",24],["Leyton","Waterloo"],[10,"Waterloo",38],["Leyton","Waterloo"]]

Output
[null,null,null,null,null,null,null,14.00000,11.00000,null,11.00000,null,12.00000]

Explanation
UndergroundSystem undergroundSystem = new UndergroundSystem();
undergroundSystem.checkIn(45, "Leyton", 3);
undergroundSystem.checkIn(32, "Paradise", 8);
undergroundSystem.checkIn(27, "Leyton", 10);
undergroundSystem.checkOut(45, "Waterloo", 15);
undergroundSystem.checkOut(27, "Waterloo", 20);
undergroundSystem.checkOut(32, "Cambridge", 22);
undergroundSystem.getAverageTime("Paradise", "Cambridge");       // return 14.00000. There was only one travel from "Paradise" (at time 8) to "Cambridge" (at time 22)
undergroundSystem.getAverageTime("Leyton", "Waterloo");          // return 11.00000. There were two travels from "Leyton" to "Waterloo", a customer with id=45 from time=3 to time=15 and a customer with id=27 from time=10 to time=20. So the average time is ( (15-3) + (20-10) ) / 2 = 11.00000
undergroundSystem.checkIn(10, "Leyton", 24);
undergroundSystem.getAverageTime("Leyton", "Waterloo");          // return 11.00000
undergroundSystem.checkOut(10, "Waterloo", 38);
undergroundSystem.getAverageTime("Leyton", "Waterloo");          // return 12.00000



Example 2:

Input
["UndergroundSystem","checkIn","checkOut","getAverageTime","checkIn","checkOut","getAverageTime","checkIn","checkOut","getAverageTime"]
[[],[10,"Leyton",3],[10,"Paradise",8],["Leyton","Paradise"],[5,"Leyton",10],[5,"Paradise",16],["Leyton","Paradise"],[2,"Leyton",21],[2,"Paradise",30],["Leyton","Paradise"]]

Output
[null,null,null,5.00000,null,null,5.50000,null,null,6.66667]

Explanation
UndergroundSystem undergroundSystem = new UndergroundSystem();
undergroundSystem.checkIn(10, "Leyton", 3);
undergroundSystem.checkOut(10, "Paradise", 8);
undergroundSystem.getAverageTime("Leyton", "Paradise"); // return 5.00000
undergroundSystem.checkIn(5, "Leyton", 10);
undergroundSystem.checkOut(5, "Paradise", 16);
undergroundSystem.getAverageTime("Leyton", "Paradise"); // return 5.50000
undergroundSystem.checkIn(2, "Leyton", 21);
undergroundSystem.checkOut(2, "Paradise", 30);
undergroundSystem.getAverageTime("Leyton", "Paradise"); // return 6.66667
 

Constraints:

There will be at most 20000 operations.
1 <= id, t <= 106
All strings consist of uppercase and lowercase English letters, and digits.
1 <= stationName.length <= 10
Answers within 10-5 of the actual value will be accepted as correct.

'''



class UndergroundSystem:

    def __init__(self):
        
        ## dictionrary for passenger on-board record
        # key: id
        # value: pair of (chech-in station, check-in time)
        
        self.passenger = defaultdict( tuple )
        
        
        ## dictionary for traffic record
        # key: (startStation, endStation) pair
        # value: pair of (summation of traverl time, total count of traverl) 
        
        self.traffic_record = defaultdict( lambda:(0,0) )
    
    # ---------------------------------------------------------------
    
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        
        # update check-in station and check-in time pair
        
        self.passenger[id] = (stationName, t)
        
        return

    # ---------------------------------------------------------------
    
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        
        # update current traversal into corresponding traffic record
        
        start_station, start_time = self.passenger[id]
        end_station, end_time = stationName, t
        
        # get prev total travel time
        prev_sum_of_traverl_time, prev_count_of_traverl = self.traffic_record[(start_station, end_station)]
        
        self.traffic_record[(start_station, end_station)] = (prev_sum_of_traverl_time + end_time - start_time, prev_count_of_traverl+1)
        
        return
    
    # ---------------------------------------------------------------
    
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        
        # get total traffic time as well as total travel count from traffic record
        
        total_traffic_time, total_travel_count = self.traffic_record[(startStation, endStation)]
        
        
        # compute average travel tiem
        
        return total_traffic_time / total_travel_count
    
    # ---------------------------------------------------------------
    
# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)