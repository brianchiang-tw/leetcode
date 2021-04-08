package No_0032

func longestValidParentheses(s string) int {
    
    // stack, used to record index of parenthesis
    // initialized to -1 as dummy head for valid parenthesis length computation
    stack := []int{-1}
    
    max_length := 0
    
    // linear scan each index and character in input string s
    for curIdx, char := range s{
        
        if char == '('{
            
            // push when current char is (
            stack = append( stack, curIdx)
            
        }else{
            
            // pop when current char is )
            stack = stack[:len(stack)-1]
            
            if len(stack)==0{
                
                // stack is empty, push current index into stack
                stack = append( stack, curIdx)
            }else{
                
                // stack is non-empty, update maximal valud parentheses length
                
                max_length = max( max_length, curIdx - stack[ len(stack)-1 ] )
            }
            
        }
        
    }
    
    return max_length
    
}

func max(a, b int)int{
    
    if a > b{
        return a
    }
    
    return b
}




// n : the character length of s

//// Time Compleity: O( n )
//
// The overhead in time is the iteration, which is of O( n )

//// Space Complexity: O( n )
//
// The overhead in space is the storage of stack, which is of O( n )
