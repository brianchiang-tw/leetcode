package No_0234

//Definition for singly-linked list.
type ListNode struct {
    Val int
    Next *ListNode
}


 func isPalindrome(head *ListNode) bool {
    
    // use two pointers to locate the mid-point of linked list
    slow, fast := head, head
    
    for fast != nil && fast.Next != nil{
        
        slow = slow.Next
        fast = fast.Next.Next
    }
    
    // skip central node if length of linked list is odd number
    if fast != nil{
        slow = slow.Next
    }
    
    // Reverse the linkage of right half of linked list
    tail := reverseLinkedList( slow )
    
    // Accept if left half sequence == right half sequence
    // Reject, otherwise
    for tail != nil{
        
        if tail.Val != head.Val{
            return false
        }
        
        head, tail = head.Next, tail.Next
    }
    
    return true
}


func reverseLinkedList(node *ListNode) *ListNode{
    
    var prev *ListNode = nil
    var cur *ListNode = node
    
    for cur != nil{
        
        // backup original next hop
        nextHop := cur.Next
        
        // reverse linkage direction
        cur.Next = prev
        prev = cur
        
        // move to next position
        cur = nextHop
        
    }
    
    // new head of reversed linked list
    return prev
}



// n : the length of linked list

//// Time Complexity: O( n )
//
// The overhead in time is the cost of iteration, which is of O( n )

//// Space Complexity: O( 1 )
//
// The overhead in space is the storage for loop index and temporary variable, which is of O( 1 )
