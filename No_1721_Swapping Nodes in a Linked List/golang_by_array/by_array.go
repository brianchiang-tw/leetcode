package main

import(

)


//Definition for singly-linked list.
type ListNode struct {
    Val int
    Next *ListNode
}

func swapNodes(head *ListNode, k int) *ListNode {
    
    // buffer list to save linked list, and running cursot
    buffer, cur := make([]*ListNode, 0), head
    
    // Step_#1: save linked list into buffer list
    
    for cur != nil{
        
        buffer = append(buffer, cur)
        cur = cur.Next    
        
    }
    
    // Step_#2: swap value between first kth and last kth node
    // Note: take care that most programming is zero-base numbering
    
    buffer[k-1].Val, buffer[len(buffer)-k].Val = buffer[len(buffer)-k].Val, buffer[k-1].Val
    
    return buffer[0]
}