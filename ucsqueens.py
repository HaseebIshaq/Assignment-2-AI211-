import heapq

class Board:
    def __init__(self, n, board=None, cost=0):
        self.n = n
        if board is None:
            self.board = [[False] * n for _ in range(n)]
        else:
            self.board = board
        self.cost = cost
    
    def is_valid(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.board[i][j]:
                    # Check row and column
                    for k in range(self.n):
                        if k != i and self.board[k][j]:
                            return False
                        if k != j and self.board[i][k]:
                            return False
                    # Check diagonal
                    for k in range(1, self.n):
                        if i+k < self.n and j+k < self.n and self.board[i+k][j+k]:
                            return False
                        if i+k < self.n and j-k >= 0 and self.board[i+k][j-k]:
                            return False
                        if i-k >= 0 and j+k < self.n and self.board[i-k][j+k]:
                            return False
                        if i-k >= 0 and j-k >= 0 and self.board[i-k][j-k]:
                            return False
        return True
    
    def place_queen(self, i, j):
        self.board[i][j] = True
    
    def __str__(self):
        return '\n'.join([''.join(['Q' if self.board[i][j] else '.' for j in range(self.n)]) for i in range(self.n)])
    
    def __lt__(self, other):
        return self.cost < other.cost
    
def ucs(n):
    q = [(0, Board(n))]
    heapq.heapify(q)
    while q:
        _, board = heapq.heappop(q)
        if board.is_valid():
            if sum([1 for row in board.board for cell in row if cell]) == n:
                return board
            for i in range(n):
                for j in range(n):
                    if not board.board[i][j]:
                        new_board = Board(n)
                        new_board.board = [row[:] for row in board.board]
                        new_board.place_queen(i, j)
                        new_board.cost = board.cost + 1
                        heapq.heappush(q, (new_board.cost, new_board))

board = ucs(8)
if board:
    print(board)
else:
    print("No solution found.")
