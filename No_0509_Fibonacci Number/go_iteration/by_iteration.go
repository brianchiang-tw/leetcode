package No_0509

func fib(n int) int {

    var getFib func(int) int
    
    memo := map[int]int{0:0, 1:1}
    
    getFib = func(n int) int{
        
        // base cases
        if value, exist := memo[n]; exist == true{
            return value
        }
        
        // general cases
        fibN := getFib(n-1) + getFib(n-2)
        memo[n] = fibN
        
        return fibN
    }
    
    return getFib(n)
}



// n : the value of input

//// Time Complexity: O( n )
//
// The overhead in time is the cost of iteration, which is of O( n )

//// Sapce Complexity: O( 1 )
//
// The overhead in space is the storage for loop index and temporary varaible, which is of O( 1 )

// run "go test -v" in consonle to run unittest