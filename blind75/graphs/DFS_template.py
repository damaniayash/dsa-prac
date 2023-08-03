def traverse(matrix):

	rows, cols = len(matrix), len(matrix[0])
	visited = set()
	directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

	def dfs(node):

		if node in visited:
	 		return
		visited.add(node)

		# Traverse neighbors

		X,Y = node
		for dx,dy in directions:
			x, y = X + dx, Y + dy
			if 0 <= x < rows and 0 <= y < cols: 
			# Add any other checking here ^
				dfs(next_i, next_j)



    def dfs(node, v):

	    v.add(node)
	    X,Y = node

	    for dx,dy in neighbors:
	        x, y = X + dx, Y + dy
	        if 0 <= x < rows and 0 <= y < cols:
	            if (x,y) not in v:
	                v.add((x,y))
	                dfs((x,y),v)

	for i in range(rows):
		for j in range(cols):
			dfs(i, j)