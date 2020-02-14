# This implementation is out of time limit.


from collections import deque

class Solution(object):
    def pathsWithMaxScore(self, board):
        """
        :type board: List[str]
        :rtype: List[int]
        """
        
        
        def bfs( board, traversal_queue ):
            
            while traversal_queue:
            
                cur_y, cur_x, cur_score = traversal_queue.popleft()

                if (cur_y, cur_x) == ( 0, 0):
                    path_with_cost.append(cur_score)
                    # this path is accomplished
                    continue

                elif board[cur_y][cur_x] == 'X':
                    # discard this path due to obstacle
                    continue
                
                else:
                    # update current score
                    
                    if board[cur_y][cur_x] != 'S':
                        cur_score += int( board[cur_y][cur_x] )
                    
                    # add next three moves if it is feasible
                    for offset_y, offset_x in [(-1, 0), (-1,-1), (0,-1)]:
                        
                        next_y = cur_y + offset_y
                        next_x = cur_x + offset_x
                        
                        if next_y >= 0 and next_x >= 0:
                            traversal_queue.append( (next_y, next_x, cur_score) )
        
        # ---------
        path_with_cost = []
        size = len(board)
        
        start_y, start_x = size-1, size-1
        
        bfs_queue = deque( [(start_y, start_x, 0) ] )
        
        #print(bfs_queue)
        
        bfs( board, bfs_queue)
        
        if len(path_with_cost) == 0:
            return [0, 0]
        
        else:
            max_score = max(path_with_cost)
        
            path_count_with_max_score = path_with_cost.count(max_score)
        
            return [max_score, path_count_with_max_score]