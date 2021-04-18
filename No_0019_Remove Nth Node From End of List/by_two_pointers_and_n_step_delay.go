package No_0019


//Definition for singly-linked list.
type ListNode struct {
    Val int
    Next *ListNode
}


 func removeNthFromEnd(head *ListNode, n int) *ListNode {
    
    dummyHead := &ListNode{-1, head}
    
    cur, prevOfRemoval := dummyHead, dummyHead
    
    for cur.Next != nil{
        
        // n step delay for prevOfRemoval
        if n <= 0 {
            prevOfRemoval = prevOfRemoval.Next
        }
        
        cur = cur.Next
        
        n -= 1
    }
    
    // Remove the N-th node from end of list
    nthNode := prevOfRemoval.Next
    prevOfRemoval.Next = nthNode.Next
    
    return dummyHead.Next
    
}



// n : the length of linked list

//// Time Complexity: O( n )
//
// The overhead in time is the cost of linear scan of linked list, which is of O( n ).

//// Space Complexity: O( 1 )
//
// The overhead in space is the storage for two-pointers, which is of O( 1 ).
