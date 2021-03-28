/*

Description:

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true



Example 2:

Input: "()[]{}"
Output: true



Example 3:

Input: "(]"
Output: false



Example 4:

Input: "([)]"
Output: false



Example 5:

Input: "{[]}"
Output: true

*/

package No_0020

import (
	"container/list"
	"sync"
)

func isValid(s string) bool {

	stack := newStack()

	pair := map[rune]rune{
		')': '(',
		']': '[',
		'}': '{',
	}

	for _, char := range s {

		if leftBracket, exist := pair[char]; exist {
			// check when we mmet right parenthesis

			if stack.Empty() || (!stack.Empty() && stack.Peek() != leftBracket) {

				// parenthesis mismatch
				return false
			} else {
				// parenthesis match
				stack.Pop()
			}
		} else {
			// push left parenthesis into stack
			stack.Push(char)
		}
	}

	// Accept in all parenthesis pair are matched
	return stack.Empty()
}


// n : the length of input string s

//// Time Complexity: O( n )
//
// The overhead is the for loop to linear scan each character in s


//// Space Complexity: O( n )
//
// The overhead is the variable to keep a stack to record the left braces including '(', '[' and '{'
// The size of stack is at most O( N )



// Implement Stack by golang linked list

type Stack struct {
	list     *list.List
	safeLock *sync.RWMutex
}

func newStack() *Stack {

	list := list.New()
	safeLock := &sync.RWMutex{}

	return &Stack{list, safeLock}
}

func (stack *Stack) Push(element interface{}) {

	stack.safeLock.Lock()
	defer stack.safeLock.Unlock()

	stack.list.PushBack(element)

	return
}

func (stack *Stack) Pop() interface{} {

	stack.safeLock.Lock()
	defer stack.safeLock.Unlock()

	element := stack.list.Back()

	if element != nil {
		stack.list.Remove(element)
		return element.Value
	}
	return nil
}

func (stack *Stack) Peek() interface{} {

	stack.safeLock.Lock()
	defer stack.safeLock.Unlock()

	element := stack.list.Back()

	if element != nil {
		return element.Value
	}
	return nil
}

func (stack *Stack) Len() int {
	return stack.list.Len()
}

func (stack *Stack) Empty() bool {
	return stack.list.Len() == 0
}
