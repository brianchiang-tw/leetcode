/*

Description:

Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

 

Example 1:


Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]



Example 2:

Input: head = [2,1], x = 2
Output: [1,2]
 

Constraints:

The number of nodes in the list is in the range [0, 200].
-100 <= Node.val <= 100
-200 <= x <= 200

*/


package No_0086

//Definition for singly-linked list.
type ListNode struct {
    Val int
    Next *ListNode
}


 func partition(head *ListNode, x int) *ListNode {
    
    if head == nil{
        
        // Quick response for empty linked list
        return nil
    }
    
    // -101 as dummy head value for lessThan
    lessThan := &ListNode{-101, nil}
    
    // -102 as dummy head value for notLessThan
    notLessThan := &ListNode{-102, nil}
    
    // backup dummy head position for less_than and not_less_than for linkage update later
    headOfLessThan, headOfNotLessThan := lessThan, notLessThan
    
    //// Seperate original linked list into two lists
    // one is less than x, where node value < x
    // the other is not less than x, where node value >= x    
    
    cur := head
    
    for cur != nil{
        
        if cur.Val < x{
            lessThan.Next = cur
            lessThan = lessThan.Next
        }else{
            notLessThan.Next = cur
            notLessThan = notLessThan.Next
        }
        
        cur = cur.Next
    }
    
    //// Update linkage
    
    // connect less than's tail to not_less_than
    lessThan.Next = headOfNotLessThan.Next
    
    // let not_less_than's tail point to None (i.e., empty node)
    notLessThan.Next = nil
    
    return headOfLessThan.Next
    
}


// n : the length of linked list

//// Time Complexity: O( n )
//
// The overhead in time is the cost of linear traversal, which is of O( n )

//// Space Complexity: O( 1 )
//
// The overhead in space is the storage of two-pointers, which is of O( 1 )
