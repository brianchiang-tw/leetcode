package main

//Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

func swapNodes(head *ListNode, k int) *ListNode {

	// record for first kth node, last kth node, and runnign cursor
	var firstK, lastK *ListNode = nil, nil
	cur := head

	// Step_#1: locate firstK to corresponding position
	for i := 0; i < (k - 1); i++ {
		cur = cur.Next
	}

	firstK = cur

	// Step_#2: locate lastK to corresponding position

	lastK, cur = head, cur.Next

	for cur != nil {
		cur, lastK = cur.Next, lastK.Next
	}

	// Step_#3: swap value between first kth node and last kth node
	firstK.Val, lastK.Val = lastK.Val, firstK.Val

	return head
}
