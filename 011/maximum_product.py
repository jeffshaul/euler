grid = []

with open('grid.txt') as f:
	for line in f:
		row = [int(cell) for cell in line.split()]
		grid.append(row)

maximum_product = 0

for r in range(len(grid)):
	for c in range(len(grid[0])):
		
		# Check eastern product
		if c + 3 < len(grid[0]):
			product = grid[r][c] * grid[r][c+1] * grid[r][c+2] * grid[r][c+3]
			if product > maximum_product:
				maximum_product = product
		
		# Check southern product
		if r + 3 < len(grid):
			product = grid[r][c] * grid[r+1][c] * grid[r+2][c] * grid[r+3][c]
			if product > maximum_product:
				maximum_product = product
		
		# Check southeastern product
		if r + 3 < len(grid) and c + 3 < len(grid[0]):
			product = grid[r][c] * grid[r+1][c+1] * grid[r+2][c+2] * grid[r+3][c+3]
			if product > maximum_product:
				maximum_product = product
		
		# Check southwestern product
		if r + 3 < len(grid) and c - 3 >= 0:
			product = grid[r][c] * grid[r+1][c-1] * grid[r+2][c-2] * grid[r+3][c-3]
			if product > maximum_product:
				maximum_product = product

print(maximum_product)