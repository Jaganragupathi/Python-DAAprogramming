def g(board):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    m, n = len(board), len(board[0])
    original = [[board[r][c] for c in range(n)] for r in range(m)]
    for r in range(m):
        for c in range(n):
            live_neighbors = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and original[nr][nc] == 1:
                    live_neighbors += 1
            if original[r][c] == 1:
                if live_neighbors < 2 or live_neighbors > 3:
                    board[r][c] = 0
            else:
                if live_neighbors == 3:
                    board[r][c] = 1
    
    return board
print(g([[0,1,0],[0,0,1],[1,1,1],[0,0,0]]))  
print(g([[1,1],[1,0]]))                      
