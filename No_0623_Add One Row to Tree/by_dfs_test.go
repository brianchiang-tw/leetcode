package main

import (
	"testing"
	"reflect"
)

// type TreeNode struct {
//     Val int
//     Left *TreeNode
//     Right *TreeNode
// }


func levelOrder(root *TreeNode) [][]int {

	if root == nil { return [][]int{} } 

    var res [][]int
    queue := []*TreeNode{root}

    for level := 0; len(queue) > 0; level++ {  //level - to track where we need to insert values
        res = append(res, []int{}) //adding slice for the new "level" of values
        for levelSize := len(queue); levelSize > 0; levelSize-- { 
		
            if queue[0].Left != nil { queue = append(queue, queue[0].Left) } //adding next nodes to the queue
            if queue[0].Right != nil { queue = append(queue, queue[0].Right) }
			res[level] = append(res[level], queue[0].Val) //adding first element in the queue to a "level" slice
            queue = queue[1:] //deque first element
        }
    }
    return res
}


func TestCase_1(t *testing.T){

	root := &TreeNode{4, nil, nil}

	root.Left = &TreeNode{2, nil, nil}
	root.Right = &TreeNode{6, nil, nil}

	root.Left.Left = &TreeNode{3, nil, nil}
	root.Left.Right = &TreeNode{1, nil, nil}

	root.Right.Left = &TreeNode{5, nil, nil}

	root = addOneRow(root, 1, 2)

	result := levelOrder(root)
	expected := [][]int{{4},{1,1},{2,6},{3,1,5}}

	if !reflect.DeepEqual(result, expected){
		t.Errorf("Running result = %v; \n expected = %v", result, expected)
	}
}



func TestCase_2(t *testing.T){

	root := &TreeNode{4, nil, nil}

	root.Left = &TreeNode{2, nil, nil}

	root.Left.Left = &TreeNode{3, nil, nil}
	root.Left.Right = &TreeNode{1, nil, nil}


	root = addOneRow(root, 1, 3)

	result := levelOrder(root)
	expected := [][]int{{4},{2},{1,1},{3,1}}

	if !reflect.DeepEqual(result, expected){
		t.Errorf("Running result = %v; \n expected = %v", result, expected)
	}
}