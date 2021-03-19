package main

func canVisitAllRooms(rooms [][]int) bool {

	// a map (so-called dictionary) to record visited rooms
	// Note: golang has no native set, so here we use map as alternative plan.
	visited := make(map[int]bool)

	// ------------------------------------------
	var dfs func(curRoom int)

	dfs = func(curRoom int) {

		if _, exist := visited[curRoom]; exist {

			// base case also known as stop condition
			return
		}

		// mark current room as visited
		visited[curRoom] = true

		// general case:
		for _, nextRoom := range rooms[curRoom] {

			// Visit next room in DFS
			dfs(nextRoom)
		}
		return
	}

	// ------------------------------------------

	// Launch DFS at room_#0
	dfs(0)

	// Return true if all rooms are visited
	return len(visited) == len(rooms)

}


// n : the number of rooms
// k : the average number of keys per room

//// Time Complexity: O( n * k )
//
// The overhead in time is the while loop, iterating on available_room, which if of O( n ),
// and the for loop, iterating on room_idx_with_key, which is of O( k )
//
// It takes O( n * k ) in total.


//// Space Complexity: O( n )
//
// The overhead in space is the storage for recursion call stack, which is of O( n )

// type "go test -v" in console to run unit test