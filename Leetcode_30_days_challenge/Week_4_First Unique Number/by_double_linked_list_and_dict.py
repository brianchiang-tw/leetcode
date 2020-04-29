'''

Description:

You have a queue of integers, you need to retrieve the first unique integer in the queue.

Implement the FirstUnique class:

FirstUnique(int[] nums) Initializes the object with the numbers in the queue.
int showFirstUnique() returns the value of the first unique integer of the queue, and returns -1 if there is no such integer.
void add(int value) insert value to the queue.
 

Example 1:

Input: 
["FirstUnique","showFirstUnique","add","showFirstUnique","add","showFirstUnique","add","showFirstUnique"]
[[[2,3,5]],[],[5],[],[2],[],[3],[]]
Output: 
[null,2,null,2,null,3,null,-1]

Explanation: 
FirstUnique firstUnique = new FirstUnique([2,3,5]);
firstUnique.showFirstUnique(); // return 2
firstUnique.add(5);            // the queue is now [2,3,5,5]
firstUnique.showFirstUnique(); // return 2
firstUnique.add(2);            // the queue is now [2,3,5,5,2]
firstUnique.showFirstUnique(); // return 3
firstUnique.add(3);            // the queue is now [2,3,5,5,2,3]
firstUnique.showFirstUnique(); // return -1

Example 2:

Input: 
["FirstUnique","showFirstUnique","add","add","add","add","add","showFirstUnique"]
[[[7,7,7,7,7,7]],[],[7],[3],[3],[7],[17],[]]
Output: 
[null,-1,null,null,null,null,null,17]

Explanation: 
FirstUnique firstUnique = new FirstUnique([7,7,7,7,7,7]);
firstUnique.showFirstUnique(); // return -1
firstUnique.add(7);            // the queue is now [7,7,7,7,7,7,7]
firstUnique.add(3);            // the queue is now [7,7,7,7,7,7,7,3]
firstUnique.add(3);            // the queue is now [7,7,7,7,7,7,7,3,3]
firstUnique.add(7);            // the queue is now [7,7,7,7,7,7,7,3,3,7]
firstUnique.add(17);           // the queue is now [7,7,7,7,7,7,7,3,3,7,17]
firstUnique.showFirstUnique(); // return 17

Example 3:

Input: 
["FirstUnique","showFirstUnique","add","showFirstUnique"]
[[[809]],[],[809],[]]
Output: 
[null,809,null,-1]

Explanation: 
FirstUnique firstUnique = new FirstUnique([809]);
firstUnique.showFirstUnique(); // return 809
firstUnique.add(809);          // the queue is now [809,809]
firstUnique.showFirstUnique(); // return -1

 

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^8
1 <= value <= 10^8
At most 50000 calls will be made to showFirstUnique and add.

'''



from typing import List


class Node:
    def __init__(self,val):
        self.val = val
        self.prev = None
        self.next = None

class Double_Linked_List:
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next, self.tail.prev = self.tail, self.head
        self.count = 0

    def insert(self, val):
        newNode = Node(val)
        newNode.prev = self.tail.prev 
        newNode.next = self.tail
        self.tail.prev.next = newNode
        self.tail.prev = newNode
        self.count += 1
        return newNode

    def remove(self, node):
        prev, nxt = node.prev, node.next
        node.prev.next = nxt
        node.next.prev = prev
        self.count -= 1
    
    def isEmpty(self):
        return (self.count == 0)


class FirstUnique:

    def __init__(self, nums: List[int]):
        self.Double_Linked_List = Double_Linked_List()
        self.numDict = {}
        
        for value in nums:
            self.add( value )
        
        
    def showFirstUnique(self) -> int:
        
        if self.Double_Linked_List.isEmpty():
            return -1
        return self.Double_Linked_List.head.next.val
    

    def add(self, value: int) -> None:
        
        if value not in self.numDict:
            self.numDict[ value ] = self.Double_Linked_List.insert( value )
            
        elif self.numDict[ value ] != -1:
            self.Double_Linked_List.remove(self.numDict[value])
            self.numDict[ value ] = -1
        
            

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)