/*

Description:

Given the root of a binary tree and two integers val and depth, add a row of nodes with value val at the given depth depth.

Note that the root node is at depth 1.

The adding rule is:

Given the integer depth, for each not null tree node cur at the depth depth - 1, create two tree nodes with value val as cur's left subtree root and right subtree root.
cur's original left subtree should be the left subtree of the new left subtree root.
cur's original right subtree should be the right subtree of the new right subtree root.
If depth == 1 that means there is no depth depth - 1 at all, then create a tree node with value val as the new root of the whole original tree, and the original tree is the new root's left subtree.
 

Example 1:


Input: root = [4,2,6,3,1,5], val = 1, depth = 2
Output: [4,1,1,2,null,null,6,3,1,5]



Example 2:


Input: root = [4,2,null,3,1], val = 1, depth = 3
Output: [4,2,null,1,1,3,null,null,1]
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
The depth of the tree is in the range [1, 104].
-100 <= Node.val <= 100
-105 <= val <= 105
1 <= depth <= the depth of tree + 1

*/



package main

import(

)

type TreeNode struct {
    Val int
     Left *TreeNode
    Right *TreeNode
}


func addOneRow(root *TreeNode, v int, d int) *TreeNode {
    
    if root == nil{
        
        // base case: empty tree
        
        return nil
        
    } else if d == 1{
        
        // base case: add one row above original root
        
        return &TreeNode{v, root, nil}
        
    } else if d == 2{
        
        // base case: add one row just below original root
        
        root.Left = &TreeNode{v, root.Left, nil}
        root.Right = &TreeNode{v, nil, root.Right}
        
        return root
        
    } else{
        
        // general case: depth >= 3
        // do it in DFS with common pattern
        
        root.Left = addOneRow(root.Left, v, d-1)
        root.Right = addOneRow(root.Right, v, d-1)
        
        return root
    }
    
    
    
}
//end of function addOneRow



// n : the number of nodes

//// Time Complexity: O( n )
//
// The overhead in time is the cost of DFS, which is of O( n )

//// Space Complexity: O( n )
//
// The overhead in space is the storage for recursion, which is of O( n )

// type "go test -v" in console to run unittest

