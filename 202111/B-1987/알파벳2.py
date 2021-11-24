import sys
input = sys.stdin.readline

def alphabet(board, rows, cols):
    q = set([(0, 0, board[0][0])])
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    max_len = 1
    while q:
        r, c, path = q.pop()
        max_len = max(max_len, len(path))
        if max_len == 26:
            return 26
        
        for dr, dc in moves:
            nr, nc = r + dr, c + dc 
            if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] not in path:
                q.add((nr, nc, path + board[nr][nc]))    
    return max_len


if __name__ == '__main__':
    input = sys.stdin.readline
    rows, cols = map(int, input().split())
    board = [input().strip('\n') for _ in range(rows)]
    print(alphabet(board, rows, cols))

    print(board)