class Solution(object):
	def solve(self, board):
		"""
		:type board: List[List[str]]
		:rtype: None Do not return anything, modify board in-place instead.
		"""
		
		positions = set()
		
		def dfs(row, col):
			if (row,col) in positions:
				return
			
			if row > len(board) -1 or row <0:
				return
			
			if col > len(board[0]) -1 or col<0:
				return
			
			if board[row][col] == "X":
				return
			
			positions.add((row, col))
	
			dfs(row+1, col)
			dfs(row-1, col)
			dfs(row, col + 1)
			dfs(row, col -1)
		
		row_0 = board[0]
		row_n = board[len(board) -1]
		col_0 = [row[0] for row in board]
		col_n = [row[-1] for row in board]
		
		for index, val in enumerate(row_0):
			if val == "O":
				dfs(0, index)

		for index, val in enumerate(row_n):
			if val == "O":
				dfs(len(board) - 1, index)

		for index, val in enumerate(col_0):
			if val == "O":
				dfs(index, 0)
		
		for index, val in enumerate(col_n):
			if val == "O":
				dfs(index, len(board[0]) - 1)
		
		for row in range(len(board)):
			for col in range(len(board[0])):
				if (row,col) not in positions:
					board[row][col] = "X"
					
		return board
            