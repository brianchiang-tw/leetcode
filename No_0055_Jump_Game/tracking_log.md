Python O( n ) on greedy strategy and backtracking.

Method_#1: greedy strategy with furthest coverage update

Example explanation:

input nums= [2,3,1,1,4]

furthest_coverage is initialized to nums[0] = 2

1st iteration on i = 0:

0 + nums[0] = 0 + 2 = 2
furthest_coverage = max(2, 2) = 2

input nums= [2,3,1,1,4]

2nd iteration on i = 1:

1 + nums[1] = 1 + 3 = 4
furthest_coverage = max(2, 4) = 4

input nums= [2,3,1,1,4]

3rd iteration on i = 2:

furthest_coverage = 4 >= len(nums)-1 = 4, has reached the destination

return True

class Solution:
    

    # Greedy stragegy:
    # Maintain a variable to keep track of furthest_coverage
    def canJump(self, nums: List[int]) -> bool:
        
        size = len(nums)
        destination = size-1
        furthest_coverage = nums[0]
        
        for i in range( size ):
            
            if i > furthest_coverage:
                # travel to furtest coverage at most
                return False
            
            if furthest_coverage >= destination:
                # reach the destination
                return True
            
			# update furthest_coverage on the way to destination
            furthest_coverage = max(furthest_coverage, i + nums[i])
            
			
		# check furthest coverage reach destination or not	
        return furthest_coverage >= destination
Method_#2: greedy strategy with frontier backtracking update

Example explanation:

input nums= [2,3,1,1,4]

frontier_backtracking is initialized to len(nums)-1 = 5 - 1 = 4

input nums= [2,3,1,1,4]

1st iteration on i == 3:

3 + nums[i=3] = 3 + 1 = 4 >= frontier_backtracking

update frontier_backtracking = i
-> frontier_backtracking = 3

input nums= [2,3,1,1,4]

2st iteration on i == 2:

2 + nums[i=2] = 2 + 1 = 3 >= frontier_backtracking

update frontier_backtracking = i
-> frontier_backtracking = 2

input nums= [2,3,1,1,4]

3rd iteration on i == 1:

1 + nums[i=1] = 1 + 3 = 4 >= frontier_backtracking

update frontier_backtracking = i
-> frontier_backtracking = 1

input nums= [2,3,1,1,4]

4th iteration on i == 0:

0 + nums[i=0] = 0 + 2 = 2 >= frontier_backtracking

update frontier_backtracking = i
-> frontier_backtracking = 0

Final judgement:

frontier_backtracking = 0 == start point index

return True

class Solution:
    

    # Greedy strategy
    # Maintain a variable to keep track of frontier_backtracking
    def canJump(self, nums: List[int]) -> bool:
        
        size = len(nums)
        start_point = 0
        frontier_backtracking = size-1
        
        # backtracking from destination to start point
        for i in reversed( range( 0, size-1 ) ):
            
            # update frontier_backtracking as much as possible
            if i + nums[i] >= frontier_backtracking:
                frontier_backtracking = i

        
        return frontier_backtracking == start_point